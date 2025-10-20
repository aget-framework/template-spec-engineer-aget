#!/usr/bin/env python3
"""
Python Code Reverse Engineering Readiness Assessment

USAGE: This tool provides framework for coding agent to use.

Workflow:
1. Coding agent examines target codebase structure and history
2. Agent applies rubric scoring (6 categories, 0-3 each)
3. Agent uses this tool to calculate weighted total and recommendation
4. Tool handles: scoring logic, weighting, threshold determination
5. Agent handles: evaluating code quality, development history, documentation

This is NOT fully automated - it leverages coding agent judgment for assessment.

Works for:
- Python functions, scripts, modules, and applications
- AGET agents (as one use case)
- Legacy code, API clients, CLI tools, any Python codebase

Reference: EXTRACTION_METHODOLOGY.md for full rubric details
"""

import argparse
import sys
from pathlib import Path
from typing import Dict, Tuple
import json


class RubricAssessment:
    """Assess Python code reverse-engineering readiness."""

    # Category weights (must sum to 1.0)
    WEIGHTS = {
        'development_history': 0.25,
        'code_observability': 0.20,
        'decision_documentation': 0.20,
        'pattern_clarity': 0.15,
        'constraint_discovery': 0.10,
        'quality_attributes': 0.10
    }

    # Thresholds for recommendations
    HIGHLY_EXTRACTABLE = 15  # 83-100%
    MODERATELY_EXTRACTABLE = 11  # 61-82%
    POORLY_EXTRACTABLE = 6  # 33-60%
    # Below 6 = Not Extractable (0-32%)

    def __init__(self, agent_path: Path):
        self.agent_path = Path(agent_path)
        self.scores = {}
        self.total_score = 0
        self.weighted_score = 0.0

    def assess_category(self, category: str, score: int) -> None:
        """
        Record score for a category.

        Args:
            category: One of the 6 rubric categories
            score: 0-3 (0=none, 1=poor, 2=good, 3=excellent)
        """
        if category not in self.WEIGHTS:
            raise ValueError(f"Unknown category: {category}")

        if not 0 <= score <= 3:
            raise ValueError(f"Score must be 0-3, got {score}")

        self.scores[category] = score

    def calculate_total(self) -> Tuple[int, float]:
        """
        Calculate total score and weighted percentage.

        Returns:
            (total_score, weighted_percentage)
        """
        if len(self.scores) != 6:
            missing = set(self.WEIGHTS.keys()) - set(self.scores.keys())
            raise ValueError(f"Not all categories scored. Missing: {missing}")

        # Total score (0-18)
        self.total_score = sum(self.scores.values())

        # Weighted percentage (0-100)
        self.weighted_score = sum(
            self.scores[cat] * self.WEIGHTS[cat] * (100 / 3)
            for cat in self.WEIGHTS
        )

        return self.total_score, self.weighted_score

    def get_recommendation(self) -> Dict[str, str]:
        """
        Get recommendation based on total score.

        Returns:
            Dict with level, message, and action
        """
        if self.total_score >= self.HIGHLY_EXTRACTABLE:
            return {
                'level': 'highly_extractable',
                'range': '83-100%',
                'message': 'Professional spec can be extracted with minimal information loss',
                'action': 'Proceed with extraction (expected quality: 75%+)'
            }
        elif self.total_score >= self.MODERATELY_EXTRACTABLE:
            return {
                'level': 'moderately_extractable',
                'range': '61-82%',
                'message': 'Spec extractable with effort, some gaps need filling',
                'action': 'Proceed with extraction (expected quality: 65-75%, manual review recommended)'
            }
        elif self.total_score >= self.POORLY_EXTRACTABLE:
            return {
                'level': 'poorly_extractable',
                'range': '33-60%',
                'message': 'Significant reconstruction needed, major gaps in understanding',
                'action': 'Extraction possible but quality will be low (50-65%). Consider building more documentation first.'
            }
        else:
            return {
                'level': 'not_extractable',
                'range': '0-32%',
                'message': 'Specification cannot be reliably extracted - would require extensive rebuilding',
                'action': 'DO NOT EXTRACT. Build more documentation first (add 5-10 sessions, 3-5 evolution files), retry in 1-2 weeks.'
            }

    def get_category_breakdown(self) -> Dict[str, Dict]:
        """
        Get detailed breakdown of each category score.

        Returns:
            Dict mapping category to score, weight, contribution
        """
        breakdown = {}
        for category, weight in self.WEIGHTS.items():
            score = self.scores.get(category, 0)
            contribution = (score / 3.0) * weight * 100
            breakdown[category] = {
                'score': score,
                'max': 3,
                'weight': weight,
                'contribution_percent': round(contribution, 1)
            }
        return breakdown

    def generate_report(self) -> str:
        """Generate human-readable assessment report."""
        total, weighted = self.calculate_total()
        recommendation = self.get_recommendation()
        breakdown = self.get_category_breakdown()

        report = []
        report.append("=" * 80)
        report.append("PYTHON CODE REVERSE ENGINEERING READINESS ASSESSMENT")
        report.append("=" * 80)
        report.append(f"\nTarget: {self.agent_path.name}")
        report.append(f"Path: {self.agent_path}")
        report.append("")

        # Overall score
        report.append(f"TOTAL SCORE: {total}/18 ({weighted:.1f}%)")
        report.append(f"ASSESSMENT: {recommendation['level'].upper()} ({recommendation['range']})")
        report.append("")

        # Category breakdown
        report.append("CATEGORY BREAKDOWN:")
        report.append("-" * 80)
        report.append(f"{'Category':<35} {'Score':<10} {'Weight':<10} {'Contribution'}")
        report.append("-" * 80)

        for category, details in breakdown.items():
            category_name = category.replace('_', ' ').title()
            score_str = f"{details['score']}/{details['max']}"
            weight_str = f"{details['weight']*100:.0f}%"
            contrib_str = f"{details['contribution_percent']:.1f}%"
            report.append(f"{category_name:<35} {score_str:<10} {weight_str:<10} {contrib_str}")

        report.append("-" * 80)
        report.append("")

        # Recommendation
        report.append("RECOMMENDATION:")
        report.append(f"  {recommendation['message']}")
        report.append("")
        report.append("ACTION:")
        report.append(f"  {recommendation['action']}")
        report.append("")

        # Improvement suggestions (if not highly extractable)
        if total < self.HIGHLY_EXTRACTABLE:
            report.append("IMPROVEMENT SUGGESTIONS:")

            # Find weakest categories
            sorted_cats = sorted(
                breakdown.items(),
                key=lambda x: x[1]['score']
            )

            for category, details in sorted_cats[:3]:  # Top 3 weakest
                if details['score'] < 3:
                    category_name = category.replace('_', ' ').title()
                    report.append(f"  - {category_name}: {details['score']}/3")

                    # Specific suggestions
                    if category == 'development_history' and details['score'] < 2:
                        report.append(f"    → Add git commits with clear messages, code comments, or session files")
                    elif category == 'code_observability' and details['score'] < 2:
                        report.append(f"    → Add docstrings, usage examples (tests), clear function signatures")
                    elif category == 'decision_documentation' and details['score'] < 2:
                        report.append(f"    → Document design decisions in comments or separate docs")
                    elif category == 'pattern_clarity' and details['score'] < 2:
                        report.append(f"    → Identify and document reusable patterns and design choices")
                    elif category == 'constraint_discovery' and details['score'] < 2:
                        report.append(f"    → Document boundary conditions, error cases, validation logic")
                    elif category == 'quality_attributes' and details['score'] < 2:
                        report.append(f"    → Add performance notes, reliability indicators, security considerations")

            report.append("")

        report.append("=" * 80)

        return "\n".join(report)

    def to_json(self) -> str:
        """Export assessment as JSON."""
        total, weighted = self.calculate_total()
        recommendation = self.get_recommendation()

        return json.dumps({
            'agent_path': str(self.agent_path),
            'agent_name': self.agent_path.name,
            'total_score': total,
            'max_score': 18,
            'weighted_percentage': round(weighted, 1),
            'assessment_level': recommendation['level'],
            'recommendation': recommendation,
            'category_scores': self.scores,
            'category_breakdown': self.get_category_breakdown()
        }, indent=2)


def main():
    parser = argparse.ArgumentParser(
        description='Assess Python code reverse-engineering readiness'
    )
    parser.add_argument(
        'agent_path',
        type=Path,
        help='Path to Python codebase (script, module, or AGET agent)'
    )
    parser.add_argument(
        '--development-history',
        type=int,
        choices=[0, 1, 2, 3],
        required=True,
        help='Score for development history (git commits, comments, sessions) (0-3)'
    )
    parser.add_argument(
        '--code-observability',
        type=int,
        choices=[0, 1, 2, 3],
        required=True,
        help='Score for code observability (docstrings, tests, clear signatures) (0-3)'
    )
    parser.add_argument(
        '--decision-documentation',
        type=int,
        choices=[0, 1, 2, 3],
        required=True,
        help='Score for decision documentation (0-3)'
    )
    parser.add_argument(
        '--pattern-clarity',
        type=int,
        choices=[0, 1, 2, 3],
        required=True,
        help='Score for pattern clarity (0-3)'
    )
    parser.add_argument(
        '--constraint-discovery',
        type=int,
        choices=[0, 1, 2, 3],
        required=True,
        help='Score for constraint discovery (0-3)'
    )
    parser.add_argument(
        '--quality-attributes',
        type=int,
        choices=[0, 1, 2, 3],
        required=True,
        help='Score for quality attributes (0-3)'
    )
    parser.add_argument(
        '--json',
        action='store_true',
        help='Output as JSON instead of human-readable report'
    )

    args = parser.parse_args()

    # Verify agent path exists
    if not args.agent_path.exists():
        print(f"Error: Agent path does not exist: {args.agent_path}", file=sys.stderr)
        sys.exit(1)

    # Create assessment
    assessment = RubricAssessment(args.agent_path)

    # Record scores
    assessment.assess_category('development_history', args.development_history)
    assessment.assess_category('code_observability', args.code_observability)
    assessment.assess_category('decision_documentation', args.decision_documentation)
    assessment.assess_category('pattern_clarity', args.pattern_clarity)
    assessment.assess_category('constraint_discovery', args.constraint_discovery)
    assessment.assess_category('quality_attributes', args.quality_attributes)

    # Generate output
    if args.json:
        print(assessment.to_json())
    else:
        print(assessment.generate_report())

    # Exit code based on extractability
    total, _ = assessment.calculate_total()
    if total < RubricAssessment.POORLY_EXTRACTABLE:
        sys.exit(2)  # Not extractable
    elif total < RubricAssessment.MODERATELY_EXTRACTABLE:
        sys.exit(1)  # Poorly extractable (warning)
    else:
        sys.exit(0)  # Extractable


if __name__ == '__main__':
    main()
