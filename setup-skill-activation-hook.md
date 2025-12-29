# How to Create a Skill Activation Hook

This guide explains how to create a Claude Code hook that announces a skill at session startup—just like the everything-search skill.

## Overview

Claude Code **hooks** are shell commands that run automatically at specific events. A `SessionStart` hook can inject a message into Claude's context at the beginning of every conversation, making it aware of available skills.

## Quick Setup

### 1. Locate Your Settings File

```
C:\Users\<username>\.claude\settings.json
```

### 2. Add the Hook Configuration

Add or modify the `hooks` section in your settings.json:

```json
{
  "hooks": {
    "SessionStart": [
      {
        "matcher": "",
        "hooks": [
          {
            "type": "command",
            "command": "powershell -Command \"Write-Output 'SKILL LOADED: <skill-name> - <brief description>. Usage: <usage syntax>. Trigger on: <trigger phrases>.'\""
          }
        ]
      }
    ]
  }
}
```

### 3. Customize the Message

Replace the placeholders:

| Placeholder | Description | Example |
|-------------|-------------|---------|
| `<skill-name>` | Short identifier | `everything-search` |
| `<brief description>` | What the skill does | `Instant Windows file search via Everything` |
| `<usage syntax>` | How to invoke it | `python scripts/search.py [query]` |
| `<trigger phrases>` | When Claude should use it | `find, locate, search for files` |

## Complete Example

Here's the everything-search hook:

```json
{
  "hooks": {
    "SessionStart": [
      {
        "matcher": "",
        "hooks": [
          {
            "type": "command",
            "command": "powershell -Command \"Write-Output 'SKILL LOADED: everything-search - Instant Windows file search via Everything. Usage: python C:\\Users\\brjul\\.claude\\skills\\everything-search\\scripts\\search.py [query] [--limit N] [--folder PATH]. Patterns: *.ext, partial names, OR (|), NOT (!). Trigger on: find, locate, search for files.'\""
          }
        ]
      }
    ]
  }
}
```

## Multiple Skills

To register multiple skills, add multiple hook entries:

```json
{
  "hooks": {
    "SessionStart": [
      {
        "matcher": "",
        "hooks": [
          {
            "type": "command",
            "command": "powershell -Command \"Write-Output 'SKILL LOADED: skill-one - Description...'\""
          },
          {
            "type": "command",
            "command": "powershell -Command \"Write-Output 'SKILL LOADED: skill-two - Description...'\""
          }
        ]
      }
    ]
  }
}
```

## Tips

- **Keep messages concise** — Claude reads this every session
- **Include trigger phrases** — Helps Claude know when to use the skill
- **Use full paths** — Avoid ambiguity in script locations
- **Test the command** — Run the PowerShell command directly first to verify output

## Hook Types Reference

| Event | When It Runs |
|-------|--------------|
| `SessionStart` | Beginning of each conversation |
| `PreToolUse` | Before a tool executes |
| `PostToolUse` | After a tool executes |
| `Stop` | When Claude finishes responding |

## Troubleshooting

**Hook not firing?**
- Verify JSON syntax (use a JSON validator)
- Restart Claude Code after editing settings.json
- Check that the `matcher` field is `""` (empty matches all)

**Message not appearing?**
- Test the PowerShell command in terminal first
- Escape backslashes properly (`\\` in JSON)
- Check for quote escaping issues
