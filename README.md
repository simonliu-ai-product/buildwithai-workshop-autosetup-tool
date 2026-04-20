# bwai-workshop-tools

A universal CLI tool for Google Cloud workshop environment setup. Define steps in a JSON file and run them all at once.

**Available in:** [繁體中文](README_ZHTW.md) | [日本語](README_JP.md) | [한국어](README_KO.md)

---

## Installation

```bash
git clone https://github.com/simonliu-ai-product/buildwithai-workshop-autosetup-tool.git
cd buildwithai-workshop-autosetup-tool
pip install -e .
```

## Commands

### `bwai-workshop setup` — Run setup steps

```bash
# Run all steps (interactive confirmation for each)
bwai-workshop setup --step path/to/config.json

# Run specific steps only (comma-separated IDs)
bwai-workshop setup --step path/to/config.json --only auth,enable-apis

# Preview steps without executing
bwai-workshop setup --step path/to/config.json --dry-run
```

### `bwai-workshop verify` — Verify setup completion

```bash
# Verify all steps
bwai-workshop verify --step path/to/config.json

# Verify specific steps only
bwai-workshop verify --step path/to/config.json --only auth,check-billing-credit
```

### `bwai-workshop language` — Manage display language

```bash
# List supported languages
bwai-workshop language list

# Set language
bwai-workshop language set en      # English
bwai-workshop language set zh-tw   # Traditional Chinese
bwai-workshop language set ja      # Japanese
bwai-workshop language set ko      # Korean

# Show current language
bwai-workshop language show
```

### `bwai-workshop steps list` — List step types

```bash
bwai-workshop steps list
```

---

## Supported Step Types

| type | Description |
| :--- | :--- |
| `gemini_cli_vertex_auth` | Configure Gemini CLI with Vertex AI authentication (ADC) |
| `gcloud_auth` | Google Cloud login and project setup |
| `gcloud_enable_apis` | Enable specified Google Cloud APIs |
| `gcp_billing_credit` | Check if GCP project has Workshop promotional credit |
| `python_venv` | Create Python virtual environment and install dependencies |
| `shell` | Execute custom shell command |

---

## Step File Format

```json
{
  "name": "My Setup Flow",
  "description": "Description text",
  "steps": [
    {
      "id": "my-step",
      "type": "shell",
      "description": "Run a custom command",
      "params": {
        "command": "echo hello"
      }
    }
  ]
}
```

## Examples

See the `examples/` folder for complete examples:

- `adk-gemini-agent.json` — Full setup flow for ADK Gemini Agent Workshop
