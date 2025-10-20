#!/usr/bin/env python3
"""
Contract Tests: Rubric Scoring (4 tests)

Validates assess_agent.py rubric assessment logic.
"""

import sys
import pytest
from pathlib import Path

# Add tools to path
sys.path.insert(0, str(Path(__file__).parent.parent / '.aget' / 'tools'))

from assess_agent import RubricAssessment


def test_rubric_scores_range_0_to_3():
    """Test 1: Rubric scores must be 0-3."""
    assessment = RubricAssessment(Path('/tmp/test'))

    # Valid scores
    assessment.assess_category('conversation_traceability', 0)
    assessment.assess_category('feature_observability', 1)
    assessment.assess_category('decision_documentation', 2)
    assessment.assess_category('pattern_clarity', 3)
    assessment.assess_category('constraint_discovery', 2)
    assessment.assess_category('quality_attributes', 1)

    # Invalid scores should raise
    with pytest.raises(ValueError):
        assessment.assess_category('conversation_traceability', 4)

    with pytest.raises(ValueError):
        assessment.assess_category('conversation_traceability', -1)


def test_weighted_total_calculation():
    """Test 2: Weighted total calculated correctly."""
    assessment = RubricAssessment(Path('/tmp/test'))

    # All 3s = 18 total, 100% weighted
    assessment.assess_category('conversation_traceability', 3)
    assessment.assess_category('feature_observability', 3)
    assessment.assess_category('decision_documentation', 3)
    assessment.assess_category('pattern_clarity', 3)
    assessment.assess_category('constraint_discovery', 3)
    assessment.assess_category('quality_attributes', 3)

    total, weighted = assessment.calculate_total()

    assert total == 18, "Total should be 18 for all 3s"
    assert weighted == pytest.approx(100.0), "Weighted should be 100% for all 3s"


def test_recommendation_thresholds():
    """Test 3: Recommendation levels at correct thresholds."""
    # Highly extractable (15-18)
    assessment_high = RubricAssessment(Path('/tmp/test'))
    assessment_high.assess_category('conversation_traceability', 3)
    assessment_high.assess_category('feature_observability', 3)
    assessment_high.assess_category('decision_documentation', 3)
    assessment_high.assess_category('pattern_clarity', 2)
    assessment_high.assess_category('constraint_discovery', 2)
    assessment_high.assess_category('quality_attributes', 2)
    assessment_high.calculate_total()

    rec = assessment_high.get_recommendation()
    assert rec['level'] == 'highly_extractable', \
        "Score 15 should be highly_extractable"

    # Moderately extractable (11-14)
    assessment_mod = RubricAssessment(Path('/tmp/test'))
    assessment_mod.assess_category('conversation_traceability', 2)
    assessment_mod.assess_category('feature_observability', 2)
    assessment_mod.assess_category('decision_documentation', 2)
    assessment_mod.assess_category('pattern_clarity', 2)
    assessment_mod.assess_category('constraint_discovery', 2)
    assessment_mod.assess_category('quality_attributes', 2)
    assessment_mod.calculate_total()

    rec_mod = assessment_mod.get_recommendation()
    assert rec_mod['level'] == 'moderately_extractable', \
        "Score 12 should be moderately_extractable"

    # Not extractable (<6)
    assessment_low = RubricAssessment(Path('/tmp/test'))
    assessment_low.assess_category('conversation_traceability', 0)
    assessment_low.assess_category('feature_observability', 1)
    assessment_low.assess_category('decision_documentation', 1)
    assessment_low.assess_category('pattern_clarity', 1)
    assessment_low.assess_category('constraint_discovery', 1)
    assessment_low.assess_category('quality_attributes', 1)
    assessment_low.calculate_total()

    rec_low = assessment_low.get_recommendation()
    assert rec_low['level'] == 'not_extractable', \
        "Score 5 should be not_extractable"


def test_not_extractable_recommendation_action():
    """Test 4: Not extractable recommendation says DO NOT EXTRACT."""
    assessment = RubricAssessment(Path('/tmp/test'))

    # Score below 6
    assessment.assess_category('conversation_traceability', 0)
    assessment.assess_category('feature_observability', 0)
    assessment.assess_category('decision_documentation', 1)
    assessment.assess_category('pattern_clarity', 1)
    assessment.assess_category('constraint_discovery', 1)
    assessment.assess_category('quality_attributes', 0)
    assessment.calculate_total()

    rec = assessment.get_recommendation()

    assert rec['level'] == 'not_extractable'
    assert 'DO NOT EXTRACT' in rec['action'], \
        "Not extractable action must say 'DO NOT EXTRACT'"
