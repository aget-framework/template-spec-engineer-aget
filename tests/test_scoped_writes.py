#!/usr/bin/env python3
"""
Contract Tests: Scoped Write Permissions (5 tests)

Validates advisor agents can only write to .aget/** directories.

v3.0.0-beta: Added skip for v3.0 templates (write_scope configured at instantiation)
"""

import json
import pytest
from pathlib import Path
from conftest import is_template_context


# Skip reason for v2.x-specific tests
SKIP_TEMPLATE_V2 = pytest.mark.skipif(
    is_template_context(),
    reason="v2.x instance test: v3.0 templates configure write_scope at instantiation"
)


@pytest.fixture
def version_json():
    """Load .aget/version.json for testing."""
    version_file = Path(__file__).parent.parent / '.aget' / 'version.json'
    with open(version_file) as f:
        return json.load(f)


@SKIP_TEMPLATE_V2
def test_can_write_to_aget_sessions(version_json):
    """Test 1: Can write to .aget/sessions/** (v2.x instances only)."""
    write_scope = version_json['advisory_capabilities']['write_scope']
    allowed = write_scope.get('allowed_paths', [])

    assert any('.aget/sessions' in path for path in allowed), \
        ".aget/sessions/** must be in allowed_paths"


@SKIP_TEMPLATE_V2
def test_can_write_to_client_progress(version_json):
    """Test 2: Can write to .aget/client_progress/** (v2.x instances only)."""
    write_scope = version_json['advisory_capabilities']['write_scope']
    allowed = write_scope.get('allowed_paths', [])

    assert any('.aget/client_progress' in path for path in allowed), \
        ".aget/client_progress/** must be in allowed_paths"


@SKIP_TEMPLATE_V2
def test_cannot_write_to_src(version_json):
    """Test 3: Cannot write to src/ (external code) (v2.x instances only)."""
    write_scope = version_json['advisory_capabilities']['write_scope']
    forbidden = write_scope.get('forbidden_paths', [])

    assert 'src/' in forbidden, \
        "src/ must be in forbidden_paths"


@SKIP_TEMPLATE_V2
def test_cannot_write_to_agents_md(version_json):
    """Test 4: Cannot write to AGENTS.md (configuration) (v2.x instances only)."""
    write_scope = version_json['advisory_capabilities']['write_scope']
    forbidden = write_scope.get('forbidden_paths', [])

    assert 'AGENTS.md' in forbidden, \
        "AGENTS.md must be in forbidden_paths"


@SKIP_TEMPLATE_V2
def test_write_scope_enforcement_strict(version_json):
    """Test 5: Write scope enforcement is 'strict' (v2.x instances only)."""
    write_scope = version_json['advisory_capabilities']['write_scope']
    enforcement = write_scope.get('enforcement')

    assert enforcement == 'strict', \
        "enforcement must be 'strict' for advisor agents"
