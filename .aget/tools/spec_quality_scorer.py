#!/usr/bin/env python3
"""
Specification Quality Scorer

Detailed quality assessment for reverse-engineered specifications.

Measures:
- Completeness: % of observable features captured
- Accuracy: % of EARS statements correctly formatted
- Clarity: % of statements without ambiguity warnings

Based on Advanced benchmark: 70%+ overall quality for production-grade.
"""

import argparse
import sys
import yaml
from pathlib import Path
from typing import Dict, List, Tuple


class QualityScorer:
    """Score reverse-engineered specification quality."""

    def __init__(self, spec_path: Path, agent_path: Path):
        self.spec_path = Path(spec_path)
        self.agent_path = Path(agent_path)
        self.spec = None
        self.scores = {}

    def load_spec(self) -> Dict:
        """Load YAML specification."""
        with open(self.spec_path) as f:
            self.spec = yaml.safe_load(f)
        return self.spec

    def score_completeness(self) -> float:
        """
        Score completeness: % of observable features captured.

        Observable features:
        - Tools in .aget/tools/ (each tool = 2-3 capabilities expected)
        - Patterns in patterns/ (each pattern = 2-3 capabilities expected)
        - Scripts in scripts/ (each script = 1-2 capabilities expected)
        - Session mentions (high-frequency actions)
        """
        observable_count = 0

        # Count tools
        tools_dir = self.agent_path / '.aget' / 'tools'
        if tools_dir.exists():
            tools = list(tools_dir.glob('*.py'))
            observable_count += len(tools) * 2.5  # Average capabilities per tool

        # Count patterns
        patterns_dir = self.agent_path / 'patterns'
        if patterns_dir.exists():
            patterns = list(patterns_dir.glob('**/*.py'))
            observable_count += len(patterns) * 2.5

        # Count scripts
        scripts_dir = self.agent_path / 'scripts'
        if scripts_dir.exists():
            scripts = list(scripts_dir.glob('*.py'))
            observable_count += len(scripts) * 1.5

        # Minimum expected capabilities
        expected_capabilities = max(observable_count, 10)

        # Count extracted capabilities
        extracted_count = len(self.spec.get('capabilities', {}))

        # Completeness = min(extracted / expected, 1.0) * 100
        completeness = min((extracted_count / expected_capabilities), 1.0) * 100

        self.scores['completeness'] = round(completeness, 1)
        return self.scores['completeness']

    def score_accuracy(self) -> float:
        """
        Score accuracy: % of EARS statements correctly formatted.

        Checks:
        - Temporal pattern keywords present (WHEN/WHILE/IF/WHERE/The SYSTEM shall)
        - Pattern type matches keywords
        - Required fields present (trigger for event-driven, etc.)
        """
        capabilities = self.spec.get('capabilities', {})
        if not capabilities:
            self.scores['accuracy'] = 0.0
            return 0.0

        valid_count = 0
        total_count = len(capabilities)

        for cap_id, capability in capabilities.items():
            pattern = capability.get('pattern', '')
            statement = capability.get('statement', '')

            valid = True

            # Check pattern-specific requirements
            if pattern == 'ubiquitous':
                if not statement.startswith('The SYSTEM shall'):
                    valid = False
            elif pattern == 'event-driven':
                if not statement.startswith('WHEN'):
                    valid = False
                if 'trigger' not in capability:
                    valid = False
            elif pattern == 'state-driven':
                if not statement.startswith('WHILE'):
                    valid = False
                if 'state' not in capability:
                    valid = False
            elif pattern == 'conditional':
                if not statement.startswith('IF'):
                    valid = False
                if 'condition' not in capability:
                    valid = False
            elif pattern == 'optional':
                if not statement.startswith('WHERE'):
                    valid = False

            # Check required fields
            if 'domain' not in capability:
                valid = False

            if valid:
                valid_count += 1

        accuracy = (valid_count / total_count) * 100
        self.scores['accuracy'] = round(accuracy, 1)
        return self.scores['accuracy']

    def score_clarity(self) -> float:
        """
        Score clarity: % of statements without ambiguity.

        Simplified version - checks for:
        - Vague terms (may, might, should, could)
        - Missing inputs/outputs
        - Overly long statements (>200 chars)
        """
        capabilities = self.spec.get('capabilities', {})
        if not capabilities:
            self.scores['clarity'] = 0.0
            return 0.0

        clear_count = 0
        total_count = len(capabilities)

        vague_terms = ['may', 'might', 'should', 'could', 'possibly', 'maybe']

        for cap_id, capability in capabilities.items():
            statement = capability.get('statement', '').lower()

            clear = True

            # Check for vague terms
            if any(term in statement for term in vague_terms):
                clear = False

            # Check for missing inputs/outputs
            if not capability.get('inputs') or not capability.get('outputs'):
                clear = False

            # Check statement length
            if len(statement) > 200:
                clear = False

            if clear:
                clear_count += 1

        clarity = (clear_count / total_count) * 100
        self.scores['clarity'] = round(clarity, 1)
        return self.scores['clarity']

    def calculate_overall(self) -> float:
        """Calculate overall quality score (weighted average)."""
        if not self.scores:
            return 0.0

        completeness = self.scores.get('completeness', 0)
        accuracy = self.scores.get('accuracy', 0)
        clarity = self.scores.get('clarity', 0)

        # Weighted average (same as extract_spec.py)
        overall = (completeness * 0.5) + (accuracy * 0.3) + (clarity * 0.2)

        self.scores['overall'] = round(overall, 1)
        return self.scores['overall']

    def generate_report(self) -> str:
        """Generate quality assessment report."""
        report = []
        report.append("=" * 80)
        report.append("SPECIFICATION QUALITY ASSESSMENT")
        report.append("=" * 80)
        report.append(f"\nSpecification: {self.spec_path.name}")
        report.append(f"Source Agent: {self.agent_path.name}")
        report.append("")

        # Scores
        report.append("QUALITY SCORES:")
        report.append(f"  Completeness: {self.scores['completeness']:.1f}% (target: ≥75%)")
        report.append(f"  Accuracy:     {self.scores['accuracy']:.1f}% (target: ≥70%)")
        report.append(f"  Clarity:      {self.scores['clarity']:.1f}% (target: ≥65%)")
        report.append(f"  Overall:      {self.scores['overall']:.1f}% (target: ≥70%)")
        report.append("")

        # Assessment
        overall = self.scores['overall']
        if overall >= 70:
            assessment = "✅ PRODUCTION-GRADE (meets Advanced benchmark)"
        elif overall >= 60:
            assessment = "⚠️  ACCEPTABLE (below benchmark, manual review recommended)"
        else:
            assessment = "❌ INSUFFICIENT (improve source documentation and re-extract)"

        report.append(f"ASSESSMENT: {assessment}")
        report.append("")

        # Recommendations
        if overall < 70:
            report.append("RECOMMENDATIONS:")

            if self.scores['completeness'] < 75:
                report.append(f"  - Completeness low ({self.scores['completeness']:.1f}%)")
                report.append(f"    → Read more session files (currently limited coverage)")

            if self.scores['accuracy'] < 70:
                report.append(f"  - Accuracy low ({self.scores['accuracy']:.1f}%)")
                report.append(f"    → Review EARS pattern classification")

            if self.scores['clarity'] < 65:
                report.append(f"  - Clarity low ({self.scores['clarity']:.1f}%)")
                report.append(f"    → Remove vague terms, add inputs/outputs")

            report.append("")

        # Benchmark comparison
        capabilities_count = len(self.spec.get('capabilities', {}))
        report.append("PRODUCTION AGENT BENCHMARK COMPARISON:")
        report.append("  Advanced: 30 capabilities, 70%+ quality")
        report.append(f"  This spec: {capabilities_count} capabilities, {overall:.1f}% quality")
        report.append("")

        report.append("=" * 80)

        return "\n".join(report)


def main():
    parser = argparse.ArgumentParser(
        description='Score reverse-engineered specification quality'
    )
    parser.add_argument(
        'spec_path',
        type=Path,
        help='Path to specification YAML file'
    )
    parser.add_argument(
        'agent_path',
        type=Path,
        help='Path to source AGET agent directory'
    )

    args = parser.parse_args()

    # Validate paths
    if not args.spec_path.exists():
        print(f"Error: Specification not found: {args.spec_path}", file=sys.stderr)
        sys.exit(1)

    if not args.agent_path.exists():
        print(f"Error: Agent path not found: {args.agent_path}", file=sys.stderr)
        sys.exit(1)

    # Score quality
    scorer = QualityScorer(args.spec_path, args.agent_path)
    scorer.load_spec()

    scorer.score_completeness()
    scorer.score_accuracy()
    scorer.score_clarity()
    scorer.calculate_overall()

    # Print report
    print(scorer.generate_report())

    # Exit code based on quality
    if scorer.scores['overall'] >= 70:
        sys.exit(0)  # Success
    elif scorer.scores['overall'] >= 60:
        sys.exit(1)  # Warning
    else:
        sys.exit(2)  # Failure


if __name__ == '__main__':
    main()
