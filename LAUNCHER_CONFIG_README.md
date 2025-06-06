# Kodi Launcher Configuration

## Overview
Both the Streaming Launcher and Applications Launcher can be easily configured by editing simple JSON files.

## Streaming Services Configuration

**File Location:** `~/.kodi/addons/script.launcher.streaming/services.json`

**Format:**
```json
[
    {
        "name": "Service Name",
        "url": "https://example.com",
        "enabled": true
    }
]
```

**Example:**
```json
[
    {
        "name": "Netflix",
        "url": "https://netflix.com",
        "enabled": true
    },
    {
        "name": "Disney+",
        "url": "https://www.disneyplus.com",
        "enabled": false
    }
]
```

## Applications Configuration

**File Location:** `~/.kodi/addons/script.launcher.applications/applications.json`

**Format:**
```json
[
    {
        "name": "Application Name",
        "command": "command-to-run",
        "enabled": true
    }
]
```

**Example:**
```json
[
    {
        "name": "GIMP",
        "command": "gimp",
        "enabled": true
    },
    {
        "name": "File Manager",
        "command": "nautilus",
        "enabled": false
    }
]
```

## Usage Instructions

1. **Edit the JSON files** using any text editor
2. **Set enabled to true/false** to show/hide items
3. **Restart Kodi** or reload the addons for changes to take effect

## Command Examples for Applications

- `"gimp"` - Launch GIMP
- `"libreoffice --writer"` - Launch LibreOffice Writer
- `"gnome-terminal"` - Launch Terminal
- `"nautilus"` - Launch File Manager
- `"firefox"` - Launch Firefox browser

## URL Examples for Streaming Services

- `"https://netflix.com"`
- `"https://www.youtube.com"`
- `"https://www.disneyplus.com"`
- `"http://localhost:8096"` - Local Jellyfin server
- `"http://192.168.1.100:32400/web"` - Local Plex server

## Notes

- Services/apps with `"enabled": false` will not appear in the menus
- Changes require Kodi restart to take effect
- Invalid JSON will fall back to default configurations
- Commands are searched in system PATH automatically 