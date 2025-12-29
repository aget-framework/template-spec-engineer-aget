#!/usr/bin/env python3
"""
Contract Tests: Identity Protocol (7 tests)

Validates template complies with v2.5.0+/v3.0+ identity requirements.

v3.0.0-beta: Added v3.0 schema compatibility for templates
"""

import json
import pytest
from pathlib import Path
from conftest import is_template_context


# Skip reason for v2.x-specific tests
SKIP_TEMPLATE_V2 = pytest.mark.skipif(
    is_template_context(),
    reason="v2.x instance test: v3.0 templates use template field instead of persona"
)


# Test fixture: Load version.json
@pytest.fixture
def version_json():
    """Load .aget/version.json for testing."""
    version_file = Path(__file__).parent.parent / '.aget' / 'version.json'
    with open(version_file) as f:
        return json.load(f)


@pytest.fixture
def template_root():
    """Get template root directory."""
    return Path(__file__).parent.parent


def test_version_json_exists(template_root):
    """Test 1: version.json file exists."""
    version_file = template_root / '.aget' / 'version.json'
    assert version_file.exists(), ".aget/version.json must exist"


def test_agent_name_matches_directory(version_json, template_root):
    """Test 2: agent_name matches directory name."""
    expected_name = template_root.name
    actual_name = version_json.get('agent_name')
    assert actual_name == expected_name, \
        f"agent_name '{actual_name}' must match directory '{expected_name}'"


def test_instance_type_valid(version_json):
    """Test 3: instance_type valid for version.

    v2.x: instance_type == 'aget'
    v3.0: instance_type == 'template' with template field
    """
    instance_type = version_json.get('instance_type')
    manifest_version = version_json.get('manifest_version', '2.0')

    if manifest_version.startswith('3.'):
        assert instance_type == 'template', \
            "v3.0 templates must have instance_type='template'"
        assert 'template' in version_json, \
            "v3.0 templates must have 'template' field"
    else:
        assert instance_type == 'aget', \
            "v2.x agents must have instance_type='aget'"


def test_domain_is_specification_engineering(version_json):
    """Test 4: domain is 'specification-engineering'."""
    domain = version_json.get('domain')
    assert domain == 'specification-engineering', \
        "domain must be 'specification-engineering'"


def test_persona_or_template_valid(version_json):
    """Test 5: persona (v2.x) or template (v3.0) is valid.

    v2.x: persona == 'consultant'
    v3.0: template == 'spec_engineer'
    """
    manifest_version = version_json.get('manifest_version', '2.0')

    if manifest_version.startswith('3.'):
        template = version_json.get('template')
        assert template == 'spec_engineer', \
            f"v3.0 spec-engineer template must have template='spec_engineer', got '{template}'"
    else:
        persona = version_json.get('persona')
        assert persona == 'consultant', \
            "v2.x persona must be 'consultant'"


def test_aget_version_minimum_2_5(version_json):
    """Test 6: aget_version is 2.5.0 or higher."""
    version_str = version_json.get('aget_version', '0.0.0')

    # Parse version (handle 2.7.0 format)
    parts = version_str.split('.')
    major = int(parts[0])
    minor = int(parts[1]) if len(parts) > 1 else 0

    assert (major, minor) >= (2, 5), \
        f"aget_version '{version_str}' must be >= 2.5.0"


def test_capabilities_defined(version_json):
    """Test 7: capabilities structure exists.

    v2.x: advisory_capabilities dict with can_execute, write_scope
    v3.0: capabilities list with capability strings
    """
    manifest_version = version_json.get('manifest_version', '2.0')

    if manifest_version.startswith('3.'):
        # v3.0 uses capabilities list
        capabilities = version_json.get('capabilities')
        assert capabilities is not None, \
            "v3.0 templates must have 'capabilities' list"
        assert isinstance(capabilities, list), \
            "v3.0 capabilities must be a list"
        assert len(capabilities) > 0, \
            "v3.0 capabilities list should not be empty"
    else:
        # v2.x uses advisory_capabilities dict
        advisory_caps = version_json.get('advisory_capabilities')
        assert advisory_caps is not None, \
            "advisory_capabilities must be defined"

        assert 'can_write_internal_state' in advisory_caps, \
            "advisory_capabilities must define can_write_internal_state"
        assert 'can_execute' in advisory_caps, \
            "advisory_capabilities must define can_execute"
        assert advisory_caps['can_execute'] is False, \
            "Advisor agents must have can_execute=False"
        assert 'write_scope' in advisory_caps, \
            "advisory_capabilities must define write_scope"
