# AGET v2.0 Comprehensive Transition Test Suite

## Test Philosophy
Since we're early in Day 2 and have time, we should thoroughly test state transitions to ensure robustness before declaring victory.

## Test Categories

### 1. Basic Transitions (✅ Completed)
- [x] wake → housekeeping → doc-check → wind-down → sign-off

### 2. Multiple Session Cycles
Test session counting and state persistence:
```bash
# Cycle 1
wake up
housekeeping
wind down

# Cycle 2 (immediately after)
wake up  # Should show session #3
sanity check
sign off

# Cycle 3 (new terminal)
wake up  # Should show session #4
documentation check
wind down
```

### 3. Interrupted Sessions
Test recovery from incomplete sessions:
```bash
# Test A: Wake without wind-down
wake up
# Kill terminal / close without wind-down
# Open new terminal
wake up  # Should handle orphaned session

# Test B: Double wake
wake up
wake up  # Should handle already-awake state

# Test C: Wind-down without wake
wind down  # Should handle no active session
```

### 4. Rapid Transitions
Test quick succession commands:
```bash
wake up
sign off  # Immediate sign-off
wake up
wind down
wake up
housekeeping
sign off
```

### 5. Edge Cases
```bash
# Empty repository
cd /tmp/empty-project
wake up  # Should handle no git repo

# Corrupted state during session
wake up
echo "corrupt" > .session_state.json
wind down  # Should recover

# Multiple state files
wake up
cp .session_state.json .session_state.backup.json
wind down
wake up  # Should use correct file
```

### 6. Cross-Project Transitions
```bash
# Project A
cd ~/github/spotify-aget
wake up
housekeeping

# Switch without wind-down
cd ~/github/llm-judge-aget
wake up  # Should handle project switch
wind down

# Return to first
cd ~/github/spotify-aget
wake up  # Should resume correctly
```

### 7. Pattern vs Script Mixing
```bash
# Use script
python3 scripts/aget_session_protocol.py wake

# Use pattern directly
python3 -c "import sys; sys.path.insert(0, 'patterns'); from session.wind_down import apply_pattern; apply_pattern('.')"

# Use script again
python3 scripts/aget_session_protocol.py wake  # Should handle mixed usage
```

### 8. Stress Test
```bash
# 10 rapid cycles
for i in {1..10}; do
    python3 scripts/aget_session_protocol.py wake
    echo "Test file $i" > test_$i.txt
    python3 scripts/aget_session_protocol.py wind-down
done

# Check session count = 10+previous
python3 scripts/aget_session_protocol.py wake
```

### 9. Concurrent Sessions
```bash
# Terminal 1
cd ~/github/spotify-aget
wake up

# Terminal 2 (same project)
cd ~/github/spotify-aget
wake up  # Should detect active session

# Terminal 1
wind down

# Terminal 2
wind down  # Should handle already-ended session
```

### 10. Migration Scenarios
```bash
# Old state file
echo '{"session_count": 100}' > .session_state.json
wake up  # Should preserve count, add missing keys

# Very old format
echo '{"last_wake": "2024-01-01"}' > .session_state.json
wake up  # Should upgrade gracefully

# Future format (extra keys)
echo '{"session_count": 5, "future_feature": "test", "last_wake": null}' > .session_state.json
wake up  # Should preserve unknown keys
```

## Expected Behaviors

### ✅ PASS Criteria
- Session count increments correctly
- State persists between sessions
- Handles corrupted files gracefully
- No data loss on upgrade
- Project isolation maintained
- Recovery from any state

### ❌ FAIL Criteria
- KeyError or crashes
- Session count resets
- State file corruption
- Data loss
- Hung processes
- Inconsistent behavior

## Test Execution Plan

### Phase 1: Quick Smoke Tests (5 min)
Run tests 1-3 to verify basic functionality

### Phase 2: Thorough Testing (15 min)
Run tests 4-7 for state management validation

### Phase 3: Stress Testing (10 min)
Run tests 8-10 for robustness validation

### Phase 4: Multi-Project (10 min)
Test with llm-judge-aget and planner-aget

## Results Tracking

| Test | spotify-aget | llm-judge-aget | planner-aget | Notes |
|------|-------------|----------------|--------------|-------|
| 1. Basic | ✅ | - | - | Completed |
| 2. Multi-cycle | - | - | - | |
| 3. Interrupted | - | - | - | |
| 4. Rapid | - | - | - | |
| 5. Edge cases | - | - | - | |
| 6. Cross-project | - | - | - | |
| 7. Mix mode | - | - | - | |
| 8. Stress | - | - | - | |
| 9. Concurrent | - | - | - | |
| 10. Migration | - | - | - | |

## Risk Assessment

**High Priority** (Must Pass):
- Tests 1-3: Basic functionality
- Test 10: Migration compatibility

**Medium Priority** (Should Pass):
- Tests 4-6: State management
- Test 7: Mixed usage

**Low Priority** (Nice to Pass):
- Tests 8-9: Stress conditions

---
*Created: September 25, 2025*
*Purpose: Ensure AGET v2.0 is production-ready*