#!/usr/bin/env python3
"""v2.5 Advisor Contract Tests

Tests that advisor agents maintain read-only boundaries and proper persona configuration.
Enforces hybrid enforcement model: declarations + automated validation.
Part of AGET framework v2.5 advisor template validation.
"""

import pytest
import json
from pathlib import Path


def test_instance_type_is_aget():
    """Advisor agents must be read-only (instance_type == 'aget')."""
    version_file = Path(".aget/version.json")
    assert version_file.exists(), "version.json not found"

    with open(version_file) as f:
        data = json.load(f)
        assert "instance_type" in data, "version.json missing instance_type field"

        instance_type = data["instance_type"]
        assert instance_type == "aget", \
            f"Advisor agents must be read-only: instance_type must be 'aget', got '{instance_type}'"


def test_role_includes_advisor():
    """Advisor agents must include 'advisor' in roles array."""
    version_file = Path(".aget/version.json")
    assert version_file.exists(), "version.json not found"

    with open(version_file) as f:
        data = json.load(f)

        # Roles can be string or array, handle both
        if "roles" in data:
            roles = data["roles"]
            if isinstance(roles, str):
                roles = [roles]
            assert isinstance(roles, list), "roles must be a list or string"
            assert "advisor" in roles, \
                f"Advisor agents must include 'advisor' in roles, got: {roles}"


def test_persona_declared():
    """Advisor agents must declare a persona."""
    version_file = Path(".aget/version.json")
    assert version_file.exists(), "version.json not found"

    with open(version_file) as f:
        data = json.load(f)

        # Persona can be null in template, but field must exist
        assert "persona" in data, "version.json missing persona field"

        # If not null, must be string
        persona = data["persona"]
        if persona is not None:
            assert isinstance(persona, str), f"persona must be string or null, got {type(persona)}"


def test_advisory_capabilities_read_only():
    """Advisor agents must declare read_only capability as true."""
    version_file = Path(".aget/version.json")
    assert version_file.exists(), "version.json not found"

    with open(version_file) as f:
        data = json.load(f)

        assert "advisory_capabilities" in data, \
            "version.json missing advisory_capabilities section"

        capabilities = data["advisory_capabilities"]
        assert isinstance(capabilities, dict), \
            "advisory_capabilities must be a dictionary"

        assert "read_only" in capabilities, \
            "advisory_capabilities missing read_only field"

        assert capabilities["read_only"] is True, \
            f"Advisors must be read-only: advisory_capabilities.read_only must be true"


def test_no_action_capabilities():
    """Advisor agents must not have action capabilities enabled."""
    version_file = Path(".aget/version.json")
    assert version_file.exists(), "version.json not found"

    with open(version_file) as f:
        data = json.load(f)

        assert "advisory_capabilities" in data, \
            "version.json missing advisory_capabilities section"

        capabilities = data["advisory_capabilities"]

        # All action capabilities must be false
        action_capabilities = ["can_execute", "can_modify_files", "can_create_files"]
        for cap in action_capabilities:
            if cap in capabilities:
                assert capabilities[cap] is False, \
                    f"Advisor cannot have action capability: {cap} must be false, got {capabilities[cap]}"


def test_persona_is_valid():
    """If persona declared (not null), must be from allowed set."""
    version_file = Path(".aget/version.json")
    assert version_file.exists(), "version.json not found"

    with open(version_file) as f:
        data = json.load(f)

        # Get supported personas list
        assert "advisory_capabilities" in data, \
            "version.json missing advisory_capabilities section"

        capabilities = data["advisory_capabilities"]
        assert "supported_personas" in capabilities, \
            "advisory_capabilities missing supported_personas list"

        supported = capabilities["supported_personas"]
        assert isinstance(supported, list), "supported_personas must be a list"

        # Expected personas
        expected_personas = ["teacher", "mentor", "consultant", "guru", "coach"]
        assert set(supported) == set(expected_personas), \
            f"supported_personas must be {expected_personas}, got {supported}"

        # Check actual persona (if not null)
        if "persona" in data and data["persona"] is not None:
            persona = data["persona"]
            assert persona in supported, \
                f"persona '{persona}' not in supported_personas {supported}"


def test_supported_personas_list():
    """Advisory capabilities must list all 5 supported personas."""
    version_file = Path(".aget/version.json")
    assert version_file.exists(), "version.json not found"

    with open(version_file) as f:
        data = json.load(f)

        assert "advisory_capabilities" in data, \
            "version.json missing advisory_capabilities section"

        capabilities = data["advisory_capabilities"]
        assert "supported_personas" in capabilities, \
            "advisory_capabilities missing supported_personas field"

        supported = capabilities["supported_personas"]
        assert isinstance(supported, list), "supported_personas must be a list"
        assert len(supported) == 5, \
            f"Must support exactly 5 personas, got {len(supported)}: {supported}"

        # Verify all expected personas present
        expected = {"teacher", "mentor", "consultant", "guru", "coach"}
        actual = set(supported)
        assert actual == expected, \
            f"Missing personas: {expected - actual}, Unexpected: {actual - expected}"
