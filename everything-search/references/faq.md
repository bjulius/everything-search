# Everything FAQ - Complete Guide

## Everything Section

### What is "Everything"?
A search engine for Windows that locates files and folders by filename instantly. Unlike Windows search, it initially displays every file and folder on your computer.

### How long will it take to index my files?
Indexing only covers file and folder names:
- Fresh Windows 10 install (~120,000 files): ~1 second
- 1,000,000 files: ~1 minute

### Does Everything search file contents?
Yes, using the `content:` search function. However, file content is not indexed, making content searches slower than filename searches.

### Does "Everything" hog my system resources?
No. Resource usage examples:
- Windows 10 (~120,000 files): ~14 MB RAM, <9 MB disk
- 1,000,000 files: ~75 MB RAM, 45 MB disk

### Does "Everything" monitor file system changes?
Yes. Search results update in real-time. NTFS indexes automatically stay current via the NTFS USN Journal, and changes aren't missed even when the application is closed.

### Is "Everything" free?
Yes, it's freeware. Donations are appreciated.

### Does "Everything" contain malware, spyware or adware?
No malicious software is included.

### Does "Everything" miss changes if not running?
No. The database updates upon startup, and NTFS USN Journal maintenance ensures no changes are missed across restarts.

### What are the system requirements?
Runs on Windows XP, Vista, 7, 8, 10, and 11. NTFS indexing requires the service or administrator privileges.

### What is the Lite version?
The standard multilingual version with removed features:
- No ETP/FTP Server
- No HTTP Server
- No IPC
- Command line/ES incompatible
- SDK incompatible
- Accessibility features unavailable

### How do I index a FAT volume?
1. Tools > Options
2. Click Folders tab
3. Click Add...
4. Select FAT volume and click OK
5. Click OK

### How do I index a mapped network drive/NAS/Network share?
1. Tools > Options
2. Click Folders tab
3. Click Add...
4. Select the network location
5. Click OK twice

If not listed, try running as standard user with the service enabled.

### How do I convert a volume to NTFS?
⚠️ **Backup important data first.** NTFS conversion is permanent.

In Command Prompt:
```
convert D: /fs:ntfs
```
(Replace D: with your drive letter)

### How do I install "Everything"?
See the basic installation guide in the support documentation.

### How do I use "Everything"?
Refer to the basic usage guide in support documentation.

### Why is "Everything" 1.4 using more memory than 1.3?
Version 1.4 indexes file sizes and dates by default, plus stores additional sorting information. This can be optimized in settings.

### How do I prevent the UAC prompt?
Administrative privileges are required for NTFS indexing. Avoid UAC by:
1. Running as standard user
2. Installing the "Everything" service, OR
3. Disabling NTFS indexing

---

## Searching Section

### How do I search for a file or folder?
Type the partial name into the search box. Results appear instantly.

### How do I use boolean operators?
- **AND** (default): `abc 123` finds both terms
- **OR**: `abc | 123` finds either term
- **NOT**: `!abc` excludes the term

Access syntax help via Help > Search syntax.

### How do I use wildcards?
- `*` matches any number of characters: `e*g`
- `?` matches one character: `*.??` (two-letter extensions)

### How do I include spaces in my search?
Enclose the search in double quotes: `"foo bar"`

### How do I search for a file type?
Type the extension: `*.mp3`

Multiple types: `*.bmp|*.jpg`

### How do I search for files in a specific location?
Include `\\` in the search: `downloads\\ .mp3`

Alternatively, enable Match Path and use: `downloads .avi`

### Advanced searching
See Advanced Search documentation for detailed information.

---

## Troubleshooting Section

### Search doesn't find what I want
**Verify search options are unchecked:**
- Match Case
- Match Whole Word
- Match Path
- Match Diacritics
- Enable Regex

**Ensure "Everything" filter is selected** in Search menu.

**Verify installation:**
1. Tools > Options > General
2. Check "Store settings in %APPDATA%\Everything"
3. Check "Everything Service"
4. Uncheck "Run as administrator"
5. Exit and restart

**Verify non-NTFS volumes are included** in Folders tab.

**Force a rebuild:** Tools > Options > Indexes > Force Rebuild

### Settings are not saved
Enable "Store settings and data in %APPDATA%\Everything":
1. Tools > Options > General tab
2. Check the option
3. Click OK

### Duplicated results
NTFS volumes are automatically indexed. Remove them from folder indexes:
1. Tools > Options > Folders tab
2. Select NTFS volumes
3. Click Remove

Check the NTFS tab to see which volumes are automatically included.

### The result list is empty or contains only drives
**Ensure the service is running:**
1. Tools > Options > General
2. Check "Everything Service"
3. Click OK

**OR run as administrator:**
1. Tools > Options > General
2. Check "Run as administrator"
3. Click OK

**Ensure at least one local NTFS volume exists**, and enable indexing:
1. Tools > Options > NTFS tab
2. For each volume: check "Include in database" and "Monitor changes"

**Force database rebuild:** Tools > Options > Indexes > Force Rebuild
