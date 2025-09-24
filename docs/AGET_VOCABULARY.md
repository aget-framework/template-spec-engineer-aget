# AGET Controlled Vocabulary

*Last Updated: 2025-09-24*

## Critical Distinctions

### outputs vs Outputs
- **outputs/** (lowercase) = Agent's internal workspace, temporary files, working data
- **Outputs** (capital) = Public products the agent creates/maintains (separate repos or published artifacts)

### agent vs Agent
- **agent** = The code/script that performs tasks
- **Agent** = The conceptual entity with agency and decision-making capability

### data vs outputs vs Outputs
- **data/** = Input data, references, read-mostly content
- **outputs/** = Working space, what agent writes during processing
- **Outputs** = Public manifestations, community value created

### Naming Convention
- **aget-*** = Framework infrastructure (aget-cli-agent-template)
- ***-aget** = AGET-powered agents (llm-manager-aget, spotify-aget)
- **No suffix** = Traditional tools/libraries (llm-judge, DatGen)

### Bridge Terms
- **Bridge** = Process of extracting value from outputs → Outputs
- **Extraction** = Identifying valuable patterns in outputs/
- **Manifestation** = Public product created from private work
- **Enhancement** = Agent improving existing product

### Evolution Terms
- **Discovery** = Real-time insight during agent work
- **Milestone** = Significant achievement or transition
- **Pattern** = Reusable solution discovered through usage

### Directory Standards
- **.aget/** = Framework metadata, state, evolution tracking
- **artifacts/** = Persistent agent models, checkpoints
- **candidates/** = Potential future Outputs in outputs/

## Usage Examples

"The agent processes data from `data/` into its `outputs/` workspace, then we extract valuable patterns to create public `Outputs`."

"The `spotify-aget` agent (an `-aget` suffix repo) analyzes music in its `outputs/` directory and will eventually produce a music-analysis library as an `Output`."

"Framework components use the `aget-` prefix, while agents use the `-aget` suffix."

---

*This vocabulary ensures clarity in documentation and communication about AGET concepts.*