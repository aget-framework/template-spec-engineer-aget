# Sprint 002: Gate 2 - Pattern Library Foundation

**Sprint Duration**: ~20 hours (Phase 2 budget allocation)
**Target Release**: v2.0-beta (internal + limited external)
**Date Started**: 2025-09-22
**Gate Decision**: Go/No-Go for broader testing

## Sprint 002 Alignment Check

### Previous Sprint Actual Outcome
- ✅ Gate 1 PASSED - All 5 criteria met
- ✅ v2.0-alpha released and dogfooding active
- ✅ Core CLI architecture proven (<0.5s performance)
- ⚠️ Commands: 2 fully implemented (init, rollback), 3 placeholders (validate, apply, list)
- ⚠️ Cross-project risk detection added to scanner (not originally planned)

### This Sprint Starting Point
- Gate 1 complete, Phase 2 beginning
- v2.0-alpha deployed on aget-cli-agent-template
- Ready for pattern library implementation
- 3 placeholder commands need real functionality

### This Sprint Goal
Deliver the first 5-7 working patterns that agents can use immediately, making AGET valuable beyond just initialization.

## Success Criteria (Gate 2)

**MUST PASS ALL**:
- [ ] At least 5 patterns working and installable
- [ ] Pattern discovery mechanism functional (`aget list` shows available patterns)
- [ ] Pattern application works (`aget apply <pattern>`)
- [ ] Pattern validation prevents broken configs (`aget validate`)
- [ ] Documentation for each pattern exists
- [ ] <2 second performance maintained
- [ ] **NEW**: ≥1 real test per pattern (no test theater)
- [ ] **NEW**: Data corruption test mandatory

## Sprint Backlog with Checkpoints

### Step 1: Pattern Framework (5 hours)
- Create pattern registry system
- Implement pattern discovery mechanism
- Build pattern metadata structure
- Connect to `aget list` command
**CHECKPOINT 1**: Commit "feat: Pattern registry framework complete"

### Step 2: Core Patterns Implementation (8 hours)
Priority patterns based on existing usage:
1. **session** - Wake/wind-down protocols (most used)
2. **housekeeping** - Documentation/cleanup commands
**CHECKPOINT 2**: Commit "feat: Session and housekeeping patterns working"
3. **meta** - Multi-project management
4. **documentation** - README/CHANGELOG standards
5. **recovery** - Emergency/rollback procedures
**CHECKPOINT 3**: Commit "feat: All 5 core patterns implemented"

### Step 3: Command Enhancement (4 hours)
Transform placeholders into working commands:
- `aget validate` - Check pattern syntax and conflicts
- `aget apply <pattern>` - Install pattern to project
- `aget list` - Show available and installed patterns
**CHECKPOINT 4**: Commit "feat: Commands functional - ready for beta"

### Step 4: Testing & Documentation (3 hours)
- Test all patterns on 2+ projects
- Write pattern documentation
- Create pattern authoring guide
- Gate 2 validation suite
**CHECKPOINT 5**: Tag "v2.0-beta" if Gate 2 passes

## Definition of Done

### Code Deliverables
- [ ] `aget/patterns/registry.py` - Pattern discovery
- [ ] `aget/patterns/validator.py` - Pattern validation
- [ ] `aget/config/commands/validate.py` - Working command
- [ ] `aget/config/commands/apply.py` - Working command
- [ ] `aget/config/commands/list.py` - Working command
- [ ] 5+ patterns in `patterns/` directory

### Test Coverage
- [ ] Unit tests for pattern system
- [ ] Integration tests for each pattern
- [ ] Cross-project pattern testing
- [ ] Gate 2 acceptance tests

### Documentation
- [ ] Pattern authoring guide
- [ ] Individual pattern READMEs
- [ ] v2.0-beta release notes
- [ ] Updated examples in main README

## Risk Register

| Risk | Mitigation | Priority |
|------|------------|----------|
| Pattern conflicts between projects | Validation layer checks compatibility | High |
| Breaking existing v1 scripts | Keep patterns additive, not replacing | High |
| Performance degradation with patterns | Cache pattern metadata | Medium |
| Unclear pattern documentation | Test with external developer | Medium |

## Not In Scope (Explicitly Deferred)
- Migration tools (Gate 3)
- External documentation site (Gate 4)
- Cross-platform testing (Gate 4)
- Full test coverage (Gate 5)

## Post-Sprint

### On Success (Go)
1. Tag v2.0-beta release
2. Share with 3-5 external developers
3. Deploy patterns to test projects
4. Begin Gate 3 (migration focus)

### On Failure (No-Go)
1. Document specific pattern failures
2. Assess if core architecture needs adjustment
3. Reduce pattern scope if needed
4. Re-run sprint with fixes

## Notes from Sprint 001 Retrospective
- Documentation gaps caused confusion - being explicit about placeholders
- Cross-project dependencies are a risk - test patterns in isolation
- Every deviation needs documentation - noting why 3 commands remain basic

## Architecture Decisions Made
- ADR-007: Test requirements (no test theater allowed)
- ADR-008: Quality Agent as parent enforcement pattern
- Quality checking will start advisory, become strict over time

---

*Sprint commitment: Deliver working patterns that provide immediate value to agent-enabled projects.*