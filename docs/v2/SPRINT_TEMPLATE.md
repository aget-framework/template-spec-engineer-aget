# Sprint [NUMBER]: Gate [X] - [TITLE]

**Sprint Duration**: ~XX hours
**Target Release**: vX.X-[stage]
**Date Started**: YYYY-MM-DD
**Gate Decision**: Go/No-Go for [next phase]

## Sprint Alignment Check

### Previous Sprint Actual Outcome
- What was delivered (be specific about partial implementations)
- Key decisions that changed scope
- Technical debt or deferred items

### This Sprint Starting Point
- Current working state (what works, what doesn't)
- Dependencies resolved
- Clear understanding of scope

### This Sprint Goal
[One sentence describing the primary deliverable]

## Success Criteria (Gate X)

**MUST PASS ALL**:
- [ ] [Specific measurable criterion]
- [ ] [Another criterion]
- [ ] Performance maintained (<2s)

## Sprint Backlog with Checkpoints

### Step 1: [Major Task] (X hours)
- Subtask 1
- Subtask 2
**CHECKPOINT 1**: Commit "type: Description of milestone"

### Step 2: [Major Task] (X hours)
- Subtask 1
- Subtask 2
**CHECKPOINT 2**: Commit "type: Description of milestone"

### Step N: Gate Validation (X hours)
- Run acceptance tests
- Document results
**CHECKPOINT N**: Tag "vX.X-stage" if gate passes

## Checkpoint Planning

| Checkpoint | Trigger | Commit Message | Rollback Point |
|------------|---------|----------------|----------------|
| CP1 | Framework complete | "feat: [component] foundation" | Yes |
| CP2 | First feature works | "feat: [feature] implemented" | Yes |
| CP3 | All features work | "feat: [scope] complete" | Yes |
| CP4 | Tests pass | "test: Gate X validation suite" | Yes |
| CP5 | Gate decision | "release: vX.X-[stage]" | Tagged |

## Definition of Done

### Code Deliverables
- [ ] File/module 1
- [ ] File/module 2

### Test Coverage
- [ ] Unit tests
- [ ] Integration tests
- [ ] Gate acceptance tests

### Documentation
- [ ] Code documentation
- [ ] User documentation
- [ ] Release notes drafted

## Risk Register

| Risk | Mitigation | Priority | Checkpoint |
|------|------------|----------|------------|
| [Risk] | [How to handle] | High/Med/Low | CP[X] |

## Not In Scope (Explicitly Deferred)
- Item 1 (reason)
- Item 2 (reason)

## Post-Sprint

### On Success (Go)
1. Tag release
2. Deploy to [targets]
3. Begin next sprint

### On Failure (No-Go)
1. Document failures at checkpoint
2. Rollback to last good checkpoint
3. Revise scope/criteria
4. Re-run with fixes

## Health Checks

```bash
# Quick health check after each checkpoint
python3 scripts/health_check.py

# Full validation before gate decision
python3 scripts/gate_[X]_validation.py
```

## Notes
- Include lessons from previous sprints
- Document any scope adjustments in real-time
- Update checkpoints if plan changes

---

*Sprint commitment: [One line summary of what we're delivering]*