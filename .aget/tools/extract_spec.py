#!/usr/bin/env python3
"""
AGET Reverse Engineering Specification Extractor

USAGE: This tool provides framework for coding agent to use.

Workflow (Coding Agent + Tool Collaboration):
1. Agent reads target agent's sessions/ and .aget/evolution/ files
2. Agent analyzes conversationally using semantic understanding (not just regex)
3. Agent uses this tool structure to output well-formatted EARS spec
4. Tool handles: rubric scoring, YAML formatting, quality validation, file I/O
5. Agent handles: pattern recognition, temporal classification, capability extraction

This is NOT fully automated extraction - it leverages coding agent intelligence:
- Agent understands context ("wake up" command → session management capability)
- Agent classifies temporal patterns (always used → ubiquitous, triggered → event-driven)
- Agent infers inputs/outputs from conversation examples
- Agent identifies domains through semantic categorization

Reference: EXTRACTION_METHODOLOGY.md for full 5-phase algorithm

Proven Methodology: Advanced extraction (Oct 2025)
- Input: 6,800 lines of sessions/evolution
- Output: 30-capability EARS specification
- Quality: 70%+ (production-grade)
- Validates: This approach works with coding agent semantic understanding
"""

import argparse
import sys
from pathlib import Path
from typing import Dict, List, Optional, Tuple
from datetime import datetime
import yaml
import json


class Pattern:
    """Represents an extracted behavioral pattern."""

    def __init__(
        self,
        domain: str,
        action: str,
        frequency: str = 'sometimes',
        trigger: Optional[str] = None,
        state: Optional[str] = None,
        condition: Optional[str] = None,
        precondition: Optional[str] = None,
        inputs: Optional[List[str]] = None,
        outputs: Optional[List[str]] = None,
        confidence: float = 1.0
    ):
        self.domain = domain
        self.action = action
        self.frequency = frequency
        self.trigger = trigger
        self.state = state
        self.condition = condition
        self.precondition = precondition
        self.inputs = inputs or []
        self.outputs = outputs or []
        self.confidence = confidence

    def classify_temporal_pattern(self) -> str:
        """
        Classify EARS temporal pattern based on pattern characteristics.

        Logic (coding agent assists with classification):
        - always + no trigger → ubiquitous
        - has trigger → event-driven
        - has state → state-driven
        - has condition → conditional
        - has precondition OR low confidence → optional (conservative default)
        """
        if self.frequency == 'always' and not self.trigger:
            return 'ubiquitous'
        elif self.trigger:
            return 'event-driven'
        elif self.state:
            return 'state-driven'
        elif self.condition:
            return 'conditional'
        else:
            return 'optional'  # Conservative default

    def to_ears_statement(self) -> str:
        """
        Generate EARS-formatted capability statement.

        Coding agent helps construct proper grammar.
        """
        temporal = self.classify_temporal_pattern()

        if temporal == 'ubiquitous':
            return f"The SYSTEM shall {self.action}"
        elif temporal == 'event-driven':
            return f"WHEN {self.trigger}, the SYSTEM shall {self.action}"
        elif temporal == 'state-driven':
            return f"WHILE {self.state}, the SYSTEM shall {self.action}"
        elif temporal == 'conditional':
            return f"IF {self.condition} THEN the SYSTEM shall {self.action}"
        else:  # optional
            precond = self.precondition or "applicable"
            return f"WHERE {precond}, the SYSTEM shall {self.action}"

    def to_capability_dict(self) -> Dict:
        """Convert pattern to capability dictionary for YAML output."""
        temporal = self.classify_temporal_pattern()

        capability = {
            'domain': self.domain,
            'statement': self.to_ears_statement(),
            'pattern': temporal,
            'inputs': self.inputs,
            'outputs': self.outputs
        }

        # Add pattern-specific fields
        if temporal == 'event-driven' and self.trigger:
            capability['trigger'] = self.trigger
        elif temporal == 'state-driven' and self.state:
            capability['state'] = self.state
        elif temporal == 'conditional' and self.condition:
            capability['condition'] = self.condition
        elif temporal == 'optional' and self.precondition:
            capability['precondition'] = self.precondition

        # Flag low confidence
        if self.confidence < 0.8:
            capability['confidence'] = self.confidence
            capability['note'] = 'Low confidence - manual review recommended'

        return capability


class SpecificationExtractor:
    """Extract EARS specification from AGET agent."""

    def __init__(self, agent_path: Path):
        self.agent_path = Path(agent_path)
        self.agent_name = agent_path.name
        self.patterns: List[Pattern] = []
        self.rubric_score: Optional[int] = None
        self.quality_scores: Dict[str, float] = {}

    def check_readiness(self) -> Tuple[int, str]:
        """
        Phase 1: Check if agent is ready for extraction.

        Coding agent examines:
        - Session file count and quality
        - Evolution file presence
        - Directory structure
        - Documentation completeness

        Returns: (rubric_score, recommendation)
        """
        # This is a simplified check - full assessment via assess_agent.py
        sessions_dir = self.agent_path / 'sessions'
        evolution_dir = self.agent_path / '.aget' / 'evolution'

        if not sessions_dir.exists() and not evolution_dir.exists():
            return 0, "No sessions or evolution files found - NOT EXTRACTABLE"

        # Rough scoring (coding agent would do detailed analysis)
        session_count = len(list(sessions_dir.glob('*.md'))) if sessions_dir.exists() else 0
        evolution_count = len(list(evolution_dir.glob('L*.md'))) if evolution_dir.exists() else 0

        # Simple heuristic
        score = 0
        if session_count >= 10:
            score += 6
        elif session_count >= 5:
            score += 3
        elif session_count >= 1:
            score += 1

        if evolution_count >= 5:
            score += 6
        elif evolution_count >= 2:
            score += 3
        elif evolution_count >= 1:
            score += 1

        # Add points for tools and patterns (observable features)
        tools_dir = self.agent_path / '.aget' / 'tools'
        if tools_dir.exists() and len(list(tools_dir.glob('*.py'))) > 3:
            score += 3

        patterns_dir = self.agent_path / 'patterns'
        if patterns_dir.exists() and len(list(patterns_dir.glob('**/*.py'))) > 3:
            score += 3

        self.rubric_score = min(score, 18)  # Cap at 18

        if self.rubric_score < 6:
            return self.rubric_score, "Score too low - NOT EXTRACTABLE (add more sessions/evolution)"
        elif self.rubric_score < 11:
            return self.rubric_score, "Poorly extractable - quality will be low (50-65%)"
        elif self.rubric_score < 15:
            return self.rubric_score, "Moderately extractable - proceed with manual review"
        else:
            return self.rubric_score, "Highly extractable - good quality expected (75%+)"

    def add_pattern(self, pattern: Pattern) -> None:
        """Add extracted pattern to collection."""
        self.patterns.append(pattern)

    def deduplicate_patterns(self) -> None:
        """
        Remove duplicate patterns.

        Coding agent identifies duplicates through semantic similarity.
        """
        # Simple deduplication by (domain, action)
        seen = set()
        unique = []

        for pattern in self.patterns:
            key = (pattern.domain, pattern.action.lower())
            if key not in seen:
                seen.add(key)
                unique.append(pattern)

        self.patterns = unique

    def generate_spec(
        self,
        version: str = '1.0.0',
        maturity: str = 'bootstrapping'
    ) -> Dict:
        """
        Phase 4: Assemble specification structure.

        Returns: YAML-serializable specification dict
        """
        spec_id = f"SPEC-{self.agent_name.upper().replace('-', '_')}"

        spec = {
            'spec': {
                'id': spec_id,
                'version': version,
                'maturity': maturity,
                'format_version': '1.1',
                'description': f"{self.agent_name} capabilities (reverse engineered)",
                'system_name': self.agent_name
            },
            'capabilities': {},
            'metadata': {
                'created': datetime.now().strftime('%Y-%m-%d'),
                'extraction_method': 'reverse_engineering',
                'source_agent_path': str(self.agent_path),
                'rubric_score': self.rubric_score or 0,
                'capability_count': len(self.patterns),
                'law_insider_precedent': True,
                'notes': 'Extracted via coding agent semantic analysis. Review low-confidence capabilities (<0.8).'
            }
        }

        # Add capabilities
        for idx, pattern in enumerate(self.patterns, 1):
            cap_id = f"CAP-{idx:03d}"
            spec['capabilities'][cap_id] = pattern.to_capability_dict()

        # Add quality scores if calculated
        if self.quality_scores:
            spec['metadata']['quality_assessment'] = self.quality_scores

        return spec

    def calculate_quality_scores(self) -> Dict[str, float]:
        """
        Phase 5: Calculate quality metrics.

        Simplified version - full quality assessment in spec_quality_scorer.py

        Returns: Dict with completeness, accuracy, clarity, overall
        """
        if not self.patterns:
            return {
                'completeness': 0.0,
                'accuracy': 0.0,
                'clarity': 0.0,
                'overall': 0.0
            }

        # Completeness: rough estimate based on observable features
        tools_dir = self.agent_path / '.aget' / 'tools'
        observable_features = 0
        if tools_dir.exists():
            observable_features += len(list(tools_dir.glob('*.py')))

        patterns_dir = self.agent_path / 'patterns'
        if patterns_dir.exists():
            observable_features += len(list(patterns_dir.glob('**/*.py')))

        # Assume 2-3 capabilities per observable feature
        expected_capabilities = max(observable_features * 2.5, 10)  # Minimum 10
        completeness = min((len(self.patterns) / expected_capabilities) * 100, 100)

        # Accuracy: % of high-confidence patterns
        high_confidence_count = sum(1 for p in self.patterns if p.confidence >= 0.8)
        accuracy = (high_confidence_count / len(self.patterns)) * 100 if self.patterns else 0

        # Clarity: simplified (would use ambiguity_detector.py)
        # For now, assume 70% (coding agent provides good clarity)
        clarity = 70.0

        # Overall: weighted average
        overall = (completeness * 0.5) + (accuracy * 0.3) + (clarity * 0.2)

        self.quality_scores = {
            'completeness': round(completeness, 1),
            'accuracy': round(accuracy, 1),
            'clarity': round(clarity, 1),
            'overall': round(overall, 1)
        }

        return self.quality_scores

    def save_spec(self, output_path: Path) -> None:
        """Save specification to YAML file."""
        spec = self.generate_spec()

        output_path.parent.mkdir(parents=True, exist_ok=True)

        with open(output_path, 'w') as f:
            yaml.dump(spec, f, default_flow_style=False, sort_keys=False, width=120)

    def generate_report(self) -> str:
        """Generate extraction summary report."""
        quality = self.quality_scores or self.calculate_quality_scores()

        report = []
        report.append("=" * 80)
        report.append("SPECIFICATION EXTRACTION REPORT")
        report.append("=" * 80)
        report.append(f"\nAgent: {self.agent_name}")
        report.append(f"Path: {self.agent_path}")
        report.append(f"Rubric Score: {self.rubric_score}/18")
        report.append("")

        # Capability summary
        report.append(f"Capabilities Extracted: {len(self.patterns)}")

        # Domain breakdown
        domains = {}
        for pattern in self.patterns:
            domains[pattern.domain] = domains.get(pattern.domain, 0) + 1

        if domains:
            report.append("\nDomain Breakdown:")
            for domain, count in sorted(domains.items(), key=lambda x: x[1], reverse=True):
                report.append(f"  - {domain}: {count} capabilities")

        report.append("")

        # Temporal pattern breakdown
        temporal_patterns = {}
        for pattern in self.patterns:
            temp = pattern.classify_temporal_pattern()
            temporal_patterns[temp] = temporal_patterns.get(temp, 0) + 1

        if temporal_patterns:
            report.append("Temporal Pattern Breakdown:")
            for temp, count in sorted(temporal_patterns.items(), key=lambda x: x[1], reverse=True):
                report.append(f"  - {temp}: {count} capabilities")

        report.append("")

        # Quality assessment
        report.append("QUALITY ASSESSMENT:")
        report.append(f"  Completeness: {quality['completeness']:.1f}% (target: ≥75%)")
        report.append(f"  Accuracy:     {quality['accuracy']:.1f}% (target: ≥70%)")
        report.append(f"  Clarity:      {quality['clarity']:.1f}% (target: ≥65%)")
        report.append(f"  Overall:      {quality['overall']:.1f}% (target: ≥70%)")
        report.append("")

        # Benchmark comparison
        report.append("PRODUCTION AGENT BENCHMARK COMPARISON:")
        report.append("  Advanced: 30 capabilities, 70%+ quality (production-grade)")
        report.append(f"  This extraction: {len(self.patterns)} capabilities, {quality['overall']:.1f}% quality")

        if quality['overall'] >= 70:
            report.append("  ✅ MEETS BENCHMARK (production-grade quality)")
        elif quality['overall'] >= 60:
            report.append("  ⚠️  BELOW BENCHMARK (acceptable for v1.0, manual review recommended)")
        else:
            report.append("  ❌ WELL BELOW BENCHMARK (improve source documentation and re-extract)")

        report.append("")

        # Low confidence flags
        low_conf = [p for p in self.patterns if p.confidence < 0.8]
        if low_conf:
            report.append(f"LOW CONFIDENCE CAPABILITIES ({len(low_conf)}):")
            report.append("  Manual review recommended for:")
            for pattern in low_conf[:5]:  # Show first 5
                report.append(f"    - {pattern.domain}: {pattern.action} (confidence: {pattern.confidence:.2f})")
            if len(low_conf) > 5:
                report.append(f"    ... and {len(low_conf) - 5} more")
            report.append("")

        report.append("=" * 80)

        return "\n".join(report)


def main():
    parser = argparse.ArgumentParser(
        description='Extract EARS specification from AGET agent (coding agent scaffolding)'
    )
    parser.add_argument(
        'agent_path',
        type=Path,
        help='Path to AGET agent directory'
    )
    parser.add_argument(
        '--output',
        type=Path,
        help='Output specification file path (default: agent/.aget/specs/agent_name_REVERSE_ENGINEERED_v1.0.yaml)'
    )
    parser.add_argument(
        '--check-only',
        action='store_true',
        help='Only check readiness, do not extract'
    )
    parser.add_argument(
        '--version',
        default='1.0.0',
        help='Specification version (default: 1.0.0)'
    )
    parser.add_argument(
        '--maturity',
        choices=['bootstrapping', 'minimal', 'standard', 'exemplary'],
        default='bootstrapping',
        help='Specification maturity level (default: bootstrapping)'
    )
    parser.add_argument(
        '--json',
        action='store_true',
        help='Output report as JSON'
    )

    args = parser.parse_args()

    # Verify agent path
    if not args.agent_path.exists():
        print(f"Error: Agent path does not exist: {args.agent_path}", file=sys.stderr)
        sys.exit(1)

    # Create extractor
    extractor = SpecificationExtractor(args.agent_path)

    # Phase 1: Check readiness
    score, recommendation = extractor.check_readiness()
    print(f"\nReadiness Assessment: {score}/18")
    print(f"Recommendation: {recommendation}\n")

    if args.check_only:
        sys.exit(0 if score >= 6 else 2)

    if score < 6:
        print("❌ Extraction rejected - rubric score too low (<6/18)")
        print("   Build more documentation (sessions, evolution files) and retry.\n")
        sys.exit(2)

    # NOTE: Phases 2-3 are performed by coding agent interactively
    # This tool provides the structure, coding agent provides the analysis

    print("⚠️  This tool provides scaffolding for coding agent extraction.")
    print("   Coding agent should:")
    print("   1. Read sessions/ and .aget/evolution/ files")
    print("   2. Identify patterns through semantic analysis")
    print("   3. Create Pattern objects via extractor.add_pattern()")
    print("   4. Call extractor.generate_spec() to create YAML structure")
    print("")
    print("   For automated testing, use with --check-only flag.")
    print("   For real extraction, use coding agent conversationally.\n")


if __name__ == '__main__':
    main()
