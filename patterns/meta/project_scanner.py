#!/usr/bin/env python3
"""
Project Scanner for AGET Migration Assessment
Part of EP-7: Project Scanner Pattern

Scans repositories to assess AGET migration status and track versions.
Supports partial migrations and gradual adoption.
"""

import os
import json
import yaml
from pathlib import Path
from datetime import datetime
from enum import Enum
import argparse
import sys

class MigrationStatus(Enum):
    """Migration status levels for projects."""
    NOT_STARTED = "not_started"        # No AGET files present
    EXPLORING = "exploring"            # Has README references but no files
    PARTIAL = "partial"               # Some AGET patterns adopted
    SUBSTANTIAL = "substantial"       # Most patterns adopted, some legacy
    COMPLETE = "complete"            # Full AGET adoption
    CUSTOMIZED = "customized"        # AGET + significant custom patterns

class ProjectScanner:
    """Scan projects for AGET migration status."""
    
    # Files that indicate AGET adoption
    AGET_INDICATORS = {
        'core': ['AGENTS.md', '.aget/version.json'],
        'session': ['scripts/aget_session_protocol.py', 'scripts/session_protocol.py'],
        'housekeeping': ['scripts/aget_housekeeping_protocol.py', 'scripts/housekeeping_protocol.py'],
        'legacy': ['CLAUDE.md', '.claude_config', 'claude_*.py'],
        'compatibility': ['.cursorrules', '.aider.conf.yml', '.windsurfrules']
    }
    
    def __init__(self, root_path='.'):
        self.root_path = Path(root_path)
        self.projects = {}
        self.summary = {
            'total_projects': 0,
            'migrated': 0,
            'partial': 0,
            'not_started': 0,
            'scan_time': datetime.now().isoformat()
        }
    
    def scan_directory(self, path):
        """Scan a single directory for AGET status."""
        project_path = Path(path)
        if not project_path.exists():
            return None
        
        status = {
            'path': str(project_path),
            'name': project_path.name,
            'migration_status': MigrationStatus.NOT_STARTED,
            'aget_version': None,
            'migration_date': None,
            'patterns_adopted': [],
            'patterns_missing': [],
            'legacy_files': [],
            'compatibility_files': [],
            'score': 0
        }
        
        # Check for version tracking
        version_file = project_path / '.aget' / 'version.json'
        if version_file.exists():
            try:
                with open(version_file) as f:
                    version_data = json.load(f)
                    status['aget_version'] = version_data.get('version', 'unknown')
                    status['migration_date'] = version_data.get('migration_date')
                    status['migration_phase'] = version_data.get('phase', 'unknown')
            except:
                pass
        
        # Check for AGENTS.md with version header
        agents_file = project_path / 'AGENTS.md'
        if agents_file.exists():
            try:
                content = agents_file.read_text()[:500]  # Check first 500 chars
                if '@aget-version:' in content:
                    for line in content.split('\n'):
                        if '@aget-version:' in line:
                            status['aget_version'] = line.split('@aget-version:')[1].strip()
                            break
            except:
                pass
        
        # Score the migration level
        score = 0
        patterns = []
        missing = []
        
        # Core files (40 points)
        if agents_file.exists():
            score += 20
            patterns.append('AGENTS.md')
        else:
            missing.append('AGENTS.md')
        
        if (project_path / '.aget').exists():
            score += 20
            patterns.append('.aget directory')
        else:
            missing.append('.aget directory')
        
        # Session patterns (30 points)
        session_files = ['scripts/aget_session_protocol.py', 'scripts/session_protocol.py']
        if any((project_path / f).exists() for f in session_files):
            score += 30
            patterns.append('session protocols')
        else:
            missing.append('session protocols')
        
        # Housekeeping patterns (20 points)
        housekeeping_files = ['scripts/aget_housekeeping_protocol.py', 'scripts/housekeeping_protocol.py']
        if any((project_path / f).exists() for f in housekeeping_files):
            score += 20
            patterns.append('housekeeping protocols')
        else:
            missing.append('housekeeping protocols')
        
        # Pattern directories (10 points)
        if (project_path / 'patterns').exists():
            score += 10
            patterns.append('patterns directory')
            # Count pattern categories
            pattern_dirs = [d for d in (project_path / 'patterns').iterdir() if d.is_dir()]
            if pattern_dirs:
                patterns.append(f"{len(pattern_dirs)} pattern categories")
        
        # Check for legacy files
        legacy = []
        for legacy_file in self.AGET_INDICATORS['legacy']:
            if (project_path / legacy_file).exists():
                legacy.append(legacy_file)
        
        # Check for compatibility files
        compat = []
        for compat_file in self.AGET_INDICATORS['compatibility']:
            if (project_path / compat_file).exists():
                compat.append(compat_file)
        
        # Determine migration status based on score
        if score == 0:
            status['migration_status'] = MigrationStatus.NOT_STARTED
        elif score < 30:
            status['migration_status'] = MigrationStatus.EXPLORING
        elif score < 60:
            status['migration_status'] = MigrationStatus.PARTIAL
        elif score < 90:
            status['migration_status'] = MigrationStatus.SUBSTANTIAL
        else:
            status['migration_status'] = MigrationStatus.COMPLETE
        
        # Check for customization
        if score >= 60 and (project_path / 'patterns').exists():
            custom_patterns = len([d for d in (project_path / 'patterns').iterdir() 
                                 if d.is_dir() and d.name not in ['session', 'housekeeping', 'documentation']])
            if custom_patterns > 2:
                status['migration_status'] = MigrationStatus.CUSTOMIZED
        
        status['patterns_adopted'] = patterns
        status['patterns_missing'] = missing
        status['legacy_files'] = legacy
        status['compatibility_files'] = compat
        status['score'] = score
        
        return status
    
    def scan_all_projects(self):
        """Scan all subdirectories for projects."""
        # First check if current directory is itself a project
        if (self.root_path / '.git').exists() or (self.root_path / 'AGENTS.md').exists():
            root_status = self.scan_directory(self.root_path)
            if root_status:
                self.projects['.'] = root_status
        
        # Then scan subdirectories
        for item in self.root_path.iterdir():
            if item.is_dir() and not item.name.startswith('.'):
                # Check if it's a git repo or has AGET files
                if (item / '.git').exists() or (item / 'AGENTS.md').exists() or (item / 'CLAUDE.md').exists():
                    status = self.scan_directory(item)
                    if status:
                        self.projects[item.name] = status
        
        # Update summary
        self.summary['total_projects'] = len(self.projects)
        for project in self.projects.values():
            if project['migration_status'] == MigrationStatus.NOT_STARTED:
                self.summary['not_started'] += 1
            elif project['migration_status'] in [MigrationStatus.EXPLORING, MigrationStatus.PARTIAL]:
                self.summary['partial'] += 1
            else:
                self.summary['migrated'] += 1
    
    def generate_report(self, format='text'):
        """Generate migration status report."""
        if format == 'json':
            return json.dumps({
                'summary': self.summary,
                'projects': {k: {**v, 'migration_status': v['migration_status'].value} 
                            for k, v in self.projects.items()}
            }, indent=2)
        
        # Text report
        lines = []
        lines.append("="*60)
        lines.append("AGET Migration Status Report")
        lines.append("="*60)
        lines.append(f"Scan Time: {self.summary['scan_time']}")
        lines.append(f"Total Projects: {self.summary['total_projects']}")
        lines.append(f"  - Fully Migrated: {self.summary['migrated']}")
        lines.append(f"  - Partial Migration: {self.summary['partial']}")
        lines.append(f"  - Not Started: {self.summary['not_started']}")
        lines.append("")
        
        # Group by status
        by_status = {}
        for name, project in self.projects.items():
            status = project['migration_status']
            if status not in by_status:
                by_status[status] = []
            by_status[status].append((name, project))
        
        # Report each group
        status_order = [
            MigrationStatus.COMPLETE,
            MigrationStatus.CUSTOMIZED,
            MigrationStatus.SUBSTANTIAL,
            MigrationStatus.PARTIAL,
            MigrationStatus.EXPLORING,
            MigrationStatus.NOT_STARTED
        ]
        
        status_icons = {
            MigrationStatus.COMPLETE: "✅",
            MigrationStatus.CUSTOMIZED: "🚀",
            MigrationStatus.SUBSTANTIAL: "🟡",
            MigrationStatus.PARTIAL: "🟠",
            MigrationStatus.EXPLORING: "🔍",
            MigrationStatus.NOT_STARTED: "⭕"
        }
        
        for status in status_order:
            if status in by_status:
                lines.append(f"\n{status_icons[status]} {status.value.replace('_', ' ').title()}:")
                lines.append("-" * 40)
                
                for name, project in by_status[status]:
                    lines.append(f"  {name}:")
                    if project['aget_version']:
                        lines.append(f"    Version: {project['aget_version']}")
                    if project['migration_date']:
                        lines.append(f"    Migrated: {project['migration_date']}")
                    lines.append(f"    Score: {project['score']}/100")
                    
                    if project['patterns_adopted']:
                        lines.append(f"    ✓ Adopted: {', '.join(project['patterns_adopted'][:3])}")
                    if project['patterns_missing']:
                        lines.append(f"    ✗ Missing: {', '.join(project['patterns_missing'][:3])}")
                    if project['legacy_files']:
                        lines.append(f"    ⚠️ Legacy: {', '.join(project['legacy_files'])}")
        
        lines.append("\n" + "="*60)
        lines.append("Recommendations:")
        lines.append("-" * 40)
        
        # Generate recommendations
        if self.summary['not_started'] > 0:
            lines.append("• Run discovery mechanism (EP-1) on unmigrated projects")
        if self.summary['partial'] > 0:
            lines.append("• Use migration assistant (EP-2) to complete partial migrations")
        
        # Check for legacy cleanup opportunities
        legacy_count = sum(1 for p in self.projects.values() if p['legacy_files'])
        if legacy_count > 0:
            lines.append(f"• Run migration cleanup (EP-11) on {legacy_count} projects with legacy files")
        
        return "\n".join(lines)
    
    def save_report(self, output_dir=None):
        """Save detailed report to .aget directory."""
        if output_dir is None:
            output_dir = self.root_path / '.aget'
        
        output_dir = Path(output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)
        
        # Save JSON report
        report_file = output_dir / 'migration_report.json'
        report_file.write_text(self.generate_report('json'))
        
        # Save text report
        text_file = output_dir / 'migration_report.txt'
        text_file.write_text(self.generate_report('text'))
        
        return report_file


def apply_pattern(project_path: Path = None):
    """
    Apply the project scanner pattern.

    This function is called by `aget apply meta/project_scanner`.
    """
    try:
        if project_path is None:
            project_path = Path.cwd()

        scanner = ProjectScanner(project_path)
        scanner.scan()

        print("🔍 AGET Migration Scanner")
        print("=" * 50)
        print(scanner.generate_report('text'))

        return {
            "status": "success",
            "projects_scanned": scanner.summary['total_projects'],
            "migrated": scanner.summary['migrated'],
            "partial": scanner.summary['partial']
        }

    except Exception as e:
        print(f"❌ Error scanning projects: {e}")
        return {"status": "error", "message": str(e)}


def main():
    parser = argparse.ArgumentParser(description='Scan projects for AGET migration status')
    parser.add_argument('path', nargs='?', default='.',
                       help='Root path to scan (default: current directory)')
    parser.add_argument('--json', action='store_true',
                       help='Output in JSON format')
    parser.add_argument('--quiet', '-q', action='store_true',
                       help='Minimal output')
    parser.add_argument('--save', action='store_true',
                       help='Save detailed report to .aget directory')
    
    args = parser.parse_args()
    
    scanner = ProjectScanner(args.path)
    scanner.scan_all_projects()
    
    if args.save:
        report_file = scanner.save_report()
        if not args.quiet:
            print(f"Report saved to: {report_file}")
    
    if args.quiet:
        # Just return exit code
        if scanner.summary['not_started'] == scanner.summary['total_projects']:
            return 2  # No projects migrated
        elif scanner.summary['migrated'] == scanner.summary['total_projects']:
            return 0  # All projects migrated
        else:
            return 1  # Partial migration
    
    print(scanner.generate_report('json' if args.json else 'text'))
    
    # Exit codes
    if scanner.summary['not_started'] == scanner.summary['total_projects']:
        return 2
    elif scanner.summary['migrated'] == scanner.summary['total_projects']:
        return 0
    else:
        return 1

if __name__ == '__main__':
    sys.exit(main())