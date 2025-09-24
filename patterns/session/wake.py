#!/usr/bin/env python3
"""
Wake Up Protocol Pattern - Start agent session with context.
"""

import json
import subprocess
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, Any, Optional


class WakeProtocol:
    """Wake up protocol for starting agent sessions."""

    def __init__(self, project_path: Path = Path.cwd()):
        """Initialize wake protocol."""
        self.project_path = Path(project_path)
        self.state_file = self.project_path / ".session_state.json"

    def execute(self) -> Dict[str, Any]:
        """
        Execute wake up protocol.

        Returns:
            Status information about the session
        """
        result = {
            'timestamp': datetime.now().isoformat(),
            'status': 'ready',
            'checks': {}
        }

        # Load session state
        state = self._load_state()
        session_number = state.get('session_count', 0) + 1

        # Calculate time since last session
        last_wake = state.get('last_wake')
        if last_wake:
            last_time = datetime.fromisoformat(last_wake)
            time_diff = datetime.now() - last_time
            result['last_session'] = self._format_timedelta(time_diff)
        else:
            result['last_session'] = 'First session'

        # Display wake message
        print(f"{self._bold()}{self._blue()}## Wake Up - {datetime.now():%Y-%m-%d %H:%M}{self._reset()}")
        print(f"📅 Last session: {result['last_session']}")
        print(f"🔢 Session #{session_number}")
        print(f"📍 {self.project_path}")

        # Check git status BEFORE updating state file
        git_status = self._check_git()

        # NOW update state for new session (after git check)
        state['last_wake'] = datetime.now().isoformat()
        state['session_count'] = session_number
        state['current_session'] = {
            'start_time': datetime.now().isoformat(),
            'tasks_completed': [],
            'files_modified': [],
            'tests_run': 0
        }
        self._save_state(state)
        result['checks']['git'] = git_status
        if git_status['clean']:
            print(f"{self._green()}✓ Git repository clean{self._reset()}")
        else:
            print(f"{self._yellow()}⚠ Git has uncommitted changes{self._reset()}")

        # Check for patterns
        patterns = self._check_patterns()
        result['checks']['patterns'] = patterns
        if patterns:
            print(f"📦 Patterns available: {', '.join(patterns)}")

        # Check for templates
        templates = self._check_templates()
        result['checks']['templates'] = templates
        if templates:
            print(f"📄 Templates: {', '.join(templates)}")

        # Check tests
        test_count = self._check_tests()
        result['checks']['tests'] = test_count
        if test_count > 0:
            print(f"🧪 Tests: {test_count} test files found")

        # Final status
        print(f"{self._green()}✅ Ready for tasks.{self._reset()}")

        result['session_number'] = session_number
        return result

    def _load_state(self) -> Dict[str, Any]:
        """Load session state from disk."""
        if self.state_file.exists():
            try:
                return json.loads(self.state_file.read_text())
            except (json.JSONDecodeError, IOError):
                pass
        return {
            'session_count': 0,
            'last_wake': None,
            'last_wind_down': None
        }

    def _save_state(self, state: Dict[str, Any]):
        """Save session state to disk."""
        try:
            self.state_file.write_text(json.dumps(state, indent=2, default=str))
        except IOError:
            pass  # Silently fail if can't save state

    def _check_git(self) -> Dict[str, Any]:
        """Check git repository status."""
        try:
            # Check if it's a git repo
            result = subprocess.run(
                ['git', 'rev-parse', '--git-dir'],
                cwd=self.project_path,
                capture_output=True,
                timeout=1
            )

            if result.returncode != 0:
                return {'is_repo': False, 'clean': False}

            # Check for uncommitted changes
            result = subprocess.run(
                ['git', 'status', '--porcelain'],
                cwd=self.project_path,
                capture_output=True,
                text=True,
                timeout=1
            )

            changes = result.stdout.strip()
            return {
                'is_repo': True,
                'clean': len(changes) == 0,
                'changes': changes.split('\n') if changes else []
            }

        except (subprocess.TimeoutExpired, FileNotFoundError):
            return {'is_repo': False, 'clean': False}

    def _check_patterns(self) -> list:
        """Check available patterns."""
        patterns_dir = self.project_path / "patterns"
        if not patterns_dir.exists():
            return []

        pattern_categories = []
        for category_dir in patterns_dir.iterdir():
            if category_dir.is_dir() and not category_dir.name.startswith('.'):
                pattern_categories.append(category_dir.name)

        return sorted(pattern_categories)

    def _check_templates(self) -> list:
        """Check available templates."""
        templates = []

        # Check for template types based on AGENTS.md content
        agents_file = self.project_path / "AGENTS.md"
        if agents_file.exists():
            content = agents_file.read_text()
            if "wake up" in content.lower():
                templates.append("standard")
            if "minimal" in content.lower():
                templates.append("minimal")
            if "advanced" in content.lower():
                templates.append("advanced")

        if not templates:
            templates = ["minimal", "standard", "advanced"]

        return templates

    def _check_tests(self) -> int:
        """Count test files."""
        test_patterns = ["test_*.py", "*_test.py", "tests/*.py"]
        test_count = 0

        for pattern in test_patterns:
            test_count += len(list(self.project_path.glob(pattern)))

        tests_dir = self.project_path / "tests"
        if tests_dir.exists():
            test_count += len(list(tests_dir.glob("*.py")))

        return test_count

    def _format_timedelta(self, td: timedelta) -> str:
        """Format timedelta in human-readable form."""
        if td.days > 0:
            return f"{td.days} days ago"
        elif td.seconds > 3600:
            hours = td.seconds // 3600
            return f"{hours} hours ago"
        elif td.seconds > 60:
            minutes = td.seconds // 60
            return f"{minutes} minutes ago"
        else:
            return "Just now"

    # ANSI color helpers
    def _blue(self) -> str:
        return '\033[94m'

    def _green(self) -> str:
        return '\033[92m'

    def _yellow(self) -> str:
        return '\033[93m'

    def _bold(self) -> str:
        return '\033[1m'

    def _reset(self) -> str:
        return '\033[0m'


def apply_pattern(project_path: Path = Path.cwd()) -> Dict[str, Any]:
    """
    Apply wake pattern to project.

    This is called by `aget apply session/wake`.
    """
    protocol = WakeProtocol(project_path)
    return protocol.execute()


if __name__ == "__main__":
    # Execute wake protocol
    apply_pattern()