#!/usr/bin/env python3
"""
Sample Extraction: private-github-AGET

Demonstrates how coding agent uses extract_spec.py to extract capabilities.

This script simulates coding agent semantic analysis:
1. Reads sessions and evolution files
2. Identifies patterns through understanding context
3. Creates Pattern objects
4. Generates EARS specification

This is what happens when coding agent uses the template conversationally.
"""

import sys
from pathlib import Path

# Add tools to path
sys.path.insert(0, str(Path(__file__).parent.parent / '.aget' / 'tools'))

from extract_spec import SpecificationExtractor, Pattern


def extract_private_github_aget():
    """
    Simulate coding agent extraction of private-github-AGET.

    Coding agent would:
    1. Read FIRST_SESSION_2025-09-27.md
    2. Identify capabilities from observations
    3. Read evolution files for constraints
    4. Create Pattern objects
    5. Generate specification
    """

    agent_path = Path.home() / 'github' / 'private-github-aget'

    if not agent_path.exists():
        print(f"Agent not found: {agent_path}")
        return

    # Create extractor
    extractor = SpecificationExtractor(agent_path)

    # Phase 1: Check readiness
    score, recommendation = extractor.check_readiness()
    print(f"Readiness: {score}/18 - {recommendation}\n")

    if score < 6:
        print("Not extractable - stopping")
        return

    # Phase 2-3: Coding agent analyzes sessions and extracts patterns

    # From FIRST_SESSION_2025-09-27.md analysis:

    # Pattern 1: Workspace scanning (ubiquitous capability)
    extractor.add_pattern(Pattern(
        domain='workspace_monitoring',
        action='scan workspace directory for git repositories',
        frequency='always',
        inputs=['workspace directory path'],
        outputs=['repository list', 'repository metadata', 'scan statistics'],
        confidence=0.95
    ))

    # Pattern 2: AGET version detection (event-driven on scan)
    extractor.add_pattern(Pattern(
        domain='aget_detection',
        action='identify AGET-enabled repositories and extract version information',
        trigger='workspace scan is performed',
        inputs=['repository directories'],
        outputs=['AGET version distribution', 'agent-configured repository count'],
        confidence=0.90
    ))

    # Pattern 3: Activity tracking (ubiquitous)
    extractor.add_pattern(Pattern(
        domain='workspace_monitoring',
        action='track most recent activity across all repositories',
        frequency='always',
        inputs=['repository list'],
        outputs=['sorted activity list', 'timestamps', 'most recently modified repos'],
        confidence=0.92
    ))

    # Pattern 4: Report generation (event-driven on scan completion)
    extractor.add_pattern(Pattern(
        domain='reporting',
        action='generate workspace report with statistics and findings',
        trigger='workspace scan completes',
        inputs=['scan results', 'repository metadata'],
        outputs=['workspace report markdown file', 'statistics summary'],
        confidence=0.93
    ))

    # Pattern 5: Wake protocol (event-driven on user command)
    extractor.add_pattern(Pattern(
        domain='session_management',
        action='adjust to workspace directory structure and execute wake protocol',
        trigger="user says 'wake up'",
        inputs=["user command: 'wake up'"],
        outputs=['session initialization', 'workspace position confirmation'],
        confidence=0.88
    ))

    # Pattern 6: Performance monitoring (ubiquitous)
    extractor.add_pattern(Pattern(
        domain='quality',
        action='measure and report scan performance metrics',
        frequency='always',
        inputs=['scan operation'],
        outputs=['performance timing', 'scan duration metrics'],
        confidence=0.85
    ))

    # Pattern 7: Repository categorization (ubiquitous)
    extractor.add_pattern(Pattern(
        domain='workspace_monitoring',
        action='categorize repositories by type (AGET-enabled vs standard)',
        frequency='always',
        inputs=['repository list', 'AGET detection results'],
        outputs=['repository categories', 'distribution statistics'],
        confidence=0.91
    ))

    # Pattern 8: Trust configuration detection (state-driven)
    extractor.add_pattern(Pattern(
        domain='configuration',
        action='detect and note trust configuration settings',
        state='Claude Code prompts for trust confirmation',
        inputs=['execution environment', 'trust settings files'],
        outputs=['trust configuration notes', 'settings recommendations'],
        confidence=0.75
    ))

    # Pattern 9: Path handling (conditional on workspace location)
    extractor.add_pattern(Pattern(
        domain='session_management',
        action='use absolute paths for script execution',
        condition='running from my-github-aget subdirectory',
        inputs=['current working directory', 'script locations'],
        outputs=['adjusted command paths', 'execution commands'],
        confidence=0.87
    ))

    # Pattern 10: Issue management (inferred from agent purpose)
    extractor.add_pattern(Pattern(
        domain='github_integration',
        action='manage GitHub issues and pull requests',
        precondition='GitHub API access available',
        inputs=['GitHub repository', 'issue parameters'],
        outputs=['created issues', 'PR operations'],
        confidence=0.70  # Lower confidence - inferred not directly observed
    ))

    # Phase 4: Deduplicate
    extractor.deduplicate_patterns()

    # Phase 5: Calculate quality
    quality = extractor.calculate_quality_scores()

    # Generate spec
    spec = extractor.generate_spec(version='1.0.0', maturity='bootstrapping')

    # Save spec
    output_path = agent_path / '.aget' / 'specs' / 'private_github_aget_REVERSE_ENGINEERED_v1.0.yaml'
    extractor.save_spec(output_path)

    # Generate report
    print(extractor.generate_report())

    print(f"\n✅ Specification saved to:")
    print(f"   {output_path}\n")

    return extractor


if __name__ == '__main__':
    extractor = extract_private_github_aget()
