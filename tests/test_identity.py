#!/usr/bin/env python3
"""
Contract Tests: Identity Protocol (7 tests)

Validates template complies with v2.5.0+ advisor identity requirements.
"""

import json
import pytest
from pathlib import Path


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


def test_instance_type_is_aget(version_json):
    """Test 3: instance_type is 'aget' (read-only external, advisor)."""
    instance_type = version_json.get('instance_type')
    assert instance_type == 'aget', \
        "instance_type must be 'aget' for advisor agents"


def test_domain_is_specification_engineering(version_json):
    """Test 4: domain is 'specification-engineering'."""
    domain = version_json.get('domain')
    assert domain == 'specification-engineering', \
        "domain must be 'specification-engineering'"


def test_persona_is_consultant(version_json):
    """Test 5: persona is 'consultant'."""
    persona = version_json.get('persona')
    assert persona == 'consultant', \
        "persona must be 'consultant' (solutions focus, professional analysis)"


def test_aget_version_minimum_2_5(version_json):
    """Test 6: aget_version is 2.5.0 or higher."""
    version_str = version_json.get('aget_version', '0.0.0')

    # Parse version (handle 2.7.0 format)
    parts = version_str.split('.')
    major = int(parts[0])
    minor = int(parts[1]) if len(parts) > 1 else 0

    assert (major, minor) >= (2, 5), \
        f"aget_version '{version_str}' must be >= 2.5.0"


def test_advisory_capabilities_defined(version_json):
    """Test 7: advisory_capabilities structure exists."""
    advisory_caps = version_json.get('advisory_capabilities')
    assert advisory_caps is not None, \
        "advisory_capabilities must be defined"

    # Check required fields
    assert 'can_write_internal_state' in advisory_caps, \
        "advisory_capabilities must define can_write_internal_state"
    assert 'can_execute' in advisory_caps, \
        "advisory_capabilities must define can_execute"
    assert advisory_caps['can_execute'] is False, \
        "Advisor agents must have can_execute=False"
    assert 'write_scope' in advisory_caps, \
        "advisory_capabilities must define write_scope"
