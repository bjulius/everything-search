# Everything Search Installation Guide

## Table of Contents
- [Quick Setup](#quick-setup)
- [Detailed Installation](#detailed-installation)
- [Verification](#verification)
- [Troubleshooting](#troubleshooting)
- [Alternative: PATH Configuration](#alternative-path-configuration)

---

## Quick Setup

1. Download **Everything (Full version)** from https://www.voidtools.com/
2. Install Everything normally
3. Download **es.exe** from https://www.voidtools.com/downloads/ → "Everything Command-line tool"
4. Copy es.exe to `C:\Program Files\Everything\`
5. Restart terminal/IDE

---

## Detailed Installation

### Prerequisites

- **Everything application** - The main search engine
- **es.exe** - The command-line interface (separate download)

### Important: es.exe vs Everything.exe

| File | Purpose | Required |
|------|---------|----------|
| Everything.exe | GUI application | Optional |
| es.exe | Command-line tool | **Required for this skill** |

The Full version of Everything includes both. The Lite version includes only the GUI.

### Step 1: Verify Everything is Installed

Check if Everything.exe exists:
- `C:\Program Files\Everything\Everything.exe`
- `C:\Program Files (x86)\Everything\Everything.exe`

If not found, download from https://www.voidtools.com/

### Step 2: Download es.exe

1. Go to https://www.voidtools.com/downloads/
2. Find "Everything Command-line tool"
3. Download the appropriate version (32-bit or 64-bit)
4. Extract the es.exe file

### Step 3: Install es.exe

1. Copy es.exe to: `C:\Program Files\Everything\`
2. Administrator rights may be required
3. Restart any command prompts or terminal windows

---

## Verification

Run the verification helper:
```bash
python scripts/verify_es_installation.py
```

Expected output:
```
STATUS: es.exe READY
SUCCESS! Everything Search skill is ready to use.
```

Or test manually:
```bash
"C:\Program Files\Everything\es.exe" --version
```

---

## Troubleshooting

### "es.exe not found" error
- Run `verify_es_installation.py` to diagnose
- Check if Everything is actually installed
- Verify es.exe is in `C:\Program Files\Everything\`
- Verify the Full version of Everything is installed (not Lite)

### "Everything Service" not required
- es.exe works independently
- The Everything Service/GUI does NOT need to be running
- The skill operates without opening the Everything GUI

### Permission issues
- If you get permission errors, copy es.exe as Administrator
- Right-click Command Prompt → "Run as administrator"

### Lite vs Full Version
If you installed the Lite version:
1. Uninstall Everything Lite
2. Download Everything Full from voidtools.com
3. Install and then add es.exe

---

## Alternative: PATH Configuration

Instead of copying es.exe to Program Files, add the Everything directory to your system PATH:

1. Open Environment Variables:
   - Press Win+X, select "System"
   - Click "Advanced system settings"
   - Click "Environment Variables"

2. Under "User variables" or "System variables":
   - Find PATH and click "Edit"
   - Click "New"
   - Add: `C:\Program Files\Everything\`
   - Click OK

3. Restart your terminal/IDE
