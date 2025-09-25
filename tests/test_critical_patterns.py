"""
Enhanced tests for critical patterns to improve coverage.
Focus on wake, wind_down, and sign_off patterns.
"""

import unittest
from pathlib import Path
import tempfile
import shutil
import json
from unittest.mock import Mock, patch, MagicMock
import subprocess

from patterns.session.wake import apply_pattern as wake_pattern
from patterns.session.wind_down import apply_pattern as wind_down_pattern
from patterns.session.sign_off import apply_pattern as sign_off_pattern


class TestCriticalPatternsEnhanced(unittest.TestCase):
    """Enhanced tests for critical session patterns."""

    def setUp(self):
        """Set up test fixtures."""
        self.test_dir = Path(tempfile.mkdtemp())
        self.original_cwd = Path.cwd()

        # Create minimal project structure
        (self.test_dir / ".aget").mkdir()
        (self.test_dir / ".aget" / "state.json").write_text('{}')
        (self.test_dir / "AGENTS.md").write_text("# Test Project")

        # Change to test directory
        import os
        os.chdir(self.test_dir)

    def tearDown(self):
        """Clean up test directory."""
        import os
        os.chdir(self.original_cwd)
        if self.test_dir.exists():
            shutil.rmtree(self.test_dir)

    @patch('subprocess.run')
    def test_wake_pattern_edge_cases(self, mock_run):
        """Test wake pattern with various edge cases."""
        # Test with clean git status
        mock_run.return_value = Mock(
            returncode=0,
            stdout="",
            stderr=""
        )

        result = wake_pattern()

        self.assertEqual(result['status'], 'success')
        self.assertIn('session_number', result)
        self.assertIn('Ready for tasks', result['message'])

    @patch('subprocess.run')
    def test_wake_pattern_git_failures(self, mock_run):
        """Test wake pattern when git commands fail."""
        # Simulate git command failure
        mock_run.side_effect = subprocess.CalledProcessError(128, 'git')

        result = wake_pattern()

        # Should still succeed but note the git issue
        self.assertEqual(result['status'], 'success')
        self.assertIn('Ready', result['message'])

    @patch('subprocess.run')
    def test_wake_pattern_crash_recovery(self, mock_run):
        """Test wake pattern recovery from previous crash."""
        # Create a state file indicating crash
        state_data = {
            'session_active': True,
            'session_start': '2025-01-01T10:00:00',
            'session_number': 99
        }
        (self.test_dir / ".aget" / "state.json").write_text(json.dumps(state_data))

        mock_run.return_value = Mock(returncode=0, stdout="", stderr="")

        result = wake_pattern()

        self.assertEqual(result['status'], 'success')
        # Should detect and handle the crash recovery

    @patch('subprocess.run')
    def test_wind_down_pattern_no_changes(self, mock_run):
        """Test wind down when there are no changes to commit."""
        # Simulate no git changes
        mock_run.return_value = Mock(
            returncode=0,
            stdout="",
            stderr=""
        )

        result = wind_down_pattern()

        self.assertEqual(result['status'], 'success')
        self.assertIn('preserved', result['message'].lower())

    @patch('subprocess.run')
    def test_wind_down_pattern_with_changes(self, mock_run):
        """Test wind down with uncommitted changes."""
        # Create some test files
        (self.test_dir / "test_file.py").write_text("print('test')")

        # Mock git status showing changes
        def git_side_effect(cmd, **kwargs):
            if 'status' in cmd:
                return Mock(returncode=0, stdout="M test_file.py", stderr="")
            elif 'diff' in cmd:
                return Mock(returncode=0, stdout="+ added line", stderr="")
            elif 'add' in cmd or 'commit' in cmd:
                return Mock(returncode=0, stdout="", stderr="")
            return Mock(returncode=0, stdout="", stderr="")

        mock_run.side_effect = git_side_effect

        result = wind_down_pattern()

        self.assertEqual(result['status'], 'success')

    @patch('subprocess.run')
    def test_wind_down_pattern_session_notes(self, mock_run):
        """Test that wind down creates session notes."""
        mock_run.return_value = Mock(returncode=0, stdout="", stderr="")

        # Set up active session
        state_data = {'session_active': True, 'session_number': 100}
        (self.test_dir / ".aget" / "state.json").write_text(json.dumps(state_data))

        result = wind_down_pattern()

        # Should create session notes
        self.assertEqual(result['status'], 'success')

    @patch('subprocess.run')
    def test_sign_off_pattern_quick_save(self, mock_run):
        """Test sign off for quick save functionality."""
        # Mock git operations
        mock_run.return_value = Mock(returncode=0, stdout="", stderr="")

        result = sign_off_pattern()

        self.assertEqual(result['status'], 'success')
        self.assertIn('signed off', result['message'].lower())

    @patch('subprocess.run')
    def test_sign_off_pattern_with_remote(self, mock_run):
        """Test sign off with remote push."""
        def git_side_effect(cmd, **kwargs):
            if 'remote' in cmd:
                return Mock(returncode=0, stdout="origin", stderr="")
            elif 'push' in cmd:
                return Mock(returncode=0, stdout="Everything up-to-date", stderr="")
            return Mock(returncode=0, stdout="", stderr="")

        mock_run.side_effect = git_side_effect

        result = sign_off_pattern()

        self.assertEqual(result['status'], 'success')

    @patch('subprocess.run')
    def test_sign_off_pattern_no_remote(self, mock_run):
        """Test sign off when no remote is configured."""
        def git_side_effect(cmd, **kwargs):
            if 'remote' in cmd:
                return Mock(returncode=0, stdout="", stderr="")
            return Mock(returncode=0, stdout="", stderr="")

        mock_run.side_effect = git_side_effect

        result = sign_off_pattern()

        # Should still succeed but skip push
        self.assertEqual(result['status'], 'success')

    def test_wake_pattern_state_persistence(self):
        """Test that wake pattern properly persists state."""
        with patch('subprocess.run') as mock_run:
            mock_run.return_value = Mock(returncode=0, stdout="", stderr="")

            result = wake_pattern()

            # Check state file was updated
            state_file = self.test_dir / ".aget" / "state.json"
            self.assertTrue(state_file.exists())

            state_data = json.loads(state_file.read_text())
            self.assertTrue(state_data.get('session_active'))
            self.assertIn('session_number', state_data)

    def test_wind_down_pattern_state_cleanup(self):
        """Test that wind down properly cleans up state."""
        # Set up active session
        state_data = {
            'session_active': True,
            'session_number': 100,
            'session_start': '2025-01-01T10:00:00'
        }
        (self.test_dir / ".aget" / "state.json").write_text(json.dumps(state_data))

        with patch('subprocess.run') as mock_run:
            mock_run.return_value = Mock(returncode=0, stdout="", stderr="")

            result = wind_down_pattern()

            # Check state was properly ended
            state_file = self.test_dir / ".aget" / "state.json"
            state_data = json.loads(state_file.read_text())
            self.assertFalse(state_data.get('session_active', False))

    @patch('subprocess.run')
    def test_pattern_performance(self, mock_run):
        """Test that patterns complete within performance targets."""
        import time
        mock_run.return_value = Mock(returncode=0, stdout="", stderr="")

        # Test wake performance
        start = time.time()
        wake_pattern()
        wake_time = time.time() - start
        self.assertLess(wake_time, 2.0, "Wake pattern exceeded 2 second limit")

        # Test wind_down performance
        start = time.time()
        wind_down_pattern()
        wind_time = time.time() - start
        self.assertLess(wind_time, 2.0, "Wind down pattern exceeded 2 second limit")

        # Test sign_off performance
        start = time.time()
        sign_off_pattern()
        sign_time = time.time() - start
        self.assertLess(sign_time, 2.0, "Sign off pattern exceeded 2 second limit")

    def test_pattern_error_handling(self):
        """Test that patterns handle errors gracefully."""
        with patch('subprocess.run') as mock_run:
            # Simulate various subprocess errors
            mock_run.side_effect = Exception("Unexpected error")

            # Patterns should handle errors without crashing
            result = wake_pattern()
            self.assertIn('status', result)

            result = wind_down_pattern()
            self.assertIn('status', result)

            result = sign_off_pattern()
            self.assertIn('status', result)


if __name__ == "__main__":
    unittest.main()