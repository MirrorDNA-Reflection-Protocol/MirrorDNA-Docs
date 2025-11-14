# MirrorDNA Ecosystem Maintenance Toolkit

This directory contains maintenance tools to help keep the MirrorDNA ecosystem coherent and well-documented.

## Tools Overview

### 1. `ecosystem_map.json`

A comprehensive map of all repositories in the MirrorDNA ecosystem.

**Structure:**
```json
{
  "repositories": [
    {
      "name": "repository-name",
      "visibility": "public|private",
      "role": "spec|product|docs|sdk|playground|r&d",
      "description": "Short description of the repository"
    }
  ]
}
```

**Roles:**
- **spec**: Specifications and standards
- **product**: Core products and services
- **docs**: Documentation sites
- **sdk**: Software Development Kits
- **playground**: Examples, quickstarts, and experimental projects
- **r&d**: Research and development projects

### 2. `print_ecosystem.py`

Displays the ecosystem map in a nice, organized format.

**Features:**
- Groups repositories by role
- Shows visibility status (public/private)
- Provides summary statistics
- Color-coded output with emojis

**Usage:**
```bash
python3 tools/print_ecosystem.py
```

**No dependencies required** - uses only Python standard library.

### 3. `check_markdown_links.py`

Validates markdown links throughout the repository.

**Features:**
- Scans all `.md` files recursively
- Checks relative file links
- Identifies broken links
- Reports suspicious or unreachable paths
- Skips external URLs (http/https)
- Skips internal anchors (#)

**Usage:**
```bash
python3 tools/check_markdown_links.py
```

**Returns:**
- Exit code 0 if all links are valid
- Exit code 1 if broken links are found

**No dependencies required** - uses only Python standard library.

## Quick Start

### View the Ecosystem Map

```bash
cd /path/to/MirrorDNA-Docs
python3 tools/print_ecosystem.py
```

Example output:
```
==============================================================================================
                             MIRRORDNA ECOSYSTEM MAP
==============================================================================================

📋 Specification
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Repository                          Visibility   Description
==============================================================================================
MirrorDNA-Standard                  🌐 public    Core specification for AI agent observability...

📚 Documentation
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Repository                          Visibility   Description
==============================================================================================
MirrorDNA-Docs                      🌐 public    Unified documentation site for the MirrorDNA...
```

### Check Markdown Links

```bash
cd /path/to/MirrorDNA-Docs
python3 tools/check_markdown_links.py
```

Example output (all valid):
```
Checking markdown links in: /path/to/MirrorDNA-Docs

Found 18 markdown files to check...

==============================================================================================
                           MARKDOWN LINK CHECK REPORT
==============================================================================================

Scanned 18 markdown files
Found 147 links
Broken links: 0
Error links: 0

✅ All relative links are valid!
```

Example output (with issues):
```
❌ Issues Found:

File: website/docs/intro.md
──────────────────────────────────────────────────────────────────────────────────────────
  ❌ [Getting Started](./getting-started.md)
     File not found: /path/to/MirrorDNA-Docs/website/docs/getting-started.md
```

## Maintenance Workflows

### Adding a New Repository

1. Edit `ecosystem_map.json`
2. Add the new repository entry with all required fields
3. Run `print_ecosystem.py` to verify the output
4. Commit the changes

Example:
```bash
# Edit the file
vim tools/ecosystem_map.json

# Verify the output
python3 tools/print_ecosystem.py

# Commit
git add tools/ecosystem_map.json
git commit -m "Add new repository to ecosystem map"
```

### Before Committing Documentation Changes

Always run the link checker to ensure no broken links:

```bash
python3 tools/check_markdown_links.py
```

If broken links are found, fix them before committing.

### Regular Maintenance

Run these checks periodically (e.g., weekly or before releases):

```bash
# Check ecosystem is up to date
python3 tools/print_ecosystem.py

# Validate all links
python3 tools/check_markdown_links.py
```

## Integration with CI/CD

### GitHub Actions Example

Add to `.github/workflows/check-links.yml`:

```yaml
name: Check Markdown Links

on:
  pull_request:
    paths:
      - '**.md'
  push:
    branches: [main]

jobs:
  check-links:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3

      - name: Check markdown links
        run: |
          python3 tools/check_markdown_links.py
```

## Extending the Toolkit

### Adding New Scripts

Follow these conventions:

1. Use Python 3.8+ with standard library only (no external dependencies)
2. Include a docstring at the top explaining the script's purpose
3. Add proper error handling
4. Update this README with usage instructions
5. Make scripts executable: `chmod +x tools/your_script.py`

### Adding New Fields to ecosystem_map.json

If you need to track additional metadata:

1. Add the field to all repository entries in `ecosystem_map.json`
2. Update `print_ecosystem.py` to display the new field
3. Document the new field in this README

## Requirements

- **Python**: 3.8 or higher
- **No external dependencies**: All scripts use only Python standard library

## Troubleshooting

### Script Not Found

Make sure you're running from the repository root:
```bash
cd /path/to/MirrorDNA-Docs
python3 tools/print_ecosystem.py
```

### Permission Denied

Make scripts executable:
```bash
chmod +x tools/*.py
```

### Unicode Errors

If you encounter encoding issues, ensure your terminal supports UTF-8:
```bash
export LANG=en_US.UTF-8
export LC_ALL=en_US.UTF-8
```

## Contributing

When contributing to these tools:

1. Test your changes locally
2. Ensure scripts work on Linux, macOS, and Windows (WSL)
3. Update this README if adding new features
4. Follow existing code style (PEP 8 for Python)

## Support

For questions or issues with these tools:

- **GitHub Issues**: [MirrorDNA-Docs/issues](https://github.com/MirrorDNA-Reflection-Protocol/MirrorDNA-Docs/issues)
- **Discussions**: [MirrorDNA Discussions](https://github.com/MirrorDNA-Reflection-Protocol/discussions)

---

**Last Updated**: 2025-11-14
**Maintainer**: MirrorDNA Core Team
