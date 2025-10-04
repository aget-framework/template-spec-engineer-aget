#!/usr/bin/env python3
"""v2.5 Wake Protocol Contract Tests

Tests that wake protocol correctly reports agent identity, version, and capabilities.
Part of AGET framework v2.5 validation standards.
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
