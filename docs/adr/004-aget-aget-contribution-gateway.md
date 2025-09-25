# ADR-004: aget-aget as Framework Contribution Gateway

**Date**: 2025-09-24
**Status**: Proposed
**Deciders**: Gabor Melli (first Path 2 user), AGET development team

## Context

As AGET matures, we need to consider how the framework itself will evolve. Initial thinking suggested `aget-aget` would be an autonomous maintenance agent. However, deeper reflection reveals a more valuable purpose: enabling community contributions to the framework.

## Decision

**aget-aget will be a contribution gateway agent, not a maintenance agent.**

It will serve the 1% of users who want to contribute back to AGET, not the 99% who just use it.

## Key Insight

There are two distinct user paths:

### Path 1: Framework Users (99%)
- Want AGET to make their project agent-ready
- Use `aget init` and continue with their work
- Don't care about AGET internals
- **Don't need aget-aget**

### Path 2: Framework Contributors (1%)
- Want to improve AGET itself
- Have discovered valuable patterns worth sharing
- Found bugs or performance improvements
- **Would use aget-aget to contribute back**

Gabor Melli will be the first Path 2 user, testing the contribution flow.

## Proposed Functionality

### Pattern Contribution Flow
```bash
# User discovers a great pattern in their project
aget-aget extract-pattern security/secret-scan

# aget-aget would:
# 1. Extract the pattern from their code
# 2. Generalize it (remove project-specific parts)
# 3. Create comprehensive tests
# 4. Generate PR to AGET repository
# 5. Track attribution to contributor
```

### Framework Enhancement Flow
```bash
# User has an idea for AGET improvement
aget-aget propose "Add support for Docker containers"

# aget-aget would:
# 1. Create RFC/ADR document
# 2. Set up prototype branch
# 3. Generate test cases
# 4. Open discussion issue
# 5. Guide implementation
```

### Pattern Discovery Network
```bash
# Opt-in anonymous pattern usage analytics
aget-aget join-network

# Would share (anonymously):
# - Which patterns are most used
# - Which patterns fail/succeed
# - Performance metrics
# - New pattern combinations discovered
# - Cross-agent compatibility results
```

## Community Intelligence Layer

aget-aget becomes the bridge between individual innovation and community benefit:

1. **Pattern Harvesting**: Discovers successful patterns in the wild
2. **Quality Gate**: Tests and validates contributions automatically
3. **Attribution System**: Credits pattern creators properly
4. **Evolution Tracking**: Shows how patterns evolve across projects
5. **Compatibility Matrix**: Tests patterns across different AI agents
6. **Performance Benchmarking**: Proves optimizations work

## Implementation Approach

### Phase 1: Manual Process Documentation
- Document how Gabor manually contributes patterns
- Identify automation opportunities
- Create contribution templates

### Phase 2: Semi-Automated Tools
- Scripts to extract and generalize patterns
- Automated test generation
- PR template creation

### Phase 3: aget-aget Agent
- Full autonomous agent for contribution
- Pattern quality validation
- Community voting integration
- Attribution tracking

## Governance Model

aget-aget could implement:
- **Pattern voting**: Community votes on new patterns
- **RFC process**: Structured proposals for major changes
- **Compatibility guarantees**: Ensures backward compatibility
- **Security reviews**: Automated scanning of contributed patterns
- **Performance requirements**: Patterns must meet <2s execution
- **Coverage requirements**: Contributed patterns need >80% test coverage

## Benefits

### For Contributors
- Easy way to share discoveries
- Proper attribution
- Community recognition
- Influence framework direction

### For AGET
- Scalable contribution process
- Quality maintained through automation
- Community-driven evolution
- Best patterns naturally rise to top

### For End Users
- Benefit from community discoveries
- Assured quality through automated gates
- Diverse pattern library
- Real-world tested patterns

## Risks and Mitigations

### Risk: Poor Quality Contributions
**Mitigation**: Automated testing, coverage requirements, performance benchmarks

### Risk: Security Vulnerabilities
**Mitigation**: Automated security scanning, sandbox testing, manual review for critical patterns

### Risk: Framework Fragmentation
**Mitigation**: Strong compatibility requirements, version management, deprecation policies

### Risk: Contribution Overhead
**Mitigation**: Make aget-aget so easy that contributing is easier than not contributing

## Alternatives Considered

### Alternative 1: aget-aget as Maintenance Bot
- Would auto-update dependencies, fix bugs
- Rejected: Less valuable than enabling contributions
- Maintenance can be handled with existing CI/CD

### Alternative 2: No aget-aget
- Manual contribution process only
- Rejected: Doesn't scale, high barrier to contribution
- Misses opportunity for community building

### Alternative 3: Web-Based Contribution Portal
- GitHub-style pattern marketplace
- Rejected: Adds infrastructure complexity
- CLI-first approach aligns with AGET philosophy

## Success Metrics

- Number of contributed patterns accepted
- Time from pattern discovery to PR creation
- Contributor retention rate
- Pattern usage metrics
- Community growth rate

## Next Steps

1. Gabor will test manual contribution flow
2. Document pain points and automation opportunities
3. Create initial extraction scripts
4. Design attribution system
5. Prototype pattern generalization logic

---

## Decision

We will build aget-aget as a framework contribution gateway, enabling the community to easily share their discoveries back to AGET. This creates a virtuous cycle where individual innovations become community benefits.

Gabor Melli commits to being the first Path 2 user, testing and refining the contribution flow.

---
*"The best patterns come from real usage, not theoretical design."*