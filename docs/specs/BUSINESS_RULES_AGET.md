# AGET Business Rules

> Domain logic and policies that govern AGET's behavior

## Core Framework Rules

### BR-001: Zero External Dependencies
**Rule**: The AGET framework must use only Python standard library
**Rationale**: Ensures universal compatibility without version conflicts
**Implementation**: No third-party imports in core framework
**Enforcement**: Import scanner in CI/CD pipeline
**Exceptions**: None

### BR-002: Pattern Isolation
**Rule**: Patterns must not depend on other patterns
**Rationale**: Ensures modularity and independent reusability
**Implementation**: Each pattern self-contained with own imports
**Exceptions**: Shared utilities in aget.utils

### BR-003: Idempotent Operations
**Rule**: Running any pattern multiple times must be safe
**Rationale**: User safety, predictable behavior
**Examples**:
- `wake` creates session OR shows existing status
- `extract` skips if product already exists
- `init` with --force overwrites, without --force preserves

## Template Rules

### BR-004: Template Hierarchy
**Rule**: minimal ⊂ standard ⊂ agent (each extends the previous)
**Rationale**: Users can upgrade templates without losing work
**Implementation**: Templates build on each other incrementally
**Validation**: Template tests verify subset relationships

### BR-005: Default Template Selection
**Rule**: No template specified → use 'standard'
**Rationale**: Balances features with simplicity for most users
**Override**: --template flag or --minimal shorthand

## Session Management Rules

### BR-006: Session State Persistence
**Rule**: Session state must survive agent restarts
**Location**: `.session_state.json` in project root
**Format**: JSON with ISO timestamps
**Cleanup**: Automatic after 30 days of inactivity

### BR-007: Session Numbering
**Rule**: Sessions increment from last known state
**Reset**: Only on explicit user request or corruption
**Recovery**: If corrupted, start from session 1 with warning

## Git Operation Rules

### BR-008: No Destructive Git Operations
**Rule**: Never use git force push or destructive commands
**Rationale**: Preserve user work and history
**Implementation**: No --force flags in git commands
**Exception**: Only with explicit user confirmation

### BR-009: Commit Message Format
**Rule**: Commits follow conventional format: `type: description`
**Types**: feat, fix, docs, style, refactor, test, chore
**Enforcement**: Pre-commit hooks when available
**Fallback**: Best-effort formatting

## File Operation Rules

### BR-010: Path Security
**Rule**: All file operations must be within project root
**Rationale**: Prevent directory traversal attacks
**Implementation**: Path.resolve() and parent validation
**Error**: Reject operations outside project boundary

### BR-011: Backup Before Modify
**Rule**: Create backups before modifying existing files
**Format**: `{filename}.backup.{timestamp}`
**Retention**: Keep last 3 backups
**Cleanup**: Remove backups older than 7 days

### BR-012: File Creation Safety
**Rule**: Never overwrite files without --force flag
**Check**: Verify file existence before writing
**Prompt**: Ask for confirmation if file exists
**Exception**: Temporary and cache files

## Error Handling Rules

### BR-013: Graceful Degradation
**Rule**: Partial success is better than total failure
**Example**: If git commit fails, still save work locally
**Priority**: Preserve user work > complete all steps
**Reporting**: Clear indication of what succeeded/failed

### BR-014: No Silent Failures
**Rule**: All errors must be visible to user
**Format**: `❌ Error: {what} - {why} - {recovery}`
**Logging**: Errors also saved to `.aget/logs/`
**Level**: INFO by default, DEBUG with --verbose

### BR-015: Recovery Suggestions
**Rule**: Every error must suggest recovery action
**Example**: "Git not found - Install git or use --no-git"
**Documentation**: Link to relevant docs when appropriate

## Evolution Tracking Rules

### BR-016: Decision Documentation
**Rule**: Significant changes require evolution entry
**Threshold**: Breaking changes, new features, architecture changes
**Format**: `YYYY-MM-DD-HHMMSS-{decision|discovery}.md`
**Location**: `.aget/evolution/`

### BR-017: Evolution Retention
**Rule**: Evolution entries are permanent record
**Rationale**: Preserve project history and learning
**Archival**: Move to yearly folders after 1 year
**Access**: `aget evolution --list` shows recent entries

## Pattern Development Rules

### BR-018: Pattern Return Contract
**Rule**: All patterns must return standardized dict
**Required Keys**: status, message, changes
**Optional Keys**: errors, warnings, next_steps
**Status Values**: success, failure, partial

### BR-019: Pattern Documentation
**Rule**: Every pattern must have README.md
**Sections**: Purpose, Usage, Parameters, Examples
**Format**: Follow PATTERN_TEMPLATE.md
**Location**: `patterns/{category}/README.md`

## Performance Rules

### BR-020: Command Response Time
**Rule**: Interactive commands complete in <2 seconds
**Measurement**: From invocation to first output
**Exceptions**: Network operations, large file processing
**Optimization**: Lazy loading, progress indicators

### BR-021: Memory Efficiency
**Rule**: Patterns must work with <50MB RAM
**Rationale**: Support resource-constrained environments
**Implementation**: Stream large files, batch processing
**Testing**: Memory profiling in CI

## Compatibility Rules

### BR-022: Python Version Support
**Rule**: Support Python 3.8+ (Ubuntu 20.04 LTS default)
**Testing**: CI matrix for 3.8, 3.9, 3.10, 3.11, 3.12
**Features**: Use only features available in 3.8
**Deprecation**: Follow Python EOL schedule

### BR-023: Cross-Platform Support
**Rule**: Must work on macOS, Linux, Windows (WSL)
**Testing**: GitHub Actions on all platforms
**Path Handling**: Use pathlib for OS independence
**Line Endings**: Git autocrlf configuration

## Security Rules

### BR-024: No Credential Storage
**Rule**: Never store passwords, tokens, or keys
**Check**: Pattern review, secret scanning
**Alternative**: Environment variables, config files
**Documentation**: Clear examples of secure practices

### BR-025: Safe Command Execution
**Rule**: Sanitize all shell command inputs
**Implementation**: Use subprocess with arrays, not strings
**Validation**: Reject suspicious characters
**Logging**: Log all executed commands in debug mode

---

*These business rules represent the core policies that ensure AGET remains safe, predictable, and maintainable.*

*Last Updated: 2025-09-25*
*Version: 1.0.0*