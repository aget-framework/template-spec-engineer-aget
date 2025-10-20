#!/usr/bin/env python3
"""
Contract Tests: Pattern Extraction (6 tests)

Validates Pattern class and extraction logic.
"""

import sys
import pytest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / '.aget' / 'tools'))

from extract_spec import Pattern, SpecificationExtractor


def test_pattern_creation():
    """Test 1: Pattern objects can be created with required fields."""
    pattern = Pattern(
        domain='test_domain',
        action='test action',
        frequency='always'
    )

    assert pattern.domain == 'test_domain'
    assert pattern.action == 'test action'
    assert pattern.frequency == 'always'
    assert pattern.confidence == 1.0  # Default


def test_temporal_pattern_ubiquitous():
    """Test 2: Ubiquitous pattern classification (always + no trigger)."""
    pattern = Pattern(
        domain='test',
        action='do something',
        frequency='always'  # No trigger
    )

    assert pattern.classify_temporal_pattern() == 'ubiquitous'


def test_temporal_pattern_event_driven():
    """Test 3: Event-driven pattern classification (has trigger)."""
    pattern = Pattern(
        domain='test',
        action='respond to event',
        trigger='user command received'
    )

    assert pattern.classify_temporal_pattern() == 'event-driven'


def test_temporal_pattern_state_driven():
    """Test 4: State-driven pattern classification (has state)."""
    pattern = Pattern(
        domain='test',
        action='maintain consistency',
        state='session is active'
    )

    assert pattern.classify_temporal_pattern() == 'state-driven'


def test_temporal_pattern_conditional():
    """Test 5: Conditional pattern classification (has condition)."""
    pattern = Pattern(
        domain='test',
        action='perform validation',
        condition='input is valid'
    )

    assert pattern.classify_temporal_pattern() == 'conditional'


def test_temporal_pattern_optional_default():
    """Test 6: Optional pattern as conservative default."""
    pattern = Pattern(
        domain='test',
        action='optional feature',
        precondition='feature enabled'
    )

    assert pattern.classify_temporal_pattern() == 'optional'

    # Also optional when low confidence (no explicit precondition)
    pattern_low_conf = Pattern(
        domain='test',
        action='uncertain capability',
        confidence=0.4
    )

    # Low confidence patterns default to optional
    assert pattern_low_conf.classify_temporal_pattern() == 'optional'
