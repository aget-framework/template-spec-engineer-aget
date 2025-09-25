# AGET Functional Requirements

> What the AGET system must do

## Session Management Requirements

### FR-001: Initialize Session [MUST HAVE]
**Description**: System must initialize a development session
**Trigger**: User says "wake up", "wake", or "hey"
**Behavior**:
- Display current working directory
- Show git repository status
- List available patterns
- Display session number
- Show time since last session
**Success Criteria**:
- Completes in <2 seconds
- Creates .session_state.json if not exists
- Increments session counter

### FR-002: Preserve Session State [MUST HAVE]
**Description**: System must save work and session state
**Trigger**: User says "wind down", "save work"
**Behavior**:
- Commit uncommitted changes with descriptive message
- Create session notes with timestamp
- Run tests if test command configured
- Update session state file
**Success Criteria**:
- All changes committed to git
- Session notes created in SESSION_NOTES/
- State file updated with timestamp

### FR-003: Quick Save [MUST HAVE]
**Description**: System must provide quick save and sync
**Trigger**: User says "sign off", "sync up", "all done"
**Behavior**:
- Quick commit with timestamp
- Push to remote if available
- Update session state
**Success Criteria**:
- Changes committed within 5 seconds
- Clear success/failure message

## Pattern Management Requirements

### FR-004: Apply Patterns [MUST HAVE]
**Description**: System must apply reusable workflow patterns
**Command**: `aget apply <pattern_id>`
**Behavior**:
- Locate pattern by ID
- Execute pattern's apply_pattern() function
- Report success/failure
- Show files modified
**Success Criteria**:
- Pattern found and executed
- Clear status returned
- No uncaught exceptions

### FR-005: List Available Patterns [MUST HAVE]
**Description**: System must list all available patterns
**Command**: `aget list`
**Behavior**:
- Scan patterns directory
- Group by category
- Show pattern ID and description
**Success Criteria**:
- All patterns discovered
- Organized by category
- Human-readable output

### FR-006: Create New Pattern [SHOULD HAVE]
**Description**: System must scaffold new patterns
**Command**: `aget pattern create <category>/<name>`
**Behavior**:
- Create pattern file with template
- Create test file
- Update pattern registry
**Success Criteria**:
- Valid Python file created
- Test file created
- Pattern appears in list

## Project Initialization Requirements

### FR-007: Initialize New Project [MUST HAVE]
**Description**: System must set up AGET in new project
**Command**: `aget init [--template <name>]`
**Behavior**:
- Create AGENTS.md configuration
- Create necessary directories
- Copy protocol scripts
- Initialize .aget/ metadata
**Success Criteria**:
- Project becomes agent-ready
- All protocols functional
- Template correctly applied

### FR-008: Template Selection [MUST HAVE]
**Description**: System must support multiple templates
**Options**: minimal, standard, agent, tool, hybrid
**Behavior**:
- Apply selected template
- Create template-specific structure
- Configure appropriate patterns
**Success Criteria**:
- Correct files created
- Template features available
- Upgrade path preserved

### FR-009: Migrate Existing Project [SHOULD HAVE]
**Description**: System must migrate existing projects
**Command**: `aget migrate <path>`
**Behavior**:
- Detect existing structure
- Preserve custom content
- Merge with AGET configuration
- Create backup
**Success Criteria**:
- No data loss
- Existing functionality preserved
- AGET features added

## Code Extraction Requirements

### FR-010: Extract to Products [MUST HAVE]
**Description**: System must extract code to reusable products
**Command**: `aget extract --from <source> --to products/ --name <name>`
**Behavior**:
- Copy source files/directories
- Generate setup.py
- Create README.md
- Sanitize secrets
- Handle dependencies
**Success Criteria**:
- Standalone package created
- No secrets exposed
- Dependencies documented

### FR-011: Directory Extraction [MUST HAVE]
**Description**: System must extract entire directories
**Behavior**:
- Preserve directory structure
- Handle nested directories
- Skip excluded patterns
- Generate appropriate metadata
**Success Criteria**:
- Structure maintained
- All files included
- Exclusions respected

## Evolution Tracking Requirements

### FR-012: Record Decisions [SHOULD HAVE]
**Description**: System must track significant decisions
**Command**: `aget evolution --type decision "<description>"`
**Behavior**:
- Create timestamped file
- Add to evolution directory
- Include metadata
**Success Criteria**:
- File created with correct format
- Findable via list command
- Preserves history

### FR-013: Record Discoveries [SHOULD HAVE]
**Description**: System must track learnings and insights
**Command**: `aget evolution --type discovery "<description>"`
**Behavior**:
- Create discovery entry
- Tag with metadata
- Link related files
**Success Criteria**:
- Discovery recorded
- Searchable by date
- Context preserved

### FR-014: List Evolution History [SHOULD HAVE]
**Description**: System must show evolution entries
**Command**: `aget evolution --list`
**Behavior**:
- Show recent entries
- Sort by date
- Filter by type
**Success Criteria**:
- Last 10 entries shown
- Chronological order
- Type indicated

## Housekeeping Requirements

### FR-015: Documentation Check [SHOULD HAVE]
**Description**: System must analyze documentation quality
**Trigger**: User says "check docs", "documentation check"
**Behavior**:
- Scan all markdown files
- Check for completeness
- Grade quality (A-F)
- Report issues
**Success Criteria**:
- All docs analyzed
- Grade assigned
- Specific issues listed

### FR-016: Light Cleanup [SHOULD HAVE]
**Description**: System must clean temporary files
**Trigger**: User says "tidy up", "housekeeping"
**Behavior**:
- Remove Python cache
- Clear temporary files
- Clean old logs
- Show what was cleaned
**Success Criteria**:
- Safe cleanup only
- Dry-run by default
- Clear report

### FR-017: Deep Clean [NICE TO HAVE]
**Description**: System must perform deep cleanup
**Trigger**: User says "deep clean", "spring clean"
**Behavior**:
- Archive old sessions
- Remove duplicates
- Consolidate backups
- Compress logs
**Success Criteria**:
- Requires confirmation
- Preserves important data
- Detailed report

## Diagnostic Requirements

### FR-018: System Health Check [MUST HAVE]
**Description**: System must verify environment health
**Trigger**: User says "health check", "sanity check"
**Behavior**:
- Check Python version
- Verify git availability
- Test file permissions
- Validate dependencies
**Success Criteria**:
- Reports OK/DEGRADED/CRITICAL
- Specific issues identified
- Suggests fixes

### FR-019: Emergency Recovery [SHOULD HAVE]
**Description**: System must provide recovery options
**Command**: `aget recover`
**Behavior**:
- Check for corruption
- Restore from backups
- Reset state if needed
- Preserve user data
**Success Criteria**:
- Automated recovery
- Data preservation
- Clear status report

## Configuration Requirements

### FR-020: Include Architecture Support [MUST HAVE]
**Description**: System must support modular includes
**Feature**: `--separate` flag for v2.0+
**Behavior**:
- AGENTS_AGET.md for framework
- AGENTS.md for project
- Include directive support
**Success Criteria**:
- Both files work together
- Updates don't break projects
- Backward compatible

### FR-021: Pattern Bundle Support [SHOULD HAVE]
**Description**: System must apply pattern bundles
**Command**: `aget init --with-patterns`
**Behavior**:
- Initialize project
- Apply default patterns
- Configure protocols
**Success Criteria**:
- One-step setup
- All patterns functional
- <60 second completion

## Rollback Requirements

### FR-022: Configuration Rollback [NICE TO HAVE]
**Description**: System must rollback configurations
**Command**: `aget rollback`
**Behavior**:
- Restore previous configuration
- Preserve current as backup
- Show what changed
**Success Criteria**:
- Previous state restored
- No data loss
- Clear change log

## Performance Requirements

*Note: These are functional requirements about performance features*

### FR-023: Progress Indication [SHOULD HAVE]
**Description**: System must show progress for long operations
**Behavior**:
- Display progress bar or spinner
- Show current step
- Estimate time remaining
**Success Criteria**:
- Updates at least every second
- Accurate progress shown
- Clean terminal output

### FR-024: Batch Operations [NICE TO HAVE]
**Description**: System must support batch pattern application
**Command**: `aget apply pattern1 pattern2 pattern3`
**Behavior**:
- Apply multiple patterns
- Stop on first failure
- Report all results
**Success Criteria**:
- Patterns applied in order
- Clear success/failure for each
- Summary report

---

*These functional requirements define what AGET must do to fulfill its mission.*

*Last Updated: 2025-09-25*
*Version: 1.0.0*
*Status: Template for completion*