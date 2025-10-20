#!/usr/bin/env python3
"""
Contract Tests: EARS Statement Generation (4 tests)

Validates EARS pattern formatting.
"""

import sys
import pytest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / '.aget' / 'tools'))

from extract_spec import Pattern


def test_ubiquitous_pattern_format():
    """Test 1: Ubiquitous EARS format = 'The SYSTEM shall...'."""
    pattern = Pattern(
        domain='test',
        action='validate input',
        frequency='always'
    )

    statement = pattern.to_ears_statement()

    assert statement.startswith('The SYSTEM shall'), \
        "Ubiquitous must start with 'The SYSTEM shall'"
    assert 'validate input' in statement
    assert pattern.classify_temporal_pattern() == 'ubiquitous'


def test_event_driven_pattern_format():
    """Test 2: Event-driven EARS format = 'WHEN [trigger], the SYSTEM shall...'."""
    pattern = Pattern(
        domain='test',
        action='process request',
        trigger='user submits command'
    )

    statement = pattern.to_ears_statement()

    assert statement.startswith('WHEN'), \
        "Event-driven must start with 'WHEN'"
    assert 'user submits command' in statement
    assert 'the SYSTEM shall process request' in statement
    assert pattern.classify_temporal_pattern() == 'event-driven'


def test_state_driven_pattern_format():
    """Test 3: State-driven EARS format = 'WHILE [state], the SYSTEM shall...'."""
    pattern = Pattern(
        domain='test',
        action='maintain session',
        state='session is active'
    )

    statement = pattern.to_ears_statement()

    assert statement.startswith('WHILE'), \
        "State-driven must start with 'WHILE'"
    assert 'session is active' in statement
    assert 'the SYSTEM shall maintain session' in statement
    assert pattern.classify_temporal_pattern() == 'state-driven'


def test_conditional_pattern_format():
    """Test 4: Conditional EARS format = 'IF [condition] THEN the SYSTEM shall...'."""
    pattern = Pattern(
        domain='test',
        action='reject input',
        condition='validation fails'
    )

    statement = pattern.to_ears_statement()

    assert statement.startswith('IF'), \
        "Conditional must start with 'IF'"
    assert 'validation fails' in statement
    assert 'THEN the SYSTEM shall reject input' in statement
    assert pattern.classify_temporal_pattern() == 'conditional'
