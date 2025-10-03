# Aget Worker Template

> **Framework for AI-assisted software engineering agents**

Transform any project into an AI agent workspace where your coding assistant discovers patterns and evolves capabilities through interaction. Works with Claude Code, Cursor, Aider, Windsurf, and other AI coding assistants.

**Current Version**: v2.4.0 "Clarity"

---

## What This Is

**Not a traditional CLI tool** - Aget is a template and pattern system that your AI assistant uses to organize work, discover patterns, and maintain context across sessions.

**Mental Model**:
```
You → Natural Language → AI Assistant → Discovers Aget Patterns → Executes
```

You never type `aget` commands. Your AI reads the patterns and uses them based on your natural language requests.

---

## Quick Start (2 Minutes)

### 1. Clone the Template

```bash
# Choose your agent name based on capability:
# -AGET suffix = action-taking (can modify systems) ⚠️
# -aget suffix = information-only (read-only) ✅

git clone https://github.com/aget-framework/aget-worker-template.git my-custom-AGET
cd my-custom-AGET
```

### 2. Open with Your AI Assistant

```bash
# Claude Code (primary development)
claude .

# Also works with: Cursor, Aider, Windsurf, and other CLI agents
```

### 3. Start with Natural Language

```
You: hey

AI: [Reads AGENTS.md, checks environment, reports status]

You: initialize this for a Python data analysis project

AI: [Creates workspace/, products/, data/ structure with Python tooling]

You: wind down

AI: [Commits changes, creates session notes, reports completion]
```

**That's it.** Your AI assistant handles the mechanics. You focus on what you want to accomplish.

---

## How It Works

### AI-Discovered Patterns

Your AI assistant discovers patterns from:

1. **AGENTS.md** - Configuration and protocols (read on wake-up)
2. **.aget/** - Framework metadata, patterns, learnings
3. **Directory structure** - Conventional organization
4. **Session history** - Previous interactions and context

### Natural Language Interface

Instead of commands, you use conversational language:

| You Say | AI Understands |
|---------|----------------|
| "hey" or "wake up" | Read configuration, check status, report readiness |
| "create a web scraper" | Scaffold tool in workspace/, add tests, document |
| "run tests" | Execute test suite, report results |
| "what did we work on last time?" | Read session notes, summarize |
| "wind down" | Commit changes, create session notes |
| "sign off" | Quick save and exit |

### Session Workflow

```
wake up → work (iterative) → wind down → sign off
   ↓           ↓                  ↓
Read       Natural           Create
config     language          session
           interaction       notes
```

---

## Who This Is For

- **Software Owners** - Govern project evolution with AI assistance
- **Data Scientists** - Organize analysis work (Spotify data, financial, etc.)
- **Contributors** - Private workspace for external projects
- **Analysts** - Examine codebases without modifying
- **Learners** - Use AI to understand and build software

---

## Naming Convention

**Suffix signals capability** (v2.4 framework convention):

- **-AGET** = Action-taking agent (⚠️ can modify systems, create PRs, deploy)
- **-aget** = Information-only agent (✅ read-only, reports, analysis)

**Examples**:
```
my-github-AGET              # Can create PRs, merge code, modify repos
my-spotify-analyst-aget     # Reports analytics only (read-only)
my-deployment-AGET          # Can deploy to production
my-code-reviewer-aget       # Reviews code, provides feedback only
```

Like `sudo` or `rm -rf`, the capitalized AGET provides visual warning of powerful operations.

---

## Directory Structure

```
my-custom-AGET/
├── AGENTS.md              # Configuration (AI reads on wake-up)
├── .aget/                 # Framework metadata
│   ├── version.json       # Agent identity and capabilities
│   ├── evolution/         # Learnings and decisions (L*.md)
│   ├── checkpoints/       # State snapshots
│   └── patterns/          # Reusable patterns (optional)
├── workspace/             # Private workspace for exploration
├── products/              # Public artifacts for others
├── data/                  # Persistent data storage
├── docs/                  # Documentation
├── src/                   # Source code (if building tool)
├── tests/                 # Test suite
└── sessions/              # Session notes (timestamped)
```

**Vocabulary**:
- `workspace/` = Your agent's private scratchpad
- `products/` = Public outputs for others
- `.aget/evolution/` = Learnings discovered over time
- `sessions/` = Interaction history

---

## What Your AI Understands

When you open a project with Aget template, your AI can:

### Session Management
- **"hey"** - Wake up, check environment, report status
- **"wind down"** - Commit changes, create session notes
- **"sign off"** - Quick save and exit

### Work Commands
- **"run tests"** - Execute test suite
- **"check documentation"** - Analyze docs completeness
- **"tidy up"** - Clean temporary files
- **"sanity check"** - Verify critical components

### Discovery
- **"read docs"** - Smart documentation briefing
- **"what did we work on last time?"** - Session history
- **"show recent learnings"** - Evolution documents

### Development
- **"create [type] for [purpose]"** - Scaffold new component
- **"refactor [component]"** - Improve code structure
- **"add tests for [feature]"** - Expand test coverage

**Note**: Exact phrasing is flexible. Your AI interprets intent, not rigid commands.

---

## Key Features

### Progressive Understanding

Agents start empty and grow knowledge through:
- Session notes capturing what worked
- Evolution documents (L*.md) capturing learnings
- Checkpoints for significant state changes

### Universal Compatibility

Works with all major AI coding assistants:
- ✅ Claude Code (primary development)
- ✅ Cursor
- ✅ Aider
- ✅ Windsurf
- ✅ GitHub Copilot CLI
- ✅ Any AI assistant that can read project files

### Privacy-First

- Works fully offline
- No telemetry or tracking
- Private by default
- Selective sharing (your choice)

### Specification-Driven

Define capabilities before building:
- EARS patterns (aerospace requirements format)
- Ambiguity detection
- Validation frameworks

---

## Documentation

- **[Getting Started Guide](docs/GET_STARTED.md)** - Detailed setup and customization
- **[Pattern Explained](docs/PATTERNS_EXPLAINED.md)** - How patterns work
- **[Why This Matters](docs/WHY_THIS_MATTERS.md)** - Philosophy and rationale
- **[Troubleshooting](docs/TROUBLESHOOTING.md)** - Common issues
- **[docs/README.md](docs/README.md)** - Documentation index

---

## Examples

### Example 1: Data Analysis Agent

```bash
git clone https://github.com/aget-framework/aget-worker-template.git my-spotify-analyst-aget
cd my-spotify-analyst-aget
claude .
```

```
You: hey
AI: [Reads config, reports readiness]

You: I want to analyze my Spotify streaming history

AI: I'll help you set up a Spotify analysis workspace. First, where is your data?

You: I have spotify_streaming_history.json in ~/Downloads

AI: [Copies data to data/, creates analysis notebook in workspace/, sets up Python environment]

You: analyze top artists by decade

AI: [Runs analysis, creates visualization in products/, reports findings]

You: wind down

AI: [Commits analysis code, creates session notes, reports: "Session saved. Analysis available in products/top_artists_by_decade.html"]
```

**Result**: Read-only analysis, no system modifications (suffix: -aget ✅)

### Example 2: GitHub Management Agent

```bash
git clone https://github.com/aget-framework/aget-worker-template.git my-github-AGET
cd my-github-AGET
claude .
```

```
You: hey
AI: [Reads config, reports readiness]

You: Create a PR for the feature branch

AI: I can create PRs. Which repository and what's the branch name?

You: my-project repo, feature/new-api branch to main

AI: [Uses gh CLI to create PR, adds description from recent commits, reports PR URL]

You: wind down

AI: [Commits session notes: "Created PR #123 for feature/new-api"]
```

**Result**: Modified GitHub state (suffix: -AGET ⚠️)

---

## Comparison to Traditional Tools

| Traditional CLI | Aget Template |
|----------------|---------------|
| Human types commands | AI discovers patterns |
| Rigid command syntax | Natural language |
| Documentation as reference | AI reads configuration |
| State in shell history | State in session notes |
| One-off execution | Evolving capabilities |

Aget is not a faster way to type commands. It's a framework for AI-human collaboration.

---

## Framework Information

**Organization**: [aget-framework](https://github.com/aget-framework)
**Template**: [aget-worker-template](https://github.com/aget-framework/aget-worker-template)
**Hub** (issues, coordination): [aget-aget](https://github.com/aget-framework/aget-aget)

**Version**: v2.4.0 "Clarity"
- Naming conventions established
- Organizational grouping (aget_group)
- Privacy-first architecture foundation

---

## Migration from v2.3

If you have existing agents on v2.3:
- See [v2.4 Migration Guide](https://github.com/aget-framework/aget-aget/blob/main/docs/v2.4_MIGRATION_GUIDE.md)
- Old URL redirects: `aget-framework/aget-cli-agent-template` → `aget-framework/aget-worker-template`

---

## Contributing

Framework is in active development. Contribution guidelines coming in v2.5+.

---

## License

Apache 2.0

---

## Support

- **Issues**: [File to hub repo](https://github.com/aget-framework/aget-aget/issues) with `[worker-template]` prefix
- **Discussions**: GitHub Discussions (coming soon)
- **Documentation**: Start with [docs/README.md](docs/README.md)

---

*Aget Framework - AI discovers patterns, you describe intent*
