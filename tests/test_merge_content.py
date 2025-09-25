"""
Tests for the merge_content module.
"""

import unittest
from pathlib import Path
from aget.config.commands.merge_content import ContentMerger


class TestContentMerger(unittest.TestCase):
    """Test the ContentMerger class for AGET migrations."""

    def setUp(self):
        """Set up test fixtures."""
        self.merger = ContentMerger()

    def test_extract_sections_basic(self):
        """Test extracting sections from markdown content."""
        content = """# Title
Some header content

## Section One
Content for section one

## Section Two
Content for section two
"""
        sections = self.merger.extract_sections(content)

        self.assertIn("HEADER", sections)
        self.assertIn("Section One", sections)
        self.assertIn("Section Two", sections)
        self.assertIn("Some header content", sections["HEADER"])

    def test_extract_sections_nested(self):
        """Test extracting nested sections."""
        content = """## Main Section
Main content

### Subsection
Subsection content

## Another Section
Another content
"""
        sections = self.merger.extract_sections(content)

        self.assertIn("Main Section", sections)
        self.assertIn("Subsection", sections)
        self.assertIn("Another Section", sections)

    def test_is_aget_section(self):
        """Test identifying AGET sections."""
        # AGET sections
        self.assertTrue(self.merger.is_aget_section("Session Management Protocols"))
        self.assertTrue(self.merger.is_aget_section("Housekeeping Protocols"))
        self.assertTrue(self.merger.is_aget_section("Directory Structure"))

        # Non-AGET sections
        self.assertFalse(self.merger.is_aget_section("Project Overview"))
        self.assertFalse(self.merger.is_aget_section("Custom Commands"))

    def test_is_preserved_section(self):
        """Test identifying preserved custom sections."""
        # Preserved sections
        self.assertTrue(self.merger.is_preserved_section("Project Overview"))
        self.assertTrue(self.merger.is_preserved_section("Custom Commands"))
        self.assertTrue(self.merger.is_preserved_section("Project-Specific Setup"))

        # Non-preserved sections
        self.assertFalse(self.merger.is_preserved_section("Random Section"))
        self.assertFalse(self.merger.is_preserved_section("Notes"))

    def test_merge_sections(self):
        """Test merging AGET and custom sections."""
        existing_sections = {
            "HEADER": "# My Project",
            "Project Overview": "## Project Overview\nMy custom project",
            "Session Management Protocols": "## Session Management Protocols\nOld protocols"
        }

        aget_sections = {
            "Session Management Protocols": "## Session Management Protocols\nNew AGET protocols",
            "Housekeeping Protocols": "## Housekeeping Protocols\nNew housekeeping"
        }

        merged = self.merger.merge_sections(existing_sections, aget_sections)

        # Custom sections preserved
        self.assertIn("Project Overview", merged)
        self.assertIn("My custom project", merged["Project Overview"])

        # AGET sections updated
        self.assertIn("Session Management Protocols", merged)
        self.assertIn("New AGET protocols", merged["Session Management Protocols"])

        # New AGET sections added
        self.assertIn("Housekeeping Protocols", merged)

    def test_merge_agents_files(self):
        """Test merging complete AGENTS.md files."""
        existing_content = """# Project Configuration

## Project Overview
This is my custom project with special requirements.

## Session Management Protocols
Old session protocols here.

## Custom Commands
My custom commands that should be preserved.
"""

        aget_template = """# AGET Configuration

## Session Management Protocols
New AGET session protocols.

## Housekeeping Protocols
AGET housekeeping protocols.
"""

        merged = self.merger.merge_agents_files(existing_content, aget_template)

        # Check merged content contains both custom and AGET sections
        self.assertIn("Project Overview", merged)
        self.assertIn("custom project with special requirements", merged)
        self.assertIn("Custom Commands", merged)
        self.assertIn("New AGET session protocols", merged)
        self.assertIn("AGET housekeeping protocols", merged)

    def test_format_merged_content(self):
        """Test formatting merged sections into final content."""
        sections = {
            "HEADER": "# My Project",
            "Project Overview": "## Project Overview\nCustom content",
            "Session Management Protocols": "## Session Management Protocols\nAGET protocols"
        }

        formatted = self.merger.format_merged_content(sections)

        # Check proper formatting
        self.assertTrue(formatted.startswith("# My Project"))
        self.assertIn("## Project Overview", formatted)
        self.assertIn("## Session Management Protocols", formatted)

        # Check section ordering (custom first, then AGET)
        overview_pos = formatted.index("Project Overview")
        session_pos = formatted.index("Session Management Protocols")
        self.assertLess(overview_pos, session_pos)

    def test_empty_content_handling(self):
        """Test handling of empty content."""
        sections = self.merger.extract_sections("")
        self.assertEqual(len(sections), 0)

        merged = self.merger.merge_sections({}, {})
        self.assertEqual(len(merged), 0)

    def test_section_preservation_priority(self):
        """Test that custom sections take priority over template sections."""
        existing_sections = {
            "Custom Setup": "## Custom Setup\nImportant custom setup"
        }

        aget_sections = {
            "Custom Setup": "## Custom Setup\nGeneric AGET setup",
            "New Section": "## New Section\nNew AGET content"
        }

        merged = self.merger.merge_sections(existing_sections, aget_sections)

        # Custom content preserved when section exists
        self.assertIn("Important custom setup", merged["Custom Setup"])
        self.assertNotIn("Generic AGET setup", merged["Custom Setup"])

        # New sections added
        self.assertIn("New Section", merged)


if __name__ == "__main__":
    unittest.main()