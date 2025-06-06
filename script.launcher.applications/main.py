#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import xbmc
import xbmcaddon
import xbmcgui
import subprocess
import sys
import os
import json

# Get addon handle
addon = xbmcaddon.Addon()
addon_name = addon.getAddonInfo('name')

def load_applications():
    """Load applications from JSON config file"""
    config_file = os.path.join(os.path.dirname(__file__), 'applications.json')
    
    # Default applications if config file doesn't exist
    default_apps = [
        {'name': 'Shotwell', 'command': 'shotwell', 'enabled': True},
        {'name': 'BackInTime', 'command': 'backintime-qt', 'enabled': True}
    ]
    
    try:
        if os.path.exists(config_file):
            with open(config_file, 'r') as f:
                apps = json.load(f)
            xbmc.log(f"[{addon_name}] Loaded {len(apps)} applications from config", xbmc.LOGINFO)
        else:
            apps = default_apps
            xbmc.log(f"[{addon_name}] Using default applications", xbmc.LOGINFO)
        
        # Filter to only enabled apps and convert to expected format
        enabled_apps = []
        for app in apps:
            if app.get('enabled', True):
                # Split command by spaces and commas to support alternatives
                commands = [cmd.strip() for cmd in app['command'].replace(',', ' ').split()]
                enabled_apps.append({
                    'name': app['name'],
                    'commands': commands,
                    'icon': 'DefaultProgram.png'
                })
        
        return enabled_apps
        
    except Exception as e:
        xbmc.log(f"[{addon_name}] Error loading config: {str(e)}", xbmc.LOGERROR)
        return [{'name': a['name'], 'commands': [a['command']], 'icon': 'DefaultProgram.png'} for a in default_apps]

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
    
    # Load applications from config
    applications = load_applications()
    
    if not applications:
        xbmcgui.Dialog().notification(addon_name, "No applications configured", xbmcgui.NOTIFICATION_WARNING)
        return
    
    # Create list of application names for the dialog
    app_names = [app['name'] for app in applications]
    
    # Show selection dialog
    dialog = xbmcgui.Dialog()
    selected = dialog.select("Select Application", app_names)
    
    if selected >= 0:
        app = applications[selected]
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