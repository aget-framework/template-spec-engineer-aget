# Sprint Workflow & Decision Points

**Purpose**: Define clear workflow and decision points for v2 development sprints
**Created**: 2025-09-22
**Sprint**: 001 (Gate 1)

## Roles & Responsibilities

### Your Role (Gabor - Architect/Product Owner)
- **Guide**: Set direction and priorities
- **Clarify**: Answer questions about requirements
- **Review**: Approve architecture and major decisions
- **Decide**: Go/No-Go at gates
- **Control**: When to save, pause, or continue

### Agent Role (CCB - Builder/Implementer)
- **Implement**: Build according to specifications
- **Report**: Show progress and results
- **Ask**: Seek clarification when uncertain
- **Pause**: Stop at decision points for input
- **Document**: Record decisions and progress

## Step Workflow

```
┌─────────────────────────────────────┐
│         Step Begins                  │
├─────────────────────────────────────┤
│ Agent: Updates todo to "in_progress" │
│ Agent: Implements step               │
│ Agent: Shows results/output          │
├─────────────────────────────────────┤
│      DECISION POINT (Pause)          │
├─────────────────────────────────────┤
│ You choose:                          │
│  • "continue" → Next step            │
│  • "review" → Examine details        │
│  • "adjust" → Modify approach        │
│  • "save work" → Git commit          │
│  • "wind down" → Full session save   │
└─────────────────────────────────────┘
```

## Sprint 001 Decision Points

### 🔷 Sprint Start: Pre-Work Checkpoint
**Before Step 1 begins**
**Agent delivers**: Clean starting point with all planning complete
**You decide**:
- Create checkpoint commit?
- Tag as sprint start?
- **Recommended**: "save work" (clean rollback point)

### 🔷 Step 1 Complete: Scanner Baseline
**Agent delivers**: `.aget/v2-baseline.json` with 3 projects analyzed
**You decide**:
- Review scan results?
- Add more projects?
- Adjust migration priority?
- **Default**: "continue" to Step 2

### 🔷 Step 2 Complete: Core Architecture
**Agent delivers**: BaseCommand with three-tier degradation
**You decide**: ⚠️ **CRITICAL REVIEW POINT**
- Architecture approval (this locks in v2 foundation)
- Test the pattern?
- Review code structure?
- **Recommended**: "save work" (architecture milestone)

### 🔷 Step 3 Complete: First Command
**Agent delivers**: Working `aget init` command
**You decide**:
- Test performance (<2 seconds)?
- Try on test project?
- Review three tiers?
- **Default**: "continue" to Step 4

### 🔷 Step 4 Complete: Backup Mechanism
**Agent delivers**: RKB agent protection ready
**You decide**: ✅ **VALUE DELIVERED**
- Test backup/restore?
- Deploy to RKB immediately?
- Take break here?
- **Recommended**: "save work" or "wind down" (natural pause point)

### 🔷 Step 5 Complete: Gate 1 Validation
**Agent delivers**: Test results and Go/No-Go recommendation
**You decide**: 🚀 **MAJOR MILESTONE**
- Review all criteria
- Make Go/No-Go decision
- Tag v2.0-alpha?
- **Required**: "wind down" (gate completion)

## Session Commands Reference

### During Development
- **"continue"**: Proceed to next step/task
- **"review"**: Examine current work in detail
- **"adjust"**: Change approach or requirements
- **"pause"**: Take a break without saving

### Saving Work
- **"save work"**: Create git commit with progress
- **"wind down"**: Full save (commit + session notes + cleanup)
- **"sign off"**: Quick save and end session

### Emergency
- **"stop"**: Halt current operation
- **"rollback"**: Undo recent changes
- **"sanity check"**: Run diagnostics

## Commit Points Strategy

### Automatic Commits (Agent-initiated)
None - agent always waits for your instruction

### Recommended Commit Points
1. After Step 2 (architecture) - "save work"
2. After Step 4 (backup) - "save work"
3. After Step 5 (gate) - "wind down"

### Optional Commit Points
- After any step if you need to pause
- Before any risky operation
- When switching context

## Communication Patterns

### Agent Should Always
- Pause after completing each step
- Show clear results/outputs
- Indicate what was built/changed
- Wait for your decision

### Agent Should Never
- Auto-continue to next step
- Make architectural decisions alone
- Commit without permission
- Skip decision points

## Risk-Based Pausing

### Must Pause (High Risk)
- Step 2: Architecture (lock-in risk)
- Step 5: Gate decision (milestone)

### Should Pause (Medium Risk)
- Step 4: Backup complete (value delivered)

### Can Continue (Low Risk)
- Step 1: Scanner (just analysis)
- Step 3: First command (if Step 2 approved)

## Example Session Flow

```
You: "Let's begin Sprint 1"
Agent: *starts Step 1*
Agent: "Scanner complete. Found X patterns in 3 projects. Continue?"
You: "continue"
Agent: *starts Step 2*
Agent: "Core architecture built. CRITICAL REVIEW POINT. Review?"
You: "review"
Agent: *shows architecture details*
You: "looks good, save work"
Agent: *commits with message*
You: "continue"
Agent: *proceeds to Step 3*
...
```

## Questions to Answer at Each Pause

1. **Is the output what you expected?**
2. **Should we adjust before continuing?**
3. **Is this a good save point?**
4. **Do you need a break?**

---

*This workflow ensures you maintain control while we maintain momentum.*