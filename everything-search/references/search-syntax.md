# Everything Search Syntax Guide

This guide covers the practical search syntax for Everything search queries. Use these patterns when calling the search wrapper.

## Basic Searches

### Filename Search
Simply type a partial filename:
```
document
report
```
Results: All files/folders containing "document" or "report" in the name

### File Type/Extension
```
*.pdf
*.mp3
*.docx
```
Results: All files with the specified extension

### Multiple Extensions
```
*.bmp|*.jpg|*.png
*.doc|*.docx
```
Results: Files matching any of the specified extensions (OR logic)

## Wildcards

### Asterisk (*)
Matches any number of characters:
```
e*g        matches: egg, everything, editing
*.exe      matches: calc.exe, notepad.exe
test*.py   matches: test_main.py, testing.py
```

### Question Mark (?)
Matches exactly one character:
```
?.txt           matches: a.txt, b.txt (single character files)
*.??            matches: file.py, code.js (two-letter extensions)
test_?.log      matches: test_1.log, test_a.log
```

## Boolean Operators

### AND (default)
Space between terms means AND:
```
python script
```
Results: Files containing both "python" AND "script"

### OR
Use pipe `|` to match either term:
```
jpg|png
document|report
```
Results: Files containing either "jpg" OR "png"

### NOT
Use `!` to exclude terms:
```
!.exe
temp !backup
```
Results: All files except .exe / All "temp" files except "backup"

## Location-Based Searches

### Search in Specific Folder
Use double backslash `\\` to restrict to a location:
```
downloads\\ .mp3
documents\\ invoice
C:\Users\john\Pictures\\ *.jpg
```
Results: Files matching the pattern in the specified folder only

Note: Everything searches recursively within the folder

### Alternative: Match Path
Enable "Match Path" option and use:
```
downloads .avi
Pictures invoice
```
Same effect as using `\\` syntax

## Content Search

### Search File Contents
Use `content:` prefix (slower, not indexed):
```
content:password
content:api_key
```
Results: Files containing the specified text in their contents

Note: File content is not indexed, so these searches are slower. Use for small searches or when filename matching isn't enough.

## Advanced: Wildcards with Operators

### Combine wildcards with boolean logic
```
*.py|*.js          Python or JavaScript files
test*.py !backup   Test files except backups
!temp* *.log       Log files not in temp folders
```

## Advanced: Regex (When Needed)

Enable "Enable Regex" in search options, then use regex patterns:
```
.*\.py$            All Python files
[0-9]{3}-[0-9]{4}  Phone number pattern
```

Note: Only needed for complex pattern matching. Wildcards are usually simpler.

## Common Search Examples

| Task | Query | Notes |
|------|-------|-------|
| Find all PDFs | `*.pdf` | Simple extension search |
| Find PDFs in Documents | `documents\\ *.pdf` | Location-restricted |
| Find backup files | `*backup*` | Wildcard matching |
| Find logs except temp | `!temp* *.log` | Boolean NOT operator |
| Find Python or Ruby files | `*.py\|*.rb` | Multiple extensions |
| Find recent cache | `~cache !system` | Exclude system folders |
| Find config files | `*.config\|*.cfg\|*.ini` | Multiple config formats |
| Find by partial name | `screen* !lock` | Partial match, exclude variations |

## Tips for Effective Searching

1. **Start Simple**: Begin with basic wildcards before complex operators
2. **Use AND by Default**: Spaces automatically AND terms together
3. **Content Search Sparingly**: Use `content:` only when needed; it's slower
4. **Location Restriction**: Use `\\` prefix for large searches to reduce results
5. **Test Syntax**: If a search isn't working, check the syntax in Everything's Help menu
6. **Combine Operators**: Mix AND, OR, and NOT for precise results

## When Searches Aren't Working

- Check that search options aren't enabled (Match Case, Match Whole Word, etc.) unless intentional
- Verify Everything is running and database is indexed
- Try a simpler query to test
- See the FAQ for troubleshooting tips
