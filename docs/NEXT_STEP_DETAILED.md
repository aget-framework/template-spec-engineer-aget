# Next Step: Template System Update for Include Architecture

**Timeline**: Day 1-2 of Week 1 (Sept 25-26)
**Priority**: Critical Path
**Dependencies**: Include pattern validation complete ✅

## Objective

Update the template system to support the include architecture with procedural instructions that work with AI agents.

## Detailed Task Breakdown

### Task 1: Create Master AGENTS_AGET.md Template (2 hours)

#### 1.1 Create Base Template
**File**: `templates/AGENTS_AGET.md`

```markdown
# AGET Standard Protocols v2.0.0

**Framework File** - Maintained by AGET, not project-specific
**Version**: 2.0.0
**Updated**: 2025-09-25

## Session Management Protocols
[Standard wake up, wind down, sign off protocols]

## Housekeeping Protocols
[Tidy up, check docs, health check, introspection]

## AGET Commands
[Evolution, extract, apply patterns]

## Directory Structure
[Standard directory explanations]
```

#### 1.2 Add Version Tracking
- Add version header: `# AGET Standard Protocols v2.0.0`
- Add update date: `**Updated**: YYYY-MM-DD`
- Add compatibility notes: `**Compatible with**: AGET v2.0+`

#### 1.3 Test Procedural Instructions
- Verify "Step 1, Step 2" format throughout
- Ensure imperative language used
- Add verification checklists

### Task 2: Update AGENTS.md Templates (3 hours)

#### 2.1 Create Template Variants

**For each template type** (minimal, standard, advanced, agent, tool, hybrid):

1. **Update Header Section**:
```markdown
# Agent Configuration - {Project Type}

## 🚨 INITIALIZATION PROCEDURE (REQUIRED)
**Step 1:** Check if `AGENTS_AGET.md` exists in this directory
**Step 2:** If it exists, READ IT IMMEDIATELY for protocol definitions
**Step 3:** Use protocols from AGENTS_AGET.md for all session/housekeeping commands

<!-- aget:include AGENTS_AGET.md -->
```

2. **Add Quick Reference Section**:
```markdown
## Quick Command Reference
**If user says "hey" or "wake up":**
1. First read AGENTS_AGET.md if not already read
2. Execute the Wake Up Protocol from that file
3. Include project status below
```

3. **Add Bottom Verification**:
```markdown
## ⚠️ Protocol File Verification
Before executing ANY command, ensure you have read:
✅ AGENTS.md (this file) - Project configuration
✅ AGENTS_AGET.md - Standard AGET protocols
```

#### 2.2 Template-Specific Customization

**Minimal Template**:
- Keep project section small
- Focus on essential customization only

**Standard Template**:
- Include common project patterns
- Add typical customization sections

**Advanced Template**:
- Full feature set
- Extended customization options

**Agent Template**:
- Workspace/products structure
- Evolution tracking emphasis

**Tool Template**:
- Library/tool specific sections
- API documentation pointers

**Hybrid Template**:
- Both agent and tool features
- Flexible structure

### Task 3: Implement Init Command Changes (3 hours)

#### 3.1 Add --separate Flag Support

**File**: `aget/config/commands/init.py`

```python
def add_arguments(self, parser):
    parser.add_argument('--separate', action='store_true',
                       help='Create separate AGENTS_AGET.md for protocols')
    parser.add_argument('--merged', action='store_true',
                       help='Use merged single-file approach (legacy)')
```

#### 3.2 File Creation Logic

```python
def execute(self, args):
    if args.separate or self.should_use_separate(args):
        # Create two files
        self.create_agents_md(project_path, template, separate=True)
        self.create_agents_aget_md(project_path)
    else:
        # Legacy merged approach
        self.create_merged_agents_md(project_path, template)

    # Always create CLAUDE.md symlink
    self.create_claude_symlink(project_path)
```

#### 3.3 Auto-Detection Logic

```python
def should_use_separate(self, args):
    """Determine if we should use separate files."""
    # Check if AGENTS_AGET.md already exists
    if (args.project_path / "AGENTS_AGET.md").exists():
        return True

    # Check template preference
    if args.template in ['agent', 'hybrid']:
        return True  # These benefit most from separation

    # Default to merged for backward compatibility
    return False
```

### Task 4: Create Test Suite (2 hours)

#### 4.1 Test File Creation

```python
def test_separate_flag_creates_two_files():
    """Test that --separate creates both files."""

def test_agents_md_has_procedural_instructions():
    """Verify procedural language in AGENTS.md."""

def test_agents_aget_has_protocols():
    """Verify AGENTS_AGET.md contains protocols."""

def test_backward_compatibility():
    """Ensure merged mode still works."""
```

#### 4.2 Content Validation Tests

```python
def test_procedural_instructions_present():
    """Check for Step 1, Step 2 format."""
    content = read_file("AGENTS.md")
    assert "Step 1:" in content
    assert "Step 2:" in content
    assert "READ IT IMMEDIATELY" in content

def test_include_directive_present():
    """Check for include comment."""
    content = read_file("AGENTS.md")
    assert "<!-- aget:include AGENTS_AGET.md -->" in content
```

### Task 5: Migration Helper (1 hour)

#### 5.1 Create Migration Command

```python
class MigrateToSeparate:
    """Migrate existing merged AGENTS.md to separate files."""

    def extract_aget_sections(self, content):
        """Extract standard AGET sections."""
        # Identify protocol sections
        # Move to AGENTS_AGET.md
        # Leave custom in AGENTS.md

    def add_procedural_instructions(self, content):
        """Add Step 1, 2, 3 instructions."""
        # Insert at top of file
        # Add quick reference
        # Add bottom verification
```

### Task 6: Documentation (1 hour)

#### 6.1 Update Template Documentation

**File**: `templates/README.md`
- Explain separate vs merged approach
- Show example of both files
- Explain procedural instructions

#### 6.2 Create Migration Instructions

**File**: `docs/MIGRATE_TO_SEPARATE.md`
- Step-by-step migration guide
- Before/after examples
- Validation checklist

## Success Criteria

### Functional Requirements
- [ ] --separate flag creates two files
- [ ] Both files have correct content
- [ ] Procedural instructions present
- [ ] All template types updated
- [ ] Tests passing

### Quality Checks
- [ ] Instructions use imperative language
- [ ] Step format consistent
- [ ] Version tracking included
- [ ] Documentation clear

### Validation
- [ ] Test with fresh project
- [ ] Test with existing project migration
- [ ] Test with Claude Code
- [ ] Test with at least one other AI

## Time Estimate

**Total**: 12 hours over 2 days

Day 1 (6 hours):
- Morning: Create templates (3h)
- Afternoon: Update init command (3h)

Day 2 (6 hours):
- Morning: Testing and validation (3h)
- Afternoon: Documentation and migration helper (3h)

## Dependencies

### Required Before Starting
- ✅ Include pattern validated
- ✅ Procedural instruction format confirmed
- ✅ Decision documented (ADR-003)

### Required for Next Step
- All templates updated
- Init command working
- Basic tests passing
- Documentation drafted

## Risk Factors

1. **Template complexity** - Keep first version simple
2. **Backward compatibility** - Test thoroughly
3. **instruction clarity** - Get feedback early
4. **Time constraints** - Focus on core functionality first

---
*This detailed plan ensures we properly implement the include architecture discovery into v2.0's template system.*