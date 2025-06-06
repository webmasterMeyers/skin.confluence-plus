#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import xbmc
import xbmcaddon
import xbmcgui
import subprocess
import sys
import os

# Get addon handle
addon = xbmcaddon.Addon()
addon_name = addon.getAddonInfo('name')

# Applications configuration
APPLICATIONS = [
    {
        'name': 'Shotwell',
        'commands': ['shotwell', '/usr/bin/shotwell'],
        'icon': 'DefaultProgram.png'
    },
    {
        'name': 'BackInTime',
        'commands': ['backintime-qt', 'backintime-gtk', '/usr/bin/backintime-qt', '/usr/bin/backintime-gtk'],
        'icon': 'DefaultProgram.png'
    }
]

def find_executable(commands):
    """Find the first available executable from a list of possible commands"""
    for cmd in commands:
        # Check if it's an absolute path
        if cmd.startswith('/'):
            if os.path.isfile(cmd) and os.access(cmd, os.X_OK):
                return cmd
        else:
            # Check if command is in PATH
            try:
                result = subprocess.run(['which', cmd], capture_output=True, text=True)
                if result.returncode == 0 and result.stdout.strip():
                    return result.stdout.strip()
            except:
                continue
    return None

def launch_application(app_config):
    """Launch a Linux application"""
    try:
        executable = find_executable(app_config['commands'])
        
        if not executable:
            xbmcgui.Dialog().notification(addon_name, f"{app_config['name']} not found", xbmcgui.NOTIFICATION_ERROR)
            return False
        
        xbmc.log(f"[{addon_name}] Launching: {executable}", xbmc.LOGINFO)
        
        # Launch the application
        subprocess.Popen([executable], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        
        return True
        
    except Exception as e:
        xbmc.log(f"[{addon_name}] Error launching {app_config['name']}: {str(e)}", xbmc.LOGERROR)
        xbmcgui.Dialog().notification(addon_name, f"Error: {str(e)}", xbmcgui.NOTIFICATION_ERROR)
        return False

def show_applications_menu():
    """Show the applications selection dialog"""
    
    # Create list of application names for the dialog
    app_names = [app['name'] for app in APPLICATIONS]
    
    # Show selection dialog
    dialog = xbmcgui.Dialog()
    selected = dialog.select("Select Application", app_names)
    
    if selected >= 0:
        app = APPLICATIONS[selected]
        xbmc.log(f"[{addon_name}] User selected: {app['name']}", xbmc.LOGINFO)
        
        # Show loading notification
        xbmcgui.Dialog().notification(addon_name, f"Launching {app['name']}...", xbmcgui.NOTIFICATION_INFO, 2000)
        
        # Launch the application
        if launch_application(app):
            xbmc.log(f"[{addon_name}] Successfully launched {app['name']}", xbmc.LOGINFO)
        else:
            xbmc.log(f"[{addon_name}] Failed to launch {app['name']}", xbmc.LOGERROR)

if __name__ == '__main__':
    xbmc.log(f"[{addon_name}] Starting applications launcher", xbmc.LOGINFO)
    show_applications_menu() 