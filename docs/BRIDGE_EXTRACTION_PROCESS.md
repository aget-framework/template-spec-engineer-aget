# Bridge Extraction Process

## Overview
The bridge extraction process transforms private agent outputs into public Outputs (products) that provide value to the community.

## Step-by-Step Process

### 1. Discovery Phase
The agent works naturally in its `outputs/` directory, creating tools, scripts, and data as needed for its tasks.

```
outputs/
├── cost_analyzer.py       # Tool for analyzing API costs
├── data_processor.js      # Script for processing data
├── config.yaml           # Configuration files
└── experiments/          # Experimental code
```

### 2. Value Assessment
The bridge pattern scans outputs and calculates value scores based on:

- **Size Factor** (10-30 points)
  - >1KB: +10 points
  - >10KB: +20 points

- **Recency Factor** (10-30 points)
  - <7 days old: +30 points
  - <30 days old: +10 points

- **Documentation** (+25 points)
  - Has README.md in same directory

- **Test Coverage** (+25 points)
  - Has test files for the output

### 3. Extraction Command
When a valuable output is identified:

```bash
# Current method (direct pattern use)
python3 patterns/bridge/extract_output.py

# Future method (Phase 4)
aget extract outputs/cost_analyzer.py --target Outputs/
```

### 4. Transformation
During extraction, the bridge:

1. **Transforms Names**
   - `my_tool.py` → `my-tool.py`
   - `config.toml` → `{project}-config.toml` (if generic)

2. **Creates Manifest**
   ```json
   {
     "extracted_from": "llm-manager-aget",
     "original_path": "outputs/cost_analyzer.py",
     "output_name": "cost-analyzer.py",
     "extraction_date": "2025-09-24T10:30:00",
     "value_score": 80,
     "category": "tool",
     "public_product": true
   }
   ```

3. **Records Evolution**
   Creates entry in `.aget/evolution/YYYY-MM-DD-extraction.md`

### 5. Public Output Structure
After extraction:

```
Outputs/
├── cost-analyzer/
│   ├── cost-analyzer.py
│   ├── cost-analyzer.py.manifest.json
│   └── README.md
└── data-processor/
    ├── data-processor.js
    └── data-processor.js.manifest.json
```

## Integration Points

### With AGET CLI (Current)
- `aget init` creates outputs/ directory
- Patterns can be applied via `aget apply bridge` (Phase 3)

### With Framework (Future)
- Agents use bridge patterns automatically
- Evolution tracking integrated
- Output registry for discovery

## Example Workflow

```bash
# 1. Agent creates output
echo "#!/usr/bin/env python3
import json
# Tool code here" > outputs/my_tool.py

# 2. Scan for valuable outputs
python3 patterns/bridge/extract_output.py

# 3. Extract specific output (future)
aget extract outputs/my_tool.py

# 4. Output is now public
ls Outputs/my-tool/
```

## Best Practices

1. **Natural Accumulation**
   - Don't force extraction
   - Let outputs mature in outputs/ first

2. **Value Threshold**
   - Only extract outputs with score >50
   - Ensure documentation exists

3. **Backward Compatibility**
   - Once extracted, maintain compatibility
   - Version Outputs properly

4. **Clear Manifests**
   - Always create manifests
   - Track origin and transformation

## Success Criteria

An extraction is successful when:
- ✅ Output has value score >50
- ✅ Name is transformed appropriately
- ✅ Manifest is created
- ✅ Evolution is recorded
- ✅ Output works standalone
- ✅ Documentation is included

## Common Patterns

### Tool Extraction
```
outputs/analyzer.py → Outputs/analyzer/
```

### Data Set Extraction
```
outputs/dataset.json → Outputs/datasets/project-dataset.json
```

### Configuration Extraction
```
outputs/config.yaml → Outputs/configs/project-config.yaml
```

## Troubleshooting

### No Outputs Found
- Ensure outputs/ directory exists
- Check that files are >100 bytes
- Verify files aren't hidden (start with .)

### Low Value Scores
- Add documentation (README.md)
- Create tests for the output
- Ensure file is substantial (>1KB)

### Extraction Fails
- Check write permissions on target directory
- Ensure source file exists
- Verify path is relative to project root

---

*The bridge extraction process is central to AGET's vision of agents as co-creators of community value.*