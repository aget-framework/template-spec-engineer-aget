# Sprint Alignment Checklist

Use this checklist at sprint start and end to maintain alignment across sessions.

## Sprint Start Checklist

### 1. Previous Sprint Reality Check
- [ ] Read previous sprint retrospective
- [ ] Compare PLANNED vs ACTUAL deliverables
- [ ] Note any deferred work or technical debt
- [ ] Check if gate criteria were modified

### 2. Current State Verification
- [ ] Run `git log --oneline -5` to see recent commits
- [ ] Check latest release tag and version
- [ ] Verify which commands/features actually work
- [ ] Test the current deployment

### 3. Documentation Sync
- [ ] Update/archive outdated planning docs
- [ ] Ensure version numbers are consistent
- [ ] Remove or mark deprecated checklists
- [ ] Create CURRENT_SPRINT.md if needed

### 4. Sprint Definition Clarity
- [ ] Explicit starting point documented
- [ ] Clear success criteria (no ambiguity)
- [ ] "Not in scope" section included
- [ ] Risk register updated

## Sprint End Checklist

### 1. Actual vs Planned
- [ ] Document what was actually delivered
- [ ] Note any criteria that were relaxed/changed
- [ ] List deferred items explicitly
- [ ] Update technical debt log

### 2. Handoff Documentation
- [ ] Create/update SPRINT_HANDOFF.md
- [ ] Link to relevant commits
- [ ] Note key decisions made
- [ ] Highlight surprises or changes

### 3. Clean Up Conflicts
- [ ] Archive completed sprint plans
- [ ] Update or remove outdated docs
- [ ] Ensure single source of truth
- [ ] Tag release if applicable

### 4. Next Sprint Prep
- [ ] Clear starting point for next sprint
- [ ] Unresolved items documented
- [ ] Dependencies identified
- [ ] Resource allocation noted

## Red Flags to Catch

⚠️ **Version Confusion**: Multiple version numbers in docs (v1.0 vs v2.0)
⚠️ **Criteria Mismatch**: Gate criteria don't match implementation
⚠️ **Orphaned Docs**: Old checklists that no longer apply
⚠️ **Hidden Decisions**: Changes made but not documented
⚠️ **Placeholder Confusion**: Unclear what's real vs placeholder

## Example Alignment Statement

```markdown
## Sprint X Alignment
- Previous Outcome: [Gate Y passed with modifications: ...]
- Current State: [2 commands working, 3 placeholders, deployed on ...]
- This Sprint: [Deliver Z patterns for Gate Y+1]
- Success = [All criteria met without modification]
- Not Doing: [Migration tools, external docs, ...]
```

---

*Purpose: Prevent the "what were we doing?" confusion between sprint sessions*