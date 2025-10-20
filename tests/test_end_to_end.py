#!/usr/bin/env python3
"""
Contract Tests: End-to-End Workflows (3 tests)

Validates complete extraction workflows.
"""

import sys
import pytest
import yaml
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / '.aget' / 'tools'))

from extract_spec import SpecificationExtractor, Pattern


@pytest.fixture
def test_agent_path():
    """Get test agent path (private-github-aget)."""
    path = Path.home() / 'github' / 'private-github-aget'
    if not path.exists():
        pytest.skip("Test agent not available")
    return path


def test_extract_spec_from_valid_agent(test_agent_path, tmp_path):
    """Test 1: Complete extraction workflow produces valid spec."""
    extractor = SpecificationExtractor(test_agent_path)

    # Check readiness
    score, _ = extractor.check_readiness()
    assert score >= 6, "Test agent must be extractable"

    # Add sample patterns
    extractor.add_pattern(Pattern(
        domain='test_domain',
        action='test capability',
        frequency='always'
    ))

    # Generate spec
    spec = extractor.generate_spec()

    assert 'spec' in spec
    assert 'capabilities' in spec
    assert 'metadata' in spec

    # Save and verify YAML is valid
    output_file = tmp_path / 'test_spec.yaml'
    extractor.save_spec(output_file)

    assert output_file.exists()

    # Re-load to verify valid YAML
    with open(output_file) as f:
        loaded_spec = yaml.safe_load(f)

    assert loaded_spec == spec


def test_reject_low_scoring_agent(tmp_path):
    """Test 2: Low rubric score rejection."""
    # Create minimal directory (low score)
    low_score_agent = tmp_path / 'low_score_agent'
    low_score_agent.mkdir()

    extractor = SpecificationExtractor(low_score_agent)

    score, recommendation = extractor.check_readiness()

    # Should have very low score (no sessions, no evolution)
    assert score < 6, "Agent with no docs should score <6"
    assert 'NOT EXTRACTABLE' in recommendation or 'too low' in recommendation


def test_output_yaml_format_valid(test_agent_path, tmp_path):
    """Test 3: Generated YAML conforms to spec format v1.1."""
    extractor = SpecificationExtractor(test_agent_path)

    # Add patterns with different temporal types
    extractor.add_pattern(Pattern(
        domain='test1',
        action='ubiquitous test',
        frequency='always'
    ))

    extractor.add_pattern(Pattern(
        domain='test2',
        action='event test',
        trigger='event occurs'
    ))

    extractor.add_pattern(Pattern(
        domain='test3',
        action='state test',
        state='active state'
    ))

    spec = extractor.generate_spec()

    # Validate structure
    assert spec['spec']['format_version'] == '1.1'
    assert spec['spec']['maturity'] in ['bootstrapping', 'minimal', 'standard', 'exemplary']
    assert 'id' in spec['spec']
    assert 'version' in spec['spec']
    assert 'system_name' in spec['spec']

    # Validate capabilities
    for cap_id, capability in spec['capabilities'].items():
        assert cap_id.startswith('CAP-'), \
            f"Capability ID '{cap_id}' must start with 'CAP-'"

        assert 'domain' in capability
        assert 'statement' in capability
        assert 'pattern' in capability
        assert capability['pattern'] in [
            'ubiquitous', 'event-driven', 'state-driven', 'conditional', 'optional'
        ]

    # Validate metadata
    assert 'created' in spec['metadata']
    assert 'extraction_method' in spec['metadata']
    assert spec['metadata']['extraction_method'] == 'reverse_engineering'
