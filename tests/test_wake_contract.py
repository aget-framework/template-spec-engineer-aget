#!/usr/bin/env python3
"""v2.5 Wake Protocol Contract Tests - Advisor Template

Tests that wake protocol correctly reports agent identity, version, capabilities,
and advisor-specific information (advisory mode, persona).
Part of AGET framework v2.5 advisor template validation.
"""

import pytest
import json
from pathlib import Path


def test_wake_protocol_reports_agent_name():
    """Wake protocol must report agent name from version.json (if present)."""
    version_file = Path(".aget/version.json")
    assert version_file.exists(), "version.json not found"

    with open(version_file) as f:
        data = json.load(f)
        # agent_name optional in templates, required in instantiated agents
        if "agent_name" in data:
            agent_name = data["agent_name"]
            assert agent_name, "agent_name field is empty"
            assert isinstance(agent_name, str), "agent_name must be a string"


def test_wake_protocol_reports_version():
    """Wake protocol must report current AGET version."""
    version_file = Path(".aget/version.json")
    assert version_file.exists(), "version.json not found"

    with open(version_file) as f:
        data = json.load(f)
        assert "aget_version" in data, "version.json missing aget_version field"
        # Version format: X.Y.Z
        version = data["aget_version"]
        parts = version.split(".")
        assert len(parts) == 3, f"Version format invalid: {version} (expected X.Y.Z)"


def test_wake_protocol_reports_capabilities():
    """Wake protocol must report agent capabilities (if present)."""
    version_file = Path(".aget/version.json")
    assert version_file.exists(), "version.json not found"

    with open(version_file) as f:
        data = json.load(f)
        # Capabilities are optional in template, but if present, must be dict
        if "capabilities" in data:
            capabilities = data["capabilities"]
            assert isinstance(capabilities, dict), "capabilities must be a dictionary"


def test_wake_protocol_reports_domain():
    """Wake protocol must report agent domain for context (if present)."""
    version_file = Path(".aget/version.json")
    assert version_file.exists(), "version.json not found"

    with open(version_file) as f:
        data = json.load(f)
        # Domain is optional in template, but if present, must be string
        if "domain" in data:
            domain = data["domain"]
            assert isinstance(domain, str), "domain must be a string"
            assert domain, "domain field is empty"


# ============================================================================
# Advisor-Specific Wake Protocol Tests
# ============================================================================


def test_wake_displays_advisory_mode():
    """Wake protocol must indicate advisory mode for advisor agents."""
    version_file = Path(".aget/version.json")
    assert version_file.exists(), "version.json not found"

    with open(version_file) as f:
        data = json.load(f)

        # Verify this is an advisor agent
        assert "roles" in data, "version.json missing roles field"
        roles = data["roles"]
        if isinstance(roles, str):
            roles = [roles]

        # If roles includes "advisor", advisory mode must be indicated
        if "advisor" in roles:
            # Check advisory_capabilities section exists
            assert "advisory_capabilities" in data, \
                "Advisor agents must have advisory_capabilities section"

            # Verify read-only mode declared
            caps = data["advisory_capabilities"]
            assert caps.get("read_only") is True, \
                "Advisory mode requires read_only capability"

            # Note: Actual wake output validation would require running wake protocol
            # This test validates the configuration that wake protocol will display


def test_wake_displays_persona():
    """Wake protocol must display persona type for advisor agents."""
    version_file = Path(".aget/version.json")
    assert version_file.exists(), "version.json not found"

    with open(version_file) as f:
        data = json.load(f)

        # Check if roles includes advisor
        if "roles" in data:
            roles = data["roles"]
            if isinstance(roles, str):
                roles = [roles]

            # If advisor role, persona field must exist (can be null in template)
            if "advisor" in roles:
                assert "persona" in data, \
                    "Advisor agents must have persona field in version.json"

                # If persona is not null, verify it's displayable
                persona = data.get("persona")
                if persona is not None:
                    assert isinstance(persona, str), \
                        f"persona must be string if set, got {type(persona)}"
                    assert persona.strip(), \
                        "persona must not be empty string"

                    # Verify against supported personas
                    if "advisory_capabilities" in data:
                        caps = data["advisory_capabilities"]
                        if "supported_personas" in caps:
                            supported = caps["supported_personas"]
                            assert persona in supported, \
                                f"persona '{persona}' not in supported list: {supported}"
