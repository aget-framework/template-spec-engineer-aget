#!/usr/bin/env python3
"""
Contract Tests: Scoped Write Permissions (5 tests)

Validates advisor agents can only write to .aget/** directories.
"""

import json
import pytest
from pathlib import Path


@pytest.fixture
def version_json():
    """Load .aget/version.json for testing."""
    version_file = Path(__file__).parent.parent / '.aget' / 'version.json'
    with open(version_file) as f:
        return json.load(f)


def test_can_write_to_aget_sessions(version_json):
    """Test 1: Can write to .aget/sessions/**."""
    write_scope = version_json['advisory_capabilities']['write_scope']
    allowed = write_scope.get('allowed_paths', [])

    assert any('.aget/sessions' in path for path in allowed), \
        ".aget/sessions/** must be in allowed_paths"


def test_can_write_to_client_progress(version_json):
    """Test 2: Can write to .aget/client_progress/**."""
    write_scope = version_json['advisory_capabilities']['write_scope']
    allowed = write_scope.get('allowed_paths', [])

    assert any('.aget/client_progress' in path for path in allowed), \
        ".aget/client_progress/** must be in allowed_paths"


def test_cannot_write_to_src(version_json):
    """Test 3: Cannot write to src/ (external code)."""
    write_scope = version_json['advisory_capabilities']['write_scope']
    forbidden = write_scope.get('forbidden_paths', [])

    assert 'src/' in forbidden, \
        "src/ must be in forbidden_paths"


def test_cannot_write_to_agents_md(version_json):
    """Test 4: Cannot write to AGENTS.md (configuration)."""
    write_scope = version_json['advisory_capabilities']['write_scope']
    forbidden = write_scope.get('forbidden_paths', [])

    assert 'AGENTS.md' in forbidden, \
        "AGENTS.md must be in forbidden_paths"


def test_write_scope_enforcement_strict(version_json):
    """Test 5: Write scope enforcement is 'strict'."""
    write_scope = version_json['advisory_capabilities']['write_scope']
    enforcement = write_scope.get('enforcement')

    assert enforcement == 'strict', \
        "enforcement must be 'strict' for advisor agents"
