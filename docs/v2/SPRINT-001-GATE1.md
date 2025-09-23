# Sprint 001: Gate 1 - Core CLI Foundation

**Sprint Duration**: ~19 hours (of 48 hour Phase 1 budget)
**Target Release**: v2.0-alpha (internal use)
**Date Committed**: 2025-09-22
**Gate Decision**: Go/No-Go for Phase 2

## Sprint Commitment

We commit to delivering the foundational architecture and first working command that proves AGET v2's core value proposition: safe, fast, universal agent configuration.

## Release Strategy: Gates as Incremental Value

### Why Gate-Based Releases

Each gate represents a natural release boundary where:
1. **Working software exists** - Not just infrastructure
2. **Value can be delivered** - Agents benefit immediately
3. **Feedback informs next phase** - Real usage, not speculation
4. **Risk is reduced** - Find issues after 19 hours, not 143

### Incremental Benefit Timeline

```
Sprint 1 / Gate 1 → v2.0-alpha (this sprint)
  ↳ RKB agent gets backup protection
  ↳ CCB can use core commands
  ↳ Dogfood on aget-cli-agent-template

Gate 2 → v2.0-beta
  ↳ 10+ patterns available
  ↳ Progressive adoption per project

Gate 3 → (migration only, no release)
  ↳ CCB: 60% → 100% complete
  ↳ RKB: Safety validated

Gate 4 → v2.0-rc
  ↳ First external users
  ↳ Documentation complete

Gate 5 → v2.0 (public)
  ↳ Full test coverage
  ↳ Cross-platform validated
```

## Sprint Backlog (19 hours)

### Step 1: Scanner Baseline (2 hours)
**Gate Prerequisite**: PROJECT_PLAN.md line 371
- Scan: aget-cli-agent-template, CCB, GM-RKB
- Output: `.aget/v2-baseline.json`
- Establishes migration complexity score

### Step 2: Core Architecture (6 hours)
**Gate 1 Criterion**: "Internal routing supports future expansion"
- Implement BaseCommand with three-tier degradation (ADR-004)
- Create ConfigModule structure (PROJECT_PLAN lines 123-139)
- Build capability detection (gh/git/python)

### Step 3: First Command - `aget init` (4 hours)
**Gate 1 Criterion**: "<2 second response time"
- Implement all three tiers:
  - gh tier: GitHub templates
  - git tier: .gitignore updates
  - basic tier: AGENTS.md creation
- Performance monitoring built-in

### Step 4: Backup Mechanism (4 hours)
**Gate 1 Criterion**: "Backup/rollback mechanism works"
- Implement .aget/ state management
- Version tracking with SemVer
- Critical for RKB agent safety

### Step 5: Gate 1 Validation (3 hours)
**Go/No-Go Decision Point**
- Run automated test suite
- Measure performance metrics
- Document results

## Gate 1 Success Criteria

**MUST PASS ALL**:
- [ ] All 5 commands execute without error
- [ ] <2 second response time (proven in Step 3)
- [ ] Backup/rollback mechanism works (proven in Step 4)
- [ ] Clean error messages
- [ ] Internal routing supports future expansion (proven in Step 2)

**Decision**: If ANY criterion fails → STOP, do not proceed to Phase 2

## Definition of Done

### Code Deliverables
- [ ] `aget/base.py` with BaseCommand class
- [ ] `aget/__main__.py` with routing
- [ ] `aget/config/commands/init.py`
- [ ] `aget/shared/capabilities.py`
- [ ] `aget/shared/backup.py`

### Test Coverage
- [ ] Unit tests for all modules
- [ ] Integration test for `aget init`
- [ ] Performance benchmark tests
- [ ] Gate 1 acceptance tests

### Documentation
- [ ] Docstrings for all public methods
- [ ] Updated PROJECT_PLAN with progress
- [ ] v2.0-alpha release notes

## Risk Register

| Risk | Mitigation | Owner |
|------|------------|-------|
| RKB data loss | Test backup mechanism thoroughly | Step 4 |
| Performance >2s | Profile early, optimize critical path | Step 3 |
| Architecture lock-in | Review at Step 2 completion | Step 2 |

## Post-Sprint

### On Success (Go)
1. Tag v2.0-alpha release
2. Deploy to aget-cli-agent-template (dogfood)
3. Test with CCB project
4. Begin Gate 2 / Phase 2 (Patterns)

### On Failure (No-Go)
1. Document specific failures
2. Estimate remediation effort
3. Revise Gate 1 criteria if needed
4. Re-run sprint with fixes

## References
- PROJECT_PLAN.md: Phase 1 scope
- ADR-003: V2 Charter Commitment
- ADR-004: Three-Tier Degradation Pattern

---

*Sprint commitment: Deliver working v2.0-alpha that benefits current agents immediately.*