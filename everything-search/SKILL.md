---
name: everything-search
description: >
  Windows file search using the Everything indexed search engine. Use when
  finding or locating local files or folders by name, pattern, or extension.
  Not for content search within files or non-Windows systems.
---

# Everything Search Skill

Instant file search on Windows using Everything's indexed database. Searches execute in milliseconds.

## Prerequisites

**es.exe** (Everything command-line tool) is bundled with this skill and used automatically. The Everything application itself must be installed and running to provide the search index — see `references/installation.md` for help.

Quick verification:
```bash
python scripts/verify_es_installation.py
```

## Usage

### Basic Search

```bash
python scripts/search.py "query"
```

### Options

| Option | Example | Purpose |
|--------|---------|---------|
| `--limit N` | `--limit 50` | Limit results (default: 100) |
| `--folder PATH` | `--folder "C:\Users"` | Restrict to folder |

### Query Patterns

| Pattern | Example | Result |
|---------|---------|--------|
| Extension | `*.pdf` | All PDF files |
| Partial name | `report` | Files containing "report" |
| Boolean OR | `*.jpg\|*.png` | JPEG or PNG files |
| Boolean NOT | `*.log !debug` | Logs except debug |
| Location | `downloads\\ *.mp3` | MP3s in Downloads |
| Multiple terms | `python script` | Files with both terms (AND) |

## Examples

**Find all Python files:**
```bash
python scripts/search.py "*.py"
```

**Find config files in a project:**
```bash
python scripts/search.py "*.config|*.json|*.yaml" --folder "C:\projects\myapp"
```

**Find files excluding build artifacts:**
```bash
python scripts/search.py "*.js !node_modules !dist"
```

**Find documents in Downloads:**
```bash
python scripts/search.py "downloads\\ *.pdf|*.docx"
```

## Output Format

Results are returned as Markdown:
```markdown
# Everything Search Results

**Query:** `*.py`
**Results:** 247 (limited to 100)

1. `C:\Users\...\project\main.py`
2. `C:\Users\...\project\utils.py`
...
```

## Limitations

### CLI Limitations (es.exe)
- **No date filtering**: `modified:today` is GUI-only
- **No file attributes**: Size/date metadata filters unavailable in CLI

**Workaround:** Use Everything GUI for date-based searches.

### Content Search
Content searches (`content:keyword`) are slow—content is not indexed. Use sparingly.

## Reference Materials

Load these when needed:
- **`references/search-syntax.md`** - Complete syntax guide with examples
- **`references/faq.md`** - Everything FAQ and troubleshooting
- **`references/installation.md`** - Detailed installation instructions

## Error Handling

The wrapper provides clear guidance for:
- **es.exe not found** - Installation instructions
- **Invalid syntax** - Syntax suggestions
- **No results** - Troubleshooting tips
