#!/usr/bin/env python3
"""
Wind Down Protocol Pattern - Save work and end session gracefully.
"""

import json
import subprocess
from datetime import datetime
from pathlib import Path
from typing import Dict, Any, List


class WindDownProtocol:
    """Wind down protocol for ending agent sessions."""

    def __init__(self, project_path: Path = Path.cwd()):
        """Initialize wind down protocol."""
        self.project_path = Path(project_path)
        self.state_file = self.project_path / ".session_state.json"
        self.session_notes_dir = self.project_path / "SESSION_NOTES"

    def execute(self) -> Dict[str, Any]:
        """
        Execute wind down protocol.

        Returns:
            Status information about the session wrap-up
        """
        result = {
            'timestamp': datetime.now().isoformat(),
            'status': 'completed',
            'actions': []
        }

        print(f"{self._bold()}{self._blue()}## Wind Down - {datetime.now():%Y-%m-%d %H:%M}{self._reset()}")

        # Load session state
        state = self._load_state()
        session_duration = self._get_session_duration(state)
        print(f"⏱️ Session duration: {session_duration}")

        # 1. Check for uncommitted changes
        git_status = self._check_git_status()
        if git_status['has_changes']:
            commit_result = self._commit_changes(git_status['changes'])
            result['actions'].append(commit_result)
            if commit_result['success']:
                print(f"{self._green()}✓ Changes committed{self._reset()}")
            else:
                print(f"{self._yellow()}⚠ Could not commit: {commit_result.get('reason')}{self._reset()}")
        else:
            print(f"{self._green()}✓ No uncommitted changes{self._reset()}")
            result['actions'].append({'action': 'git_commit', 'success': True, 'reason': 'no changes'})

        # 2. Create session notes
        notes_result = self._create_session_notes(state)
        result['actions'].append(notes_result)
        if notes_result['success']:
            print(f"{self._green()}✓ Session notes created{self._reset()}")
        else:
            print(f"{self._yellow()}⚠ Could not create notes{self._reset()}")

        # 3. Run tests if available
        test_result = self._run_tests()
        result['actions'].append(test_result)
        if test_result['tests_found']:
            if test_result['success']:
                print(f"{self._green()}✓ Tests passed ({test_result['count']} files){self._reset()}")
            else:
                print(f"{self._yellow()}⚠ Some tests failed{self._reset()}")
        else:
            print("ℹ️ No tests found")

        # 4. Update session state
        state['last_wind_down'] = datetime.now().isoformat()
        state['current_session']['end_time'] = datetime.now().isoformat()
        state['current_session']['duration'] = session_duration
        self._save_state(state)

        # Final message
        print(f"{self._green()}✅ Session preserved.{self._reset()}")

        result['session_number'] = state.get('session_count', 0)
        result['duration'] = session_duration
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
            'current_session': {'start_time': datetime.now().isoformat()}
        }

    def _save_state(self, state: Dict[str, Any]):
        """Save session state to disk."""
        try:
            self.state_file.write_text(json.dumps(state, indent=2, default=str))
        except IOError:
            pass

    def _get_session_duration(self, state: Dict[str, Any]) -> str:
        """Calculate session duration."""
        if 'current_session' in state and 'start_time' in state['current_session']:
            start = datetime.fromisoformat(state['current_session']['start_time'])
            duration = datetime.now() - start
            hours = int(duration.seconds // 3600)
            minutes = int((duration.seconds % 3600) // 60)
            if hours > 0:
                return f"{hours}h {minutes}m"
            else:
                return f"{minutes}m"
        return "unknown"

    def _check_git_status(self) -> Dict[str, Any]:
        """Check for uncommitted changes."""
        try:
            result = subprocess.run(
                ['git', 'status', '--porcelain'],
                cwd=self.project_path,
                capture_output=True,
                text=True,
                timeout=2
            )

            if result.returncode != 0:
                return {'has_changes': False, 'is_repo': False}

            changes = result.stdout.strip()
            if changes:
                change_list = changes.split('\n')
                return {
                    'has_changes': True,
                    'is_repo': True,
                    'changes': change_list,
                    'count': len(change_list)
                }

            return {'has_changes': False, 'is_repo': True}

        except (subprocess.TimeoutExpired, FileNotFoundError):
            return {'has_changes': False, 'is_repo': False}

    def _commit_changes(self, changes: List[str]) -> Dict[str, Any]:
        """Commit uncommitted changes."""
        try:
            # Stage all changes
            subprocess.run(
                ['git', 'add', '-A'],
                cwd=self.project_path,
                capture_output=True,
                timeout=2
            )

            # Generate commit message
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
            message = f"session: Wind down at {timestamp}"

            # Commit
            result = subprocess.run(
                ['git', 'commit', '-m', message],
                cwd=self.project_path,
                capture_output=True,
                text=True,
                timeout=5
            )

            return {
                'action': 'git_commit',
                'success': result.returncode == 0,
                'message': message,
                'changes_count': len(changes)
            }

        except (subprocess.TimeoutExpired, subprocess.CalledProcessError) as e:
            return {
                'action': 'git_commit',
                'success': False,
                'reason': str(e)
            }

    def _create_session_notes(self, state: Dict[str, Any]) -> Dict[str, Any]:
        """Create session notes file."""
        try:
            # Create SESSION_NOTES directory if needed
            self.session_notes_dir.mkdir(exist_ok=True)

            # Create dated subdirectory
            date_dir = self.session_notes_dir / datetime.now().strftime("%Y-%m-%d")
            date_dir.mkdir(exist_ok=True)

            # Generate note filename
            session_num = state.get('session_count', 0)
            timestamp = datetime.now().strftime("%H%M")
            note_file = date_dir / f"session_{session_num:03d}_{timestamp}.md"

            # Create note content
            content = f"""# Session {session_num} Notes

**Date**: {datetime.now():%Y-%m-%d %H:%M}
**Duration**: {self._get_session_duration(state)}

## Activities
- Session completed

## Next Steps
- Continue from current state

---
*Auto-generated by wind down protocol*
"""

            note_file.write_text(content)

            return {
                'action': 'session_notes',
                'success': True,
                'file': str(note_file.relative_to(self.project_path))
            }

        except IOError as e:
            return {
                'action': 'session_notes',
                'success': False,
                'reason': str(e)
            }

    def _run_tests(self) -> Dict[str, Any]:
        """Run available tests."""
        # Look for test files
        test_patterns = ["test_*.py", "*_test.py"]
        test_files = []

        for pattern in test_patterns:
            test_files.extend(self.project_path.glob(pattern))

        tests_dir = self.project_path / "tests"
        if tests_dir.exists():
            test_files.extend(tests_dir.glob("*.py"))

        if not test_files:
            return {
                'action': 'run_tests',
                'tests_found': False
            }

        # Try to run pytest first, then unittest
        try:
            result = subprocess.run(
                ['python3', '-m', 'pytest', '-q'],
                cwd=self.project_path,
                capture_output=True,
                timeout=30
            )

            return {
                'action': 'run_tests',
                'tests_found': True,
                'success': result.returncode == 0,
                'count': len(test_files),
                'runner': 'pytest'
            }

        except (subprocess.TimeoutExpired, subprocess.CalledProcessError, FileNotFoundError):
            # Pytest not available, try unittest
            try:
                result = subprocess.run(
                    ['python3', '-m', 'unittest', 'discover', '-q'],
                    cwd=self.project_path,
                    capture_output=True,
                    timeout=30
                )

                return {
                    'action': 'run_tests',
                    'tests_found': True,
                    'success': result.returncode == 0,
                    'count': len(test_files),
                    'runner': 'unittest'
                }

            except:
                return {
                    'action': 'run_tests',
                    'tests_found': True,
                    'success': False,
                    'reason': 'No test runner available'
                }

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
    Apply wind down pattern to project.

    This is called by `aget apply session/wind_down`.
    """
    protocol = WindDownProtocol(project_path)
    return protocol.execute()


if __name__ == "__main__":
    # Execute wind down protocol
    apply_pattern()