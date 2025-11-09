#!/usr/bin/env python3
r"""
Everything Search Wrapper

Provides a Python interface to the Everything search tool on Windows.
Formats results as Markdown for easy consumption by Claude and users.

Usage:
    python search.py "query"
    python search.py "query" --limit 50
    python search.py "query" --folder "C:\Users\brjul\Documents"
"""

import subprocess
import sys
import os
import argparse
from pathlib import Path


def find_everything_cli():
    """
    Locate the Everything command-line tool (es.exe).
    Checks common installation paths and system PATH.
    """
    common_paths = [
        r"C:\Program Files\Everything\es.exe",
        r"C:\Program Files (x86)\Everything\es.exe",
        os.path.expandvars(r"%ProgramFiles%\Everything\es.exe"),
        os.path.expandvars(r"%ProgramFiles(x86)%\Everything\es.exe"),
    ]

    for path in common_paths:
        if os.path.exists(path):
            return path

    # Try to find in PATH
    result = subprocess.run(
        ["where", "es.exe"],
        capture_output=True,
        text=True,
        shell=True
    )
    if result.returncode == 0 and result.stdout.strip():
        return result.stdout.strip().split('\n')[0]

    return None


def execute_search(query, es_path, limit=100, folder=None):
    """
    Execute a search query using Everything's CLI tool.

    Args:
        query: The search query string
        es_path: Path to es.exe
        limit: Maximum number of results to return (default: 100)
        folder: Optional folder to restrict search

    Returns:
        List of file paths matching the query, or None if search fails
    """
    cmd = [es_path, "-n", str(limit)]

    if folder:
        cmd.extend(["-path", folder])

    cmd.append(query)

    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=10
        )

        if result.returncode == 0:
            results = [line.strip() for line in result.stdout.strip().split('\n') if line.strip()]
            return results
        else:
            return None
    except subprocess.TimeoutExpired:
        return None
    except Exception as e:
        print(f"Error executing search: {e}", file=sys.stderr)
        return None


def format_results_as_markdown(query, results, limit):
    """
    Format search results as Markdown.

    Args:
        query: The original search query
        results: List of file paths
        limit: The limit that was applied

    Returns:
        Formatted Markdown string
    """
    if not results:
        return f"# Everything Search: No results\n\nNo files found matching: `{query}`"

    result_count = len(results)
    markdown = f"# Everything Search Results\n\n"
    markdown += f"**Query:** `{query}`\n"
    markdown += f"**Results:** {result_count}"

    if result_count >= limit:
        markdown += f" (limited to {limit})"

    markdown += "\n\n"

    # Format results as a list with proper escaping
    for i, path in enumerate(results, 1):
        # Escape special markdown characters
        escaped_path = path.replace("[", r"\[").replace("]", r"\]")
        markdown += f"{i}. `{escaped_path}`\n"

    return markdown


def main():
    parser = argparse.ArgumentParser(
        description="Search for files using Everything search engine"
    )
    parser.add_argument(
        "query",
        help="The search query (supports wildcards, boolean operators, etc.)"
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=100,
        help="Maximum number of results to return (default: 100)"
    )
    parser.add_argument(
        "--folder",
        help="Restrict search to a specific folder"
    )

    args = parser.parse_args()

    # Find Everything CLI tool
    es_path = find_everything_cli()
    if not es_path:
        error_msg = """# Everything Search: es.exe Not Found

The Everything search skill requires es.exe (the command-line tool).

## What's Missing?

You need the **Everything Command-Line Tool (es.exe)**, not just the Everything GUI application.

## Installation Steps

### Step 1: Verify Everything is Installed
Check if Everything.exe exists at:
- `C:\\Program Files\\Everything\\Everything.exe`
- `C:\\Program Files (x86)\\Everything\\Everything.exe`

If not found, download Everything from: https://www.voidtools.com/

### Step 2: Download es.exe
1. Visit: https://www.voidtools.com/downloads/
2. Download: "Everything Command-line tool (es.exe)"
3. Extract the es.exe file

### Step 3: Install es.exe
1. Copy es.exe to: `C:\\Program Files\\Everything\\`
2. **Note:** You may need Administrator rights
3. Verify by running: `C:\\Program Files\\Everything\\es.exe --version`

## Important Notes

- **Full vs Lite Version**: Only the Full version includes es.exe. If you have the Lite version, download the Full version.
- **Everything Service**: Does NOT need to be running for es.exe to work
- **PATH**: Alternatively, add the Everything directory to your system PATH

## Verification

After installing es.exe, run this helper script to verify:
```
python scripts/verify_es_installation.py
```

## Need Help?

See the reference materials:
- `references/faq.md` - Everything FAQ and troubleshooting
- `references/search-syntax.md` - Search syntax guide
"""
        print(error_msg)
        sys.exit(1)

    # Execute search
    results = execute_search(args.query, es_path, limit=args.limit, folder=args.folder)

    if results is None:
        error_msg = f"""# Everything Search: Query Error

The search query may be invalid or Everything encountered an error.

**Query:** `{args.query}`

Try checking:
- Query syntax (wildcards `*`, `?`, boolean operators `|`, `!`)
- Special characters that need escaping
- Everything is running and indexed

See the search syntax guide for help with advanced queries.
"""
        print(error_msg)
        sys.exit(1)

    # Format and output results
    markdown = format_results_as_markdown(args.query, results, args.limit)
    print(markdown)


if __name__ == "__main__":
    main()
