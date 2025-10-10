#!/usr/bin/env python3
"""v2.5/v2.6 Advisor Contract Tests

Tests that advisor agents maintain read-only boundaries and proper persona configuration.
Enforces hybrid enforcement model: declarations + automated validation.

v2.5.0: Global read-only (boolean values)
v2.6.0: Scoped write permissions (string "scoped" with write_scope section)

Part of AGET framework advisor template validation.
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
    """Advisor agents must declare read_only capability as true or 'scoped'."""
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

        read_only = capabilities["read_only"]
        # v2.5.0: boolean true, v2.6.0: string "scoped"
        assert read_only is True or read_only == "scoped", \
            f"Advisors must be read-only: advisory_capabilities.read_only must be true or 'scoped', got {read_only}"


def test_no_action_capabilities():
    """Advisor agents must not have unrestricted action capabilities."""
    version_file = Path(".aget/version.json")
    assert version_file.exists(), "version.json not found"

    with open(version_file) as f:
        data = json.load(f)

        assert "advisory_capabilities" in data, \
            "version.json missing advisory_capabilities section"

        capabilities = data["advisory_capabilities"]

        # can_execute must always be false (no scoped execution)
        if "can_execute" in capabilities:
            assert capabilities["can_execute"] is False, \
                f"Advisor cannot execute commands: can_execute must be false, got {capabilities['can_execute']}"

        # can_modify_files and can_create_files: false (v2.5.0) or "scoped" (v2.6.0)
        write_capabilities = ["can_modify_files", "can_create_files"]
        for cap in write_capabilities:
            if cap in capabilities:
                value = capabilities[cap]
                assert value is False or value == "scoped", \
                    f"Advisor {cap} must be false or 'scoped', got {value}"


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


# --- v2.6.0+ Scoped Write Permission Tests ---

def test_write_scope_declared_if_scoped():
    """Advisors with 'scoped' permissions must declare write_scope section (v2.6.0+)."""
    version_file = Path(".aget/version.json")
    assert version_file.exists(), "version.json not found"

    with open(version_file) as f:
        data = json.load(f)

        capabilities = data.get("advisory_capabilities", {})

        # Check if using scoped permissions
        read_only = capabilities.get("read_only")
        can_modify = capabilities.get("can_modify_files")
        can_create = capabilities.get("can_create_files")

        uses_scoped = (read_only == "scoped" or
                       can_modify == "scoped" or
                       can_create == "scoped")

        if uses_scoped:
            assert "write_scope" in capabilities, \
                "Advisors using 'scoped' permissions must declare write_scope section"

            write_scope = capabilities["write_scope"]
            assert isinstance(write_scope, dict), \
                "write_scope must be a dictionary"

            # Required fields
            assert "allowed_paths" in write_scope, \
                "write_scope missing allowed_paths"
            assert "forbidden_paths" in write_scope, \
                "write_scope missing forbidden_paths"


def test_write_scope_paths_valid():
    """Write scope allowed_paths must be internal (.aget/* only) (v2.6.0+)."""
    version_file = Path(".aget/version.json")
    assert version_file.exists(), "version.json not found"

    with open(version_file) as f:
        data = json.load(f)

        capabilities = data.get("advisory_capabilities", {})

        # Only check if write_scope exists
        if "write_scope" not in capabilities:
            pytest.skip("write_scope not declared (v2.5.0 agent)")

        write_scope = capabilities["write_scope"]
        allowed = write_scope.get("allowed_paths", [])

        assert isinstance(allowed, list), \
            "write_scope.allowed_paths must be a list"

        # All allowed paths must be internal (.aget/*)
        for path in allowed:
            assert path.startswith(".aget/"), \
                f"Allowed path '{path}' must be internal (.aget/* only) - external writes forbidden"


def test_scoped_write_maintains_external_readonly():
    """Scoped writes must explicitly forbid external file modification (v2.6.0+)."""
    version_file = Path(".aget/version.json")
    assert version_file.exists(), "version.json not found"

    with open(version_file) as f:
        data = json.load(f)

        capabilities = data.get("advisory_capabilities", {})

        # Only check if write_scope exists
        if "write_scope" not in capabilities:
            pytest.skip("write_scope not declared (v2.5.0 agent)")

        write_scope = capabilities["write_scope"]
        forbidden = write_scope.get("forbidden_paths", [])

        assert isinstance(forbidden, list), \
            "write_scope.forbidden_paths must be a list"

        # Critical external paths must be forbidden
        required_forbidden = ["AGENTS.md", "README.md", "version.json", "src/", "tests/"]

        # Check if wildcard (*) is present (forbids everything not explicitly allowed)
        has_wildcard = "*" in forbidden

        if not has_wildcard:
            # If no wildcard, must explicitly list critical paths
            for path in required_forbidden:
                assert path in forbidden, \
                    f"External path '{path}' must be in forbidden_paths (or use '*' wildcard)"
