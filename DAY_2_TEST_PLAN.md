# Day 2 Test Plan - Primary Test with spotify-aget
**Date**: September 26, 2025
**Duration**: 1.5 hours total
**Risk Level**: Medium
**Prerequisites**: Day 1 completed successfully

## Pre-Start Checklist (9:45 AM - 10:00 AM)

Verify Day 1 completion:

```bash
# Quick verification that we're ready
cd ~/github

echo "🔍 Pre-flight Check:"
echo "=================="

# Check AGET is still working
cd aget-cli-agent-template
python3 -m aget list > /dev/null 2>&1 && echo "✅ AGET CLI working" || echo "❌ AGET CLI issue"

# Check for backups
cd ~/github
[ -d "backups/20250925" ] && echo "✅ Backups present" || echo "❌ No backups found"

# Check for test subject
if [ -d "spotify-aget" ]; then
    echo "✅ spotify-aget exists"
elif [ -d "agent-music" ]; then
    echo "✅ agent-music exists (will rename)"
else
    echo "❌ Neither spotify-aget nor agent-music found"
fi
```

## Morning Session (10:00 AM - 10:45 AM)

### Task 2.1: Prepare spotify-aget Repository (15 minutes)

Handle the agent-music → spotify-aget transition:

```bash
cd ~/github

# Scenario A: If agent-music exists, rename it
if [ -d "agent-music" ] && [ ! -d "spotify-aget" ]; then
    echo "📝 Renaming agent-music to spotify-aget..."

    # Rename directory
    mv agent-music spotify-aget
    cd spotify-aget

    # Update git remote if needed (optional - can skip for local testing)
    git remote -v

    # Document current state
    echo -e "\n📊 Current State:"
    echo "================"

    # Check for existing agent configurations
    for file in CLAUDE.md AGENTS.md .cursorrules .aider.conf.yml; do
        if [ -f "$file" ]; then
            echo "Found: $file ($(wc -l < $file) lines)"
            # Show first few lines to understand customization level
            echo "  Preview:"
            head -3 "$file" | sed 's/^/    /'
        fi
    done

    # Check git status
    echo -e "\n📝 Git Status:"
    git status --short

    # List main directories
    echo -e "\n📁 Project Structure:"
    ls -la | grep "^d" | awk '{print $NF}'

# Scenario B: If spotify-aget already exists
elif [ -d "spotify-aget" ]; then
    echo "✅ spotify-aget already exists"
    cd spotify-aget

    # Check if AGET was already applied
    if [ -f "AGENTS.md" ] && [ -d "patterns" ]; then
        echo "⚠️ AGET may already be installed"
        echo "Consider using backup or documenting current state"
    fi

else
    echo "❌ ERROR: No spotify-aget or agent-music found"
    echo "Cannot proceed with Day 2 testing"
    exit 1
fi
```

### Task 2.2: Apply AGET v2 Migration (30 minutes)

Apply AGET with the agent template:

```bash
cd ~/github/spotify-aget

# Save pre-migration state
echo "📸 Capturing pre-migration state..."
ls -la > pre_migration_files.txt
git diff > pre_migration_changes.diff 2>/dev/null || true

# Decision point: Check for heavy customization
if [ -f "CLAUDE.md" ] && [ $(wc -l < CLAUDE.md) -gt 50 ]; then
    echo "⚠️ Found customized CLAUDE.md with $(wc -l < CLAUDE.md) lines"
    echo "Recommendation: Use --preserve-custom flag"

    # Option A: Preserve customizations (if migrate command exists)
    # python3 ~/github/aget-cli-agent-template/aget/cli.py migrate . --preserve-custom

    # Option B: Fresh install with manual merge
    echo "Proceeding with fresh install - will need manual merge"
fi

# Apply AGET v2 with agent template
echo "🚀 Applying AGET v2..."
python3 ~/github/aget-cli-agent-template/installer/install.py . \
    --template agent \
    --with-patterns \
    --force  # Use --force if re-running

# Verify installation
echo -e "\n✅ Post-Installation Check:"
echo "=========================="

# Check key files were created
for file in AGENTS.md scripts/aget_session_protocol.py patterns/session/wake.py; do
    if [ -f "$file" ]; then
        echo "✅ Created: $file"
    else
        echo "❌ Missing: $file"
    fi
done

# Check symlink
if [ -L "CLAUDE.md" ]; then
    echo "✅ CLAUDE.md → AGENTS.md symlink created"
else
    echo "⚠️ CLAUDE.md is not a symlink"
fi

# List new directories
echo -e "\n📁 New Structure:"
ls -la | grep -E "workspace|products|patterns|scripts" || echo "Standard directories not found"
```

## Afternoon Session (4:00 PM - 4:45 PM)

### Task 2.3: Test Core Patterns (30 minutes)

Systematically test each core pattern:

```bash
cd ~/github/spotify-aget

echo "🧪 Testing Core Patterns"
echo "======================="

# Test 1: Wake Protocol
echo -e "\n1️⃣ Testing Wake Protocol..."
START_TIME=$(date +%s)
python3 scripts/aget_session_protocol.py wake
END_TIME=$(date +%s)
DURATION=$((END_TIME - START_TIME))

if [ $? -eq 0 ]; then
    echo "✅ Wake protocol: PASS (${DURATION}s)"
else
    echo "❌ Wake protocol: FAIL"
fi

# Test 2: Wind-Down Protocol
echo -e "\n2️⃣ Testing Wind-Down Protocol..."
# Create a small change to test commit
echo "# Test change for wind-down" >> TEST_FILE.md
python3 scripts/aget_session_protocol.py wind-down

if [ $? -eq 0 ]; then
    echo "✅ Wind-down protocol: PASS"
    # Check if session notes were created
    ls -la SESSION_NOTES/$(date +%Y-%m-%d)/ 2>/dev/null && echo "  ✓ Session notes created"
else
    echo "❌ Wind-down protocol: FAIL"
fi

# Test 3: Housekeeping (Dry Run)
echo -e "\n3️⃣ Testing Housekeeping Protocol..."
python3 scripts/aget_housekeeping_protocol.py housekeeping --dry-run

if [ $? -eq 0 ]; then
    echo "✅ Housekeeping: PASS"
else
    echo "❌ Housekeeping: FAIL"
fi

# Test 4: Documentation Check
echo -e "\n4️⃣ Testing Documentation Check..."
python3 scripts/aget_housekeeping_protocol.py documentation-check

if [ $? -eq 0 ]; then
    echo "✅ Documentation check: PASS"
else
    echo "❌ Documentation check: FAIL"
fi

# Test 5: Pattern Application
echo -e "\n5️⃣ Testing Pattern Application..."
python3 -m aget list
python3 -m aget apply session/wake --dry-run 2>/dev/null || echo "  (dry-run not supported)"

# Test 6: Performance Check
echo -e "\n6️⃣ Performance Validation..."
START_TIME=$(date +%s)
python3 -m aget list > /dev/null
END_TIME=$(date +%s)
DURATION=$((END_TIME - START_TIME))

if [ $DURATION -lt 2 ]; then
    echo "✅ Performance: PASS (${DURATION}s < 2s target)"
else
    echo "⚠️ Performance: SLOW (${DURATION}s > 2s target)"
fi

# Test 7: Original Functionality
echo -e "\n7️⃣ Testing Original Functionality..."
# Test spotify-aget specific scripts still work
if [ -f "analyze_playlists.py" ]; then
    python3 analyze_playlists.py --help > /dev/null 2>&1 && echo "✅ Original scripts: WORKING" || echo "⚠️ Original scripts: NEED REVIEW"
else
    echo "ℹ️ No analyze_playlists.py found"
fi
```

### Task 2.4: Create Migration Report (15 minutes)

Document the migration results:

```bash
cd ~/github/spotify-aget

# Calculate migration time (rough estimate)
MIGRATION_START="10:15"
MIGRATION_END="10:45"

# Count working patterns
PATTERNS_WORKING=$(python3 -m aget list | grep -c "^  " || echo "0")

# Create detailed report
cat > MIGRATION_REPORT.md << EOF
# spotify-aget Migration Report
**Date**: September 26, 2025
**AGET Version**: v2.0.0-alpha
**Template Used**: agent

## Summary
- **Migration Duration**: ~30 minutes
- **Migration Method**: Fresh install with --template agent --with-patterns
- **Result**: [SUCCESS/PARTIAL/FAILURE]

## Test Results

### Core Patterns (Required)
- [x] Wake protocol: PASS
- [ ] Wind-down protocol: [PASS/FAIL]
- [ ] Sign-off protocol: [NOT TESTED]

### Additional Patterns
- [ ] Housekeeping: [PASS/FAIL]
- [ ] Documentation check: [PASS/FAIL]
- [ ] Pattern listing: [PASS/FAIL]

### Performance
- Command response time: [X]s (target: <2s)
- Memory usage: [Not measured]
- Disk usage: $(du -sh . | cut -f1)

## Compatibility

### File Structure
- AGENTS.md created: [YES/NO]
- CLAUDE.md symlink: [YES/NO]
- Patterns directory: [YES/NO]
- Scripts directory: [YES/NO]
- workspace directory: [YES/NO]
- products directory: [YES/NO]

### Original Functionality
- Existing scripts working: [YES/NO/PARTIAL]
- Custom configurations preserved: [YES/NO/NA]
- Git history maintained: [YES/NO]
- No data loss: [YES/NO]

## Issues Encountered

### Critical Issues
$(if [ -f "CRITICAL_ISSUES.txt" ]; then cat CRITICAL_ISSUES.txt; else echo "None"; fi)

### Minor Issues
1. [Issue description or "None"]
2. [Issue description or "None"]

### Warnings
- [Warning or "None"]

## AI Tool Compatibility Test

### Claude Code Test
\`\`\`
User: wake up
Expected: AI runs wake protocol and shows status
Result: [PASS/FAIL/NOT TESTED]
\`\`\`

### Generic Test
\`\`\`
File recognized: AGENTS.md [YES/NO]
Commands discovered: [YES/NO]
Patterns accessible: [YES/NO]
\`\`\`

## Customization Preservation

### Before Migration
- CLAUDE.md lines: $([ -f "pre_migration_files.txt" ] && grep -c "CLAUDE.md" pre_migration_files.txt || echo "N/A")
- Custom patterns: [NUMBER]
- Special configs: [LIST]

### After Migration
- Custom content preserved: [YES/NO/PARTIAL]
- Manual merge needed: [YES/NO]
- Conflicts resolved: [YES/NO/NA]

## Recommendations

### For This Project
1. [Specific recommendation]
2. [Specific recommendation]

### For AGET v2
1. [Improvement suggestion]
2. [Improvement suggestion]

## Next Steps
- [ ] Test with actual AI coding assistant
- [ ] Resolve any merge conflicts
- [ ] Document custom pattern requirements
- [ ] Proceed to Day 3 testing with other projects

## Overall Assessment

**Migration Success Rate**: [X]%
**Ready for Production**: [YES/NO/NEEDS WORK]
**Recommendation**: [PROCEED/FIX AND RETRY/ROLLBACK]

---
*Report generated: $(date)*
*Tester: [Your name/ID]*
EOF

echo "✅ Migration report created: MIGRATION_REPORT.md"
```

## Day 2 Completion Checklist

### Morning Session ✓
- [ ] spotify-aget repository prepared (renamed or verified)
- [ ] Pre-migration state documented
- [ ] AGET v2 installed successfully
- [ ] Key files created (AGENTS.md, patterns/, scripts/)

### Afternoon Session ✓
- [ ] Wake protocol tested
- [ ] Wind-down protocol tested
- [ ] At least 3 additional patterns tested
- [ ] Performance validated (<2s)
- [ ] Original functionality verified
- [ ] Migration report completed

### Critical Success Criteria
- [ ] ✅ No data loss
- [ ] ✅ Core patterns working
- [ ] ✅ AI tools can read AGENTS.md
- [ ] ✅ Original functionality preserved

## End of Day 2 Status

```markdown
## Day 2 Status - September 26, 2025

### ✅ Completed
- spotify-aget migration: [SUCCESS/PARTIAL/FAILURE]
- Patterns working: [X]/8
- Performance target met: [YES/NO]
- Migration report created: YES

### 🐛 Issues Found
- Critical: [Number] issues
- Minor: [Number] issues
- [Top issue description]

### 📊 Metrics
- Migration time: ~30 minutes
- Setup time: [X] seconds (target: <60s)
- Command time: [X] seconds (target: <2s)
- Success rate: [X]%

### 📋 Ready for Day 3
- [ ] spotify-aget stable
- [ ] No blocking issues
- [ ] Test environments ready
- [ ] Lessons learned documented

### 🚦 Go/No-Go Status: [GREEN/YELLOW/RED]
- GREEN = Continue to Day 3
- YELLOW = Fix minor issues, then continue
- RED = Major issues, consider delay

### Key Learning for Day 3:
[Main insight that will help with next projects]
```

## Rollback Instructions (If Critical Issues)

If migration causes critical problems:

```bash
cd ~/github

# Option 1: Restore from Day 1 backup
rm -rf spotify-aget
cp -r backups/20250925/agent-music-backup spotify-aget
cd spotify-aget
mv spotify-aget agent-music  # Restore original name if needed

# Option 2: Selective rollback (keep some changes)
cd spotify-aget
git diff > failed_migration.patch
git checkout -- .
# Apply selective changes from patch

# Document failure
cat >> DAY_2_BLOCKER.md << EOF
Blocker Found: $(date)
Project: spotify-aget
Issue: [Description]
Impact: [Critical/High/Medium]
Attempted fixes: [What was tried]
Decision: [Rollback/Postpone/Continue with workaround]
EOF

echo "❌ Day 2: Migration rolled back due to critical issues"
echo "See DAY_2_BLOCKER.md for details"
```

## Success Path to Day 3

If Day 2 successful:

```bash
# Commit successful state
cd ~/github/spotify-aget
git add -A
git commit -m "test: Successful AGET v2 migration

- Applied agent template with patterns
- All core patterns working
- No data loss
- Ready for production evaluation"

# Prepare for Day 3
echo "✅ Day 2 Complete - spotify-aget successfully migrated"
echo "Ready to test llm-judge-aget and planner-aget tomorrow"
```

---
*Day 2 Plan - Primary Migration Test*
*Focus on spotify-aget as the most complex test case*