#!/usr/bin/env python3
"""
Specification Comparison Tool

Compare original specification vs reverse-engineered specification.

Useful for validating extraction accuracy when original spec exists.
"""

import argparse
import sys
import yaml
from pathlib import Path
from typing import Dict, Set, List


class SpecComparator:
    """Compare two specifications."""

    def __init__(self, spec1_path: Path, spec2_path: Path):
        self.spec1_path = Path(spec1_path)
        self.spec2_path = Path(spec2_path)
        self.spec1 = None
        self.spec2 = None

    def load_specs(self):
        """Load both specifications."""
        with open(self.spec1_path) as f:
            self.spec1 = yaml.safe_load(f)

        with open(self.spec2_path) as f:
            self.spec2 = yaml.safe_load(f)

    def compare_capability_coverage(self) -> Dict:
        """
        Compare capability coverage between specs.

        Returns dict with:
        - total_spec1: Count in spec1
        - total_spec2: Count in spec2
        - coverage_percent: % of spec1 capabilities in spec2
        - missing: Capabilities in spec1 but not spec2
        - new: Capabilities in spec2 but not spec1
        """
        caps1 = self.spec1.get('capabilities', {})
        caps2 = self.spec2.get('capabilities', {})

        # Extract capability domains and actions for comparison
        def get_capability_signature(cap):
            domain = cap.get('domain', '')
            statement = cap.get('statement', '').lower()
            # Normalize statement (remove WHEN/WHILE/IF/WHERE prefixes)
            for prefix in ['when ', 'while ', 'if ', 'where ', 'the system shall ']:
                statement = statement.replace(prefix, '')
            return f"{domain}:{statement[:50]}"  # First 50 chars

        sigs1 = {get_capability_signature(cap) for cap in caps1.values()}
        sigs2 = {get_capability_signature(cap) for cap in caps2.values()}

        missing = sigs1 - sigs2
        new = sigs2 - sigs1
        common = sigs1 & sigs2

        coverage = (len(common) / len(sigs1) * 100) if sigs1 else 0

        return {
            'total_spec1': len(caps1),
            'total_spec2': len(caps2),
            'common': len(common),
            'coverage_percent': round(coverage, 1),
            'missing_count': len(missing),
            'new_count': len(new)
        }

    def compare_ears_patterns(self) -> Dict:
        """Compare EARS temporal pattern distribution."""
        caps1 = self.spec1.get('capabilities', {})
        caps2 = self.spec2.get('capabilities', {})

        def count_patterns(caps):
            patterns = {}
            for cap in caps.values():
                pattern = cap.get('pattern', 'unknown')
                patterns[pattern] = patterns.get(pattern, 0) + 1
            return patterns

        patterns1 = count_patterns(caps1)
        patterns2 = count_patterns(caps2)

        return {
            'spec1_patterns': patterns1,
            'spec2_patterns': patterns2
        }

    def generate_report(self) -> str:
        """Generate comparison report."""
        report = []
        report.append("=" * 80)
        report.append("SPECIFICATION COMPARISON")
        report.append("=" * 80)
        report.append(f"\nSpec 1 (Original): {self.spec1_path.name}")
        report.append(f"Spec 2 (Comparison): {self.spec2_path.name}")
        report.append("")

        # Capability coverage
        coverage = self.compare_capability_coverage()

        report.append("CAPABILITY COVERAGE:")
        report.append(f"  Spec 1: {coverage['total_spec1']} capabilities")
        report.append(f"  Spec 2: {coverage['total_spec2']} capabilities")
        report.append(f"  Common: {coverage['common']} capabilities")
        report.append(f"  Coverage: {coverage['coverage_percent']:.1f}%")
        report.append(f"  Missing in Spec 2: {coverage['missing_count']}")
        report.append(f"  New in Spec 2: {coverage['new_count']}")
        report.append("")

        # EARS pattern comparison
        patterns = self.compare_ears_patterns()

        report.append("EARS PATTERN DISTRIBUTION:")
        report.append("  Spec 1:")
        for pattern, count in sorted(patterns['spec1_patterns'].items()):
            report.append(f"    - {pattern}: {count}")

        report.append("  Spec 2:")
        for pattern, count in sorted(patterns['spec2_patterns'].items()):
            report.append(f"    - {pattern}: {count}")
        report.append("")

        # Assessment
        if coverage['coverage_percent'] >= 80:
            assessment = "✅ EXCELLENT - High coverage, spec2 captures most of spec1"
        elif coverage['coverage_percent'] >= 60:
            assessment = "⚠️  GOOD - Moderate coverage, some gaps in spec2"
        else:
            assessment = "❌ POOR - Low coverage, significant gaps in spec2"

        report.append(f"ASSESSMENT: {assessment}")
        report.append("")

        # Recommendations
        if coverage['missing_count'] > 0:
            report.append("RECOMMENDATIONS:")
            report.append(f"  - {coverage['missing_count']} capabilities missing in Spec 2")
            report.append(f"    → Review original spec, add missing capabilities to Spec 2")

        if coverage['new_count'] > 0:
            report.append(f"  - {coverage['new_count']} new capabilities in Spec 2")
            report.append(f"    → These may be legitimate additions or extraction errors")

        report.append("")
        report.append("=" * 80)

        return "\n".join(report)


def main():
    parser = argparse.ArgumentParser(
        description='Compare two EARS specifications'
    )
    parser.add_argument(
        'spec1',
        type=Path,
        help='Path to first specification (original)'
    )
    parser.add_argument(
        'spec2',
        type=Path,
        help='Path to second specification (comparison/reverse-engineered)'
    )

    args = parser.parse_args()

    # Validate paths
    if not args.spec1.exists():
        print(f"Error: Spec 1 not found: {args.spec1}", file=sys.stderr)
        sys.exit(1)

    if not args.spec2.exists():
        print(f"Error: Spec 2 not found: {args.spec2}", file=sys.stderr)
        sys.exit(1)

    # Compare
    comparator = SpecComparator(args.spec1, args.spec2)
    comparator.load_specs()

    print(comparator.generate_report())


if __name__ == '__main__':
    main()
