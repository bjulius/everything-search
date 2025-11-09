#!/usr/bin/env python3
r"""
Everything CLI (es.exe) Installation Verification Helper

This script helps users verify that es.exe is installed and configured correctly.
It provides clear guidance on how to obtain and install es.exe if needed.

Usage:
    python verify_es_installation.py
"""

import subprocess
import sys
import os
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
    try:
        result = subprocess.run(
            ["where", "es.exe"],
            capture_output=True,
            text=True,
            shell=True,
            timeout=5
        )
        if result.returncode == 0 and result.stdout.strip():
            return result.stdout.strip().split('\n')[0]
    except Exception:
        pass

    return None


def test_es_execution(es_path):
    """
    Test that es.exe can be executed successfully.
    """
    try:
        result = subprocess.run(
            [es_path, "--version"],
            capture_output=True,
            text=True,
            timeout=5
        )
        return result.returncode == 0, result.stdout + result.stderr
    except Exception as e:
        return False, str(e)


def main():
    """
    Main verification routine.
    """
    print("=" * 70)
    print("Everything CLI (es.exe) Installation Verification")
    print("=" * 70)
    print()

    # Step 1: Check if es.exe is found
    es_path = find_everything_cli()

    if not es_path:
        print("STATUS: es.exe NOT FOUND")
        print()
        print("The Everything search skill requires es.exe (the command-line tool).")
        print()
        print("WHAT TO DO:")
        print("-" * 70)
        print()
        print("1. Verify Everything is installed:")
        print("   - Look for: C:\\Program Files\\Everything\\Everything.exe")
        print()
        print("2. Download es.exe:")
        print("   - Visit: https://www.voidtools.com/downloads/")
        print("   - Download: 'Everything Command-line tool (es.exe)'")
        print()
        print("3. Install es.exe:")
        print("   - Extract the es.exe file")
        print("   - Place it in: C:\\Program Files\\Everything\\")
        print("   - Note: The Lite version doesn't include es.exe - use Full version")
        print()
        print("4. Verify installation:")
        print("   - Run this script again to confirm")
        print()
        print("TROUBLESHOOTING:")
        print("-" * 70)
        print("- Ensure you're using the Full version of Everything (not Lite)")
        print("- The Everything Service doesn't need to be running for es.exe to work")
        print("- You may need Administrator rights to place es.exe in Program Files")
        print()
        return 1

    # Step 2: Verify es.exe can execute
    print(f"FOUND: {es_path}")
    print()
    print("Testing es.exe execution...")

    success, output = test_es_execution(es_path)

    if not success:
        print("STATUS: es.exe FOUND but NOT EXECUTABLE")
        print()
        print(f"Error: {output}")
        print()
        print("TROUBLESHOOTING:")
        print("-" * 70)
        print("- Verify the file is not corrupted")
        print("- Try re-downloading es.exe from voidtools.com")
        print("- Check file permissions (should be readable/executable)")
        print()
        return 1

    # Success
    print("STATUS: es.exe READY")
    print()
    print("SUCCESS! Everything Search skill is ready to use.")
    print()
    print(f"Location: {es_path}")
    print()
    print("You can now use the Everything Search skill to:")
    print("- Find files instantly by name or pattern")
    print("- Use advanced search syntax (wildcards, boolean operators)")
    print("- Restrict searches to specific locations")
    print()
    return 0


if __name__ == "__main__":
    sys.exit(main())
