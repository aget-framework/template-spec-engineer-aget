# ADR 004: Three-Tier Degradation Pattern

## Status
Accepted

## Date
2025-09-22

## Context
AGET v2 needs to work in diverse environments:
- Developer machines with full tooling (gh, git, make, etc.)
- Minimal environments (only Python and filesystem)
- CI/CD pipelines with varying tool availability

The RKB content enhancement agent represents a critical production system that must never lose data due to missing dependencies.

## Decision
Implement three-tier degradation as foundational architecture in Gate 1 (Phase 1).

Every AGET command will inherit a base pattern:
1. **Rich tier** (gh available): Enhanced GitHub CLI features
2. **Standard tier** (git available): Local git operations
3. **Basic tier** (always): Pure filesystem operations

This is built into core architecture, not added per-command.

## Consequences

### Positive
- Guaranteed safety for critical agents (RKB)
- Consistent behavior across all commands
- Single pattern to learn and test
- Natural progressive enhancement
- No retrofitting needed

### Negative
- Slightly longer Gate 1 implementation (~5 hours)
- All commands must implement tier_basic (enforced by base class)

## Implementation
```python
class BaseCommand(ABC):
    def execute(self):
        """All commands inherit this pattern"""
        if self.has_capability('gh') and hasattr(self, 'tier_gh'):
            return self.tier_gh()
        elif self.has_capability('git') and hasattr(self, 'tier_git'):
            return self.tier_git()
        return self.tier_basic()  # Required

    @abstractmethod
    def tier_basic(self):
        """Must be implemented - pure filesystem"""
        pass
```

## Examples

### aget init
- **gh tier**: Creates .github/ISSUE_TEMPLATE/
- **git tier**: Updates .gitignore
- **basic tier**: Creates AGENTS.md and .aget/

### aget rollback
- **gh tier**: Creates issue documenting rollback
- **git tier**: Uses git reflog for recovery
- **basic tier**: Restores from .aget/backups/

## References
- PROJECT_PLAN.md: Gate 1 requirements
- GitHub Issue #1: Missing docs structure
- RKB agent safety requirements