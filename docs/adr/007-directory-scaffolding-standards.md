# ADR-007: Directory Scaffolding Standards

**Date**: 2025-09-24
**Status**: Proposed
**Context**: Learning from llm-manager-aget implementation

## Decision

AGET will provide standardized directory scaffolding templates for different project types, automatically creating the complete structure needed for agents and tools.

## Context

During the creation of llm-manager-aget, we discovered that while `aget init` creates the basic configuration, significant manual work was needed to create the proper directory structure. This friction slows adoption and can lead to inconsistent implementations.

## Directory Templates

### Agent Template
For projects that act as autonomous agents (`*-aget` pattern):

```
project-aget/
├── src/                      # Private implementation
│   ├── __init__.py
│   ├── core.py              # Core agent logic
│   └── providers/           # External integrations
├── outputs/                 # Private workspace (lowercase)
│   ├── README.md           # "Agent's private exploration space"
│   ├── analysis/           # Analysis results
│   ├── reports/            # Generated reports
│   └── experiments/        # Testing new approaches
├── Outputs/                # Public extractions (capital O)
│   └── README.md          # "Public tools extracted for community"
├── data/                   # Persistent storage
│   ├── cache/             # Temporary cache
│   └── state/             # Persistent state
├── scripts/               # Agent command scripts
│   ├── session_protocol.py
│   └── housekeeping_protocol.py
├── tests/                 # Test suite
├── .aget/                 # AGET metadata
│   ├── version.json
│   └── evolution/         # Learning capture
│       └── README.md      # "Document decisions and discoveries"
├── AGENTS.md              # Agent configuration
├── README.md              # Project documentation
└── bridge.py              # Bridge extraction mechanism
```

### Tool Template
For traditional tools and libraries:

```
project-tool/
├── src/                   # Source code
│   ├── __init__.py
│   └── main.py
├── tests/                 # Test suite
├── docs/                  # Documentation
├── examples/              # Usage examples
├── AGENTS.md             # Agent instructions
└── README.md             # Project documentation
```

### Hybrid Template
For projects that are both tools and have agent capabilities:

```
project/
├── src/                   # Tool source code
├── agent/                 # Agent capabilities
│   ├── outputs/          # Agent workspace
│   ├── Outputs/          # Public extractions
│   └── bridge.py         # Bridge mechanism
├── tests/
├── docs/
├── .aget/
│   └── evolution/
├── AGENTS.md
└── README.md
```

## Implementation

### Command Interface
```bash
# Create agent project
aget init --template agent [project-name]

# Create tool project
aget init --template tool [project-name]

# Create hybrid project
aget init --template hybrid [project-name]

# Interactive mode (asks questions)
aget init --interactive
```

### Directory Creation Logic

1. **Create all directories** with proper permissions
2. **Add README.md files** explaining each directory's purpose
3. **Create .gitkeep files** in empty directories
4. **Set up .gitignore** with appropriate patterns
5. **Initialize .aget/version.json** with template info

### README Content

Each special directory gets a README explaining its purpose:

**outputs/README.md**:
```markdown
# Private Workspace (outputs/)

This directory is your agent's private exploration space.
- Experiments and analysis go here
- Not meant for public consumption
- Can contain sensitive data or API keys
- Ignored by git (add to .gitignore if needed)
```

**Outputs/README.md**:
```markdown
# Public Outputs (Outputs/)

This directory contains tools extracted for community use.
- Clean, standalone tools
- No private data or API keys
- Ready for public distribution
- Each tool should be self-contained
```

**.aget/evolution/README.md**:
```markdown
# Evolution Tracking

Document your agent's learning and evolution:
- Design decisions
- Pattern discoveries
- Optimization strategies
- Lessons learned

Format: YYYY-MM-DD_description.md
```

## Consequences

### Positive
- **Faster setup**: <30 seconds to full structure
- **Consistency**: All AGET projects follow same structure
- **Clarity**: READMEs explain each directory's purpose
- **Best practices**: Structure guides good design

### Negative
- **Complexity**: More code to maintain in AGET
- **Opinions**: Forces specific structure (may not fit all needs)
- **Migration**: Existing projects need restructuring

### Mitigations
- Make templates configurable via .aget/config.yaml
- Allow --no-readme flag to skip README creation
- Provide migration tool for existing projects

## Alternatives Considered

1. **Single flat template**: Rejected - doesn't serve different needs
2. **No templates**: Rejected - too much manual work
3. **Config file only**: Rejected - directories need explanation

## Implementation Priority

HIGH - This is critical for Gate 3 migration tools and directly addresses friction discovered in llm-manager-aget creation.

## References

- llm-manager-aget implementation experience
- AGET_FRAMEWORK_VISION.md
- User feedback on v1→v2 migration

---

*This ADR captures the learning that proper scaffolding dramatically reduces setup time from 2 hours to <30 minutes.*