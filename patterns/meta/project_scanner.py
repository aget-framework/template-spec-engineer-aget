#!/usr/bin/env python3
"""
AGET Project Scanner
Scans all sub-projects in meta-repository for AGET migration readiness

Exit Codes:
  0 - All projects fully migrated
  1 - Partial migration (some projects migrated)
  2 - No migration started
  3 - Script execution error

Usage:
  python3 project_scanner.py [options]

Options:
  --quiet, -q      Minimal output (just summary)
  --verbose, -v    Detailed output with debug info
  --json           Output in JSON format
  --no-save        Don't save report to .aget/project_scan.json
  --exit-zero      Always exit with 0 (for CI/CD compatibility)
"""

import os
import sys
import json
import argparse
import subprocess
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Optional, Tuple


class ProjectScanner:
    """Scans projects for AGET compatibility and migration status"""

    def __init__(self, root_path: Path = None):
        self.root = root_path or Path.cwd()
        self.results = {
            'scan_date': datetime.now().isoformat(),
            'root_path': str(self.root),
            'projects': {},
            'summary': {
                'total': 0,
                'git_repos': 0,
                'has_claude_md': 0,
                'has_agents_md': 0,
                'has_aget_version': 0,
                'fully_migrated': 0,
                'partially_migrated': 0,
                'not_started': 0
            }
        }

    def is_git_repo(self, path: Path) -> bool:
        """Check if directory is a git repository"""
        return (path / '.git').exists()

    def check_file_exists(self, path: Path, filename: str) -> bool:
        """Check if a file exists in the given path"""
        return (path / filename).exists()

    def read_aget_version(self, path: Path) -> Optional[Dict]:
        """Read AGET version info if present"""
        version_file = path / '.aget' / 'version.json'
        if version_file.exists():
            try:
                with open(version_file) as f:
                    return json.load(f)
            except:
                return None
        return None

    def check_agents_md_header(self, path: Path) -> Optional[str]:
        """Check AGENTS.md for @aget-version header"""
        agents_file = path / 'AGENTS.md'
        if agents_file.exists():
            try:
                with open(agents_file) as f:
                    for line in f:
                        if '@aget-version:' in line:
                            return line.strip()
                        if line.startswith('##'):  # Stop at first section
                            break
            except:
                pass
        return None

    def analyze_project(self, project_path: Path) -> Dict:
        """Analyze a single project for AGET status"""
        project_name = project_path.name

        # Skip non-directories and hidden directories
        if not project_path.is_dir() or project_name.startswith('.'):
            return None

        analysis = {
            'name': project_name,
            'path': str(project_path),
            'is_git_repo': self.is_git_repo(project_path),
            'has_claude_md': self.check_file_exists(project_path, 'CLAUDE.md'),
            'has_agents_md': self.check_file_exists(project_path, 'AGENTS.md'),
            'has_makefile': self.check_file_exists(project_path, 'Makefile'),
            'has_patterns_dir': self.check_file_exists(project_path, 'patterns'),
            'has_scripts_dir': self.check_file_exists(project_path, 'scripts'),
            'aget_version': None,
            'migration_status': 'not_started',
            'agents_md_header': None
        }

        # Check for AGET version
        aget_info = self.read_aget_version(project_path)
        if aget_info:
            analysis['aget_version'] = aget_info.get('aget_version')
            analysis['migration_status'] = aget_info.get('status', 'unknown')

        # Check AGENTS.md header
        analysis['agents_md_header'] = self.check_agents_md_header(project_path)

        # Determine migration status if not explicitly set
        if analysis['migration_status'] == 'not_started':
            if analysis['has_agents_md'] and analysis['has_patterns_dir']:
                analysis['migration_status'] = 'fully_migrated'
            elif analysis['has_agents_md'] or analysis['has_patterns_dir']:
                analysis['migration_status'] = 'partially_migrated'
            elif analysis['has_claude_md']:
                analysis['migration_status'] = 'claude_compatible'
            else:
                analysis['migration_status'] = 'not_applicable'

        return analysis

    def scan_all_projects(self) -> Dict:
        """Scan all subdirectories for projects"""
        # Special handling for known submodules
        submodules = ['CCB', 'GM-RKB']

        for item in self.root.iterdir():
            # Skip certain directories
            if item.name in ['scripts', 'patterns', 'SESSION_NOTES', '.git', '__pycache__',
                            'scripts.backup', '.aget', 'node_modules', '.venv', 'venv']:
                continue

            analysis = self.analyze_project(item)
            if analysis and analysis['is_git_repo']:
                self.results['projects'][item.name] = analysis
                self.update_summary(analysis)

        return self.results

    def update_summary(self, analysis: Dict):
        """Update summary statistics"""
        s = self.results['summary']
        s['total'] += 1

        if analysis['is_git_repo']:
            s['git_repos'] += 1
        if analysis['has_claude_md']:
            s['has_claude_md'] += 1
        if analysis['has_agents_md']:
            s['has_agents_md'] += 1
        if analysis['aget_version']:
            s['has_aget_version'] += 1

        status = analysis['migration_status']
        if status == 'fully_migrated':
            s['fully_migrated'] += 1
        elif status in ['partially_migrated', 'migrating']:
            s['partially_migrated'] += 1
        elif status in ['not_started', 'claude_compatible']:
            s['not_started'] += 1

    def print_report(self):
        """Print a formatted report of scan results"""
        print("\n" + "="*60)
        print("AGET Migration Status Report")
        print("="*60)
        print(f"Scan Date: {self.results['scan_date']}")
        print(f"Root Path: {self.results['root_path']}")
        print("\n" + "-"*60)
        print("SUMMARY")
        print("-"*60)

        s = self.results['summary']
        print(f"Total Git Repositories: {s['git_repos']}")
        print(f"├─ With CLAUDE.md: {s['has_claude_md']}")
        print(f"├─ With AGENTS.md: {s['has_agents_md']}")
        print(f"└─ With AGET version: {s['has_aget_version']}")
        print()
        print(f"Migration Status:")
        print(f"├─ Fully Migrated: {s['fully_migrated']}")
        print(f"├─ Partially Migrated: {s['partially_migrated']}")
        print(f"└─ Not Started: {s['not_started']}")

        print("\n" + "-"*60)
        print("PROJECT DETAILS")
        print("-"*60)

        # Sort projects by migration status
        projects_by_status = {}
        for name, proj in self.results['projects'].items():
            status = proj['migration_status']
            if status not in projects_by_status:
                projects_by_status[status] = []
            projects_by_status[status].append(proj)

        # Display by status groups
        status_order = ['fully_migrated', 'partially_migrated', 'migrating',
                       'claude_compatible', 'not_started', 'not_applicable']

        status_symbols = {
            'fully_migrated': '✅',
            'partially_migrated': '🔄',
            'migrating': '🔄',
            'claude_compatible': '📝',
            'not_started': '⏳',
            'not_applicable': '➖'
        }

        for status in status_order:
            if status in projects_by_status:
                print(f"\n{status_symbols.get(status, '?')} {status.replace('_', ' ').upper()}:")
                for proj in sorted(projects_by_status[status], key=lambda x: x['name']):
                    indicators = []
                    if proj['has_agents_md']:
                        indicators.append('AGENTS.md')
                    if proj['has_claude_md']:
                        indicators.append('CLAUDE.md')
                    if proj['has_patterns_dir']:
                        indicators.append('patterns/')
                    if proj['aget_version']:
                        indicators.append(f"v{proj['aget_version']}")

                    indicator_str = f" [{', '.join(indicators)}]" if indicators else ""
                    print(f"  • {proj['name']}{indicator_str}")

        print("\n" + "="*60)

    def save_report(self, filename: str = None):
        """Save scan results to file"""
        if not filename:
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            filename = f"aget_scan_{timestamp}.json"

        output_path = self.root / '.aget' / filename
        output_path.parent.mkdir(exist_ok=True)

        with open(output_path, 'w') as f:
            json.dump(self.results, f, indent=2)

        print(f"\nReport saved to: {output_path}")
        return output_path


def main():
    """Main entry point with argument parsing and error handling"""
    parser = argparse.ArgumentParser(
        description='Scan projects for AGET migration status',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Exit Codes:
  0 - All projects fully migrated
  1 - Partial migration (some projects migrated)
  2 - No migration started
  3 - Script execution error
        """
    )
    parser.add_argument('--quiet', '-q', action='store_true',
                        help='Minimal output (just summary)')
    parser.add_argument('--verbose', '-v', action='store_true',
                        help='Detailed output with debug info')
    parser.add_argument('--json', action='store_true',
                        help='Output in JSON format')
    parser.add_argument('--no-save', action='store_true',
                        help="Don't save report to .aget/project_scan.json")
    parser.add_argument('--exit-zero', action='store_true',
                        help='Always exit with 0 (for CI/CD compatibility)')

    args = parser.parse_args()

    try:
        scanner = ProjectScanner()

        # Set verbosity level
        if args.verbose:
            print(f"[DEBUG] Scanning root directory: {scanner.root}", file=sys.stderr)

        results = scanner.scan_all_projects()

        # Output based on format preference
        if args.json:
            print(json.dumps(results, indent=2))
        elif args.quiet:
            s = results['summary']
            print(f"Migration: {s['fully_migrated']}/{s['git_repos']} projects")
            if s['partially_migrated'] > 0:
                print(f"In progress: {s['partially_migrated']} projects")
        else:
            scanner.print_report()

        # Save report unless disabled
        if not args.no_save:
            scanner.save_report('project_scan.json')
        elif args.verbose:
            print("[DEBUG] Skipping report save (--no-save)", file=sys.stderr)

        # Determine exit code
        if args.exit_zero:
            return 0

        if results['summary']['git_repos'] == 0:
            return 2  # No repos found
        elif results['summary']['fully_migrated'] == results['summary']['git_repos']:
            return 0  # All migrated
        elif results['summary']['has_agents_md'] > 0:
            return 1  # Some migration
        else:
            return 2  # No migration

    except KeyboardInterrupt:
        print("\nInterrupted by user", file=sys.stderr)
        return 3
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        if args.verbose:
            import traceback
            traceback.print_exc(file=sys.stderr)
        return 3


if __name__ == "__main__":
    sys.exit(main())