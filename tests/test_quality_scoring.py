#!/usr/bin/env python3
"""
Contract Tests: Quality Scoring (3 tests)

Validates quality assessment logic.
"""

import sys
import pytest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / '.aget' / 'tools'))

from extract_spec import SpecificationExtractor, Pattern


def test_completeness_scoring():
    """Test 1: Completeness reflects capability coverage."""
    # Create temporary extractor (use existing agent for simplicity)
    agent_path = Path.home() / 'github' / 'private-github-aget'

    if not agent_path.exists():
        pytest.skip("Test agent not available")

    extractor = SpecificationExtractor(agent_path)

    # Add some patterns
    extractor.add_pattern(Pattern(domain='test', action='test1'))
    extractor.add_pattern(Pattern(domain='test', action='test2'))

    quality = extractor.calculate_quality_scores()

    assert 'completeness' in quality
    assert 0 <= quality['completeness'] <= 100, \
        "Completeness must be 0-100%"


def test_accuracy_validation():
    """Test 2: Accuracy reflects high-confidence pattern percentage."""
    agent_path = Path.home() / 'github' / 'private-github-aget'

    if not agent_path.exists():
        pytest.skip("Test agent not available")

    extractor = SpecificationExtractor(agent_path)

    # Add high confidence patterns
    extractor.add_pattern(Pattern(domain='test', action='test1', confidence=0.9))
    extractor.add_pattern(Pattern(domain='test', action='test2', confidence=0.85))
    # Add low confidence pattern
    extractor.add_pattern(Pattern(domain='test', action='test3', confidence=0.5))

    quality = extractor.calculate_quality_scores()

    assert 'accuracy' in quality
    assert 0 <= quality['accuracy'] <= 100
    # Should be ~67% (2/3 high confidence)
    assert 60 <= quality['accuracy'] <= 75


def test_overall_quality_calculation():
    """Test 3: Overall quality is weighted average."""
    agent_path = Path.home() / 'github' / 'private-github-aget'

    if not agent_path.exists():
        pytest.skip("Test agent not available")

    extractor = SpecificationExtractor(agent_path)

    # Add patterns
    extractor.add_pattern(Pattern(domain='test', action='test1', confidence=0.9))

    quality = extractor.calculate_quality_scores()

    assert 'overall' in quality
    assert 0 <= quality['overall'] <= 100

    # Overall should be weighted: completeness*0.5 + accuracy*0.3 + clarity*0.2
    expected = (quality['completeness'] * 0.5 +
                quality['accuracy'] * 0.3 +
                quality['clarity'] * 0.2)

    assert abs(quality['overall'] - expected) < 0.1, \
        "Overall should be weighted average"
