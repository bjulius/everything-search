---
name: everything-search
description: This skill enables Claude to use the Everything search tool as the default file search mechanism on Windows. When local file discovery is needed, use the Everything CLI wrapper to instantly locate files and folders by name with powerful search syntax support. Returns results in Markdown format for immediate readability.
---

# Everything Search Skill

## Purpose

This skill provides Claude with instant file search capabilities on Windows using the Everything search tool. Instead of traditional filesystem searching, Claude can leverage Everything's indexed search to find files and folders with lightning-fast performance.

Everything is a specialized search engine for Windows that:
- **Indexes by filename**: Results appear instantly for name-based queries
- **Powerful syntax**: Supports wildcards, boolean operators, location restrictions, and more
- **Minimal overhead**: Uses negligible system resources
- **Real-time updates**: Automatically stays current with filesystem changes

## When to Use This Skill

Use this skill automatically whenever:
- Needing to find or locate local files and folders
- Searching for files by name, type, or pattern
- Looking for files in specific directories
- Discovering files matching certain criteria (e.g., "all Python files modified recently")
- Exploring the filesystem to understand what exists

Do NOT use this skill if:
- Everything is not installed on the user's system
- Searching for content within files (unless absolutely necessary)
- The user specifically asks to avoid using search tools

## How to Use This Skill

### Step 1: Check Everything is Available

The search wrapper automatically checks for Everything installation. If not found, it provides clear guidance on installation.

### Step 2: Execute Searches

Call the search wrapper script with the desired query:

```bash
python scripts/search.py "query_pattern"
```

**Supported query patterns:**

| Pattern | Example | Result |
|---------|---------|--------|
| Filename match | `python search.py "*.pdf"` | All PDF files |
| Partial name | `python search.py "document"` | Files containing "document" |
| Boolean AND | `python search.py "python script"` | Files with both terms |
| Boolean OR | `python search.py "jpg\|png"` | JPEG or PNG files |
| Boolean NOT | `python search.py "!temp"` | Exclude temp files |
| Location-based | `python search.py "downloads\\ *.mp3"` | Music in Downloads |
| Multiple extensions | `python search.py "*.py\|*.js"` | Python or JavaScript |

**Additional options:**

```bash
python search.py "query" --limit 50              # Limit results to 50 (default: 100)
python search.py "query" --folder "C:\path"      # Restrict to folder
```

### Step 3: Parse and Present Results

The script returns results as Markdown, which is immediately readable and can be presented directly to the user or processed further if needed.

## Reference Materials

For complex searches or troubleshooting:
- **search-syntax.md**: Comprehensive guide to Everything's search syntax with practical examples
- **faq.md**: Official Everything FAQ covering installation, configuration, and troubleshooting

Load these references when:
- User asks about advanced search syntax
- Troubleshooting why a search didn't return expected results
- Understanding Everything's features and configuration

## Real-World Usage Examples

### Data Discovery & File Inventory

**Example 1: Find all Python files in your system**
```bash
python scripts/search.py "*.py"
```
*Use case:* Locate all Python scripts for a project audit or migration
*Returns:* Full paths to every .py file indexed by Everything

**Example 2: Find all config files in a project**
```bash
python scripts/search.py "*.config|*.cfg|*.ini|*.toml|*.yaml"
```
*Use case:* Discover configuration files across your system to understand project structure
*Returns:* Config files in various formats

**Example 3: Find test files in specific directory**
```bash
python scripts/search.py "projects\\ test_*.py"
```
*Use case:* Locate unit tests within a projects folder
*Returns:* Python test files matching the pattern

### Cleanup & Maintenance

**Example 4: Find backup and temporary files to clean up**
```bash
python scripts/search.py "*.bak|*.tmp|*.backup"
```
*Use case:* Identify backup files for cleanup or archive
*Returns:* All temporary and backup files system-wide

**Example 5: Find debug logs excluding normal logs**
```bash
python scripts/search.py "*.log debug !production"
```
*Use case:* Separate debug logs from production logs for analysis
*Returns:* Debug log files while excluding production logs

**Example 6: Find old cache files**
```bash
python scripts/search.py "cache !recent"
```
*Use case:* Locate cache directories that can be safely cleared
*Returns:* Cache folders and files

### Project Management

**Example 7: Find all documentation in a project**
```bash
python scripts/search.py "docs\\ *.md|*.txt|*.rst"
```
*Use case:* Inventory all documentation files in a project
*Returns:* All documentation files in the docs folder

**Example 8: Find unfinished work items**
```bash
python scripts/search.py "TODO|FIXME|XXX"
```
*Use case:* Locate source files with TODO comments (requires content search)
*Returns:* Files containing work item markers

**Example 9: Locate source files in nested project structure**
```bash
python scripts/search.py "src\\ *.java|*.cpp|*.h"
```
*Use case:* Find all source code files in a src directory
*Returns:* Source files in various languages

### Advanced Searching

**Example 10: Find recently created files with specific pattern**
```bash
python scripts/search.py "report_2025*.xlsx"
```
*Use case:* Locate 2025 reports quickly by filename pattern
*Returns:* All matching report files

**Example 11: Find duplicate filenames across multiple locations**
```bash
python scripts/search.py "index.html"
```
*Use case:* Discover all index.html files (useful for understanding website structure)
*Returns:* Every index.html file on the system

**Example 12: Find files excluding common ignore patterns**
```bash
python scripts/search.py "*.js !node_modules !dist !build"
```
*Use case:* Find source JavaScript files while excluding build artifacts
*Returns:* JavaScript files excluding common ignored directories

### Result Limiting

**Example 13: Limit results for large queries**
```bash
python scripts/search.py "*.txt" --limit 50
```
*Use case:* Get a manageable sample of results instead of thousands
*Returns:* First 50 matching files

**Example 14: Search in specific folder**
```bash
python scripts/search.py "*.csv" --folder "C:\Users\username\Downloads"
```
*Use case:* Restrict search to a specific location (useful for Downloads cleanup)
*Returns:* All CSV files in Downloads folder only

### Workflow Integration Examples

**Scenario A: Code Migration Audit**
1. `python scripts/search.py "*.py"` - Find all Python files
2. `python scripts/search.py "src\\ *.py"` - Find source Python files
3. `python scripts/search.py "test_*.py"` - Find test files
4. Use results to plan migration strategy

**Scenario B: Documentation Inventory**
1. `python scripts/search.py "*.md|*.rst|*.txt"` - Find all docs
2. `python scripts/search.py "docs\\ README"` - Find README files specifically
3. `python scripts/search.py "*.md !archived"` - Exclude archived documentation
4. Review structure and consolidate

**Scenario C: Security Audit**
1. `python scripts/search.py "*.key|*.pem|*.pfx"` - Find certificates/keys
2. `python scripts/search.py "*password*|*secret*"` - Find suspicious filenames
3. `python scripts/search.py "*.sql !backup"` - Find SQL files excluding backups
4. Review findings for security issues

**Scenario D: Storage Analysis**
1. `python scripts/search.py "*.iso|*.zip|*.rar|*.7z"` - Find archives
2. `python scripts/search.py "*.mp4|*.mkv|*.avi"` - Find video files
3. `python scripts/search.py "*.dmg|*.exe" !installer` - Find installers
4. Identify large files for cleanup or archival

## Performance Characteristics

Everything provides instant search across:
- **120,000 files**: ~14 MB RAM, <1 second indexing
- **1,000,000 files**: ~75 MB RAM, ~1 minute indexing

Searches execute in milliseconds due to filename indexing. This makes Everything superior to Windows built-in search for most file discovery tasks.

## Error Handling

The wrapper script provides clear error messages for:
- **Everything not installed**: Guidance on installation from voidtools.com
- **Invalid query syntax**: Suggestions for fixing common syntax errors
- **Search failures**: Troubleshooting tips from the reference materials

## Integration Best Practices

1. **Use by default**: Whenever needing to find local files, use Everything first
2. **Provide syntax help**: Reference search-syntax.md when users ask about query syntax
3. **Leverage location restriction**: Use `\\` syntax to narrow large searches
4. **Fallback gracefully**: If Everything isn't available, provide clear installation guidance
5. **Load references as needed**: Keep SKILL.md lean; load FAQ/syntax guides only when necessary

---

*This skill is designed to make Everything the default file search tool, eliminating the need for traditional filesystem searching and providing near-instant results for file discovery tasks.*
