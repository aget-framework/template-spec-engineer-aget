"""
Tests for the validate command module.
"""

import unittest
from pathlib import Path
import tempfile
import shutil
from unittest.mock import Mock, patch, MagicMock

from aget.config.commands.validate import ValidateCommand


class TestValidateCommand(unittest.TestCase):
    """Test the ValidateCommand for AGET configuration validation."""

    def setUp(self):
        """Set up test fixtures."""
        self.validator = ValidateCommand()
        self.test_dir = Path(tempfile.mkdtemp())

    def tearDown(self):
        """Clean up test directory."""
        if self.test_dir.exists():
            shutil.rmtree(self.test_dir)

    def test_command_attributes(self):
        """Test that command has proper attributes."""
        self.assertEqual(self.validator.name, "validate")
        self.assertIn("configuration", self.validator.description.lower())

    @patch('aget.config.commands.validate.ProjectValidator')
    def test_tier_basic_default_path(self, mock_validator_class):
        """Test basic tier validation with default path."""
        mock_validator = Mock()
        mock_validator.validate.return_value = {
            'is_valid': True,
            'errors': [],
            'warnings': [],
            'info': ['All checks passed']
        }
        mock_validator_class.return_value = mock_validator

        result = self.validator.tier_basic()

        mock_validator_class.assert_called_once_with('.')
        mock_validator.validate.assert_called_once()
        self.assertEqual(result['status'], 'success')

    @patch('aget.config.commands.validate.ProjectValidator')
    def test_tier_basic_custom_path(self, mock_validator_class):
        """Test basic tier validation with custom path."""
        mock_validator = Mock()
        mock_validator.validate.return_value = {
            'is_valid': True,
            'errors': [],
            'warnings': [],
            'info': []
        }
        mock_validator_class.return_value = mock_validator

        result = self.validator.tier_basic(['custom/path'])

        mock_validator_class.assert_called_once_with('custom/path')
        self.assertEqual(result['status'], 'success')

    @patch('aget.config.commands.validate.ProjectValidator')
    def test_tier_basic_with_errors(self, mock_validator_class):
        """Test validation with errors."""
        mock_validator = Mock()
        mock_validator.validate.return_value = {
            'is_valid': False,
            'errors': ['AGENTS.md not found', 'Invalid pattern structure'],
            'warnings': [],
            'info': []
        }
        mock_validator_class.return_value = mock_validator

        result = self.validator.tier_basic()

        self.assertEqual(result['status'], 'error')
        self.assertIn('errors', result)
        self.assertEqual(len(result['errors']), 2)

    @patch('aget.config.commands.validate.ProjectValidator')
    def test_tier_basic_with_warnings(self, mock_validator_class):
        """Test validation with warnings."""
        mock_validator = Mock()
        mock_validator.validate.return_value = {
            'is_valid': True,
            'errors': [],
            'warnings': ['README.md missing', 'No tests found'],
            'info': []
        }
        mock_validator_class.return_value = mock_validator

        result = self.validator.tier_basic()

        self.assertEqual(result['status'], 'success')
        self.assertIn('warnings', result)
        self.assertEqual(len(result['warnings']), 2)

    @patch('aget.config.commands.validate.ProjectValidator')
    def test_tier_basic_strict_mode(self, mock_validator_class):
        """Test strict mode treats warnings as errors."""
        mock_validator = Mock()
        mock_validator.validate.return_value = {
            'is_valid': True,
            'errors': [],
            'warnings': ['Minor issue'],
            'info': []
        }
        mock_validator_class.return_value = mock_validator

        result = self.validator.tier_basic(['--strict'])

        # In strict mode, warnings should cause failure
        self.assertIn(result['status'], ['error', 'warning'])

    @patch('aget.config.commands.validate.ProjectValidator')
    def test_tier_basic_quiet_mode(self, mock_validator_class):
        """Test quiet mode suppresses info messages."""
        mock_validator = Mock()
        mock_validator.validate.return_value = {
            'is_valid': True,
            'errors': [],
            'warnings': [],
            'info': ['Info message 1', 'Info message 2']
        }
        mock_validator_class.return_value = mock_validator

        result = self.validator.tier_basic(['--quiet'])

        self.assertEqual(result['status'], 'success')
        # Quiet mode should not affect return structure, just output

    @patch('aget.config.commands.validate.ProjectValidator')
    def test_tier_git(self, mock_validator_class):
        """Test git tier validation."""
        mock_validator = Mock()
        mock_validator.validate.return_value = {
            'is_valid': True,
            'errors': [],
            'warnings': [],
            'info': []
        }
        mock_validator_class.return_value = mock_validator

        result = self.validator.tier_git()

        self.assertEqual(result['status'], 'success')

    @patch('aget.config.commands.validate.ProjectValidator')
    def test_tier_gh(self, mock_validator_class):
        """Test GitHub tier validation."""
        mock_validator = Mock()
        mock_validator.validate.return_value = {
            'is_valid': True,
            'errors': [],
            'warnings': [],
            'info': []
        }
        mock_validator_class.return_value = mock_validator

        result = self.validator.tier_gh()

        self.assertEqual(result['status'], 'success')

    @patch('aget.config.commands.validate.ProjectValidator')
    def test_execute_method(self, mock_validator_class):
        """Test the main execute method."""
        mock_validator = Mock()
        mock_validator.validate.return_value = {
            'is_valid': True,
            'errors': [],
            'warnings': [],
            'info': ['Validation successful']
        }
        mock_validator_class.return_value = mock_validator

        result = self.validator.execute([])

        self.assertEqual(result['status'], 'success')
        self.assertIn('elapsed', result)

    @patch('aget.config.commands.validate.ProjectValidator')
    def test_performance_tracking(self, mock_validator_class):
        """Test that performance is tracked."""
        mock_validator = Mock()
        mock_validator.validate.return_value = {
            'is_valid': True,
            'errors': [],
            'warnings': [],
            'info': []
        }
        mock_validator_class.return_value = mock_validator

        result = self.validator.tier_basic()

        self.assertIn('elapsed', result)
        self.assertIsInstance(result['elapsed'], float)
        self.assertGreaterEqual(result['elapsed'], 0)


if __name__ == "__main__":
    unittest.main()