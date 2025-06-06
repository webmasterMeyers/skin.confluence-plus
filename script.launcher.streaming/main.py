#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import xbmc
import xbmcaddon
import xbmcgui
import subprocess
import sys

# Get addon handle
addon = xbmcaddon.Addon()
addon_name = addon.getAddonInfo('name')

# Streaming services configuration
STREAMING_SERVICES = [
    {
        'name': 'Angel Studios',
        'url': 'https://www.angel.com/',
        'icon': 'DefaultVideo.png'
    },
    {
        'name': 'PureFlix',
        'url': 'https://www.pureflix.com/',
        'icon': 'DefaultVideo.png'
    },
    {
        'name': 'Dove Channel',
        'url': 'https://www.dovechannel.com/',
        'icon': 'DefaultVideo.png'
    },
    {
        'name': 'YouTube',
        'url': 'https://www.youtube.com/',
        'icon': 'DefaultVideo.png'
    }
]

def launch_brave_kiosk(url):
    """Launch Brave browser in kiosk mode with the specified URL"""
    try:
        # Try common Brave browser paths
        brave_paths = [
            '/usr/bin/brave-browser',
            '/usr/bin/brave',
            '/opt/brave.com/brave/brave-browser',
            '/snap/bin/brave',
            '/usr/local/bin/brave'
        ]
        
        brave_cmd = None
        for path in brave_paths:
            try:
                # Check if brave exists at this path
                subprocess.run([path, '--version'], capture_output=True, check=True)
                brave_cmd = path
                break
            except (subprocess.CalledProcessError, FileNotFoundError):
                continue
        
        if not brave_cmd:
            xbmcgui.Dialog().notification(addon_name, "Brave browser not found", xbmcgui.NOTIFICATION_ERROR)
            return False
        
        # Launch Brave in kiosk mode
        cmd = [brave_cmd, '--kiosk', '--disable-features=TranslateUI', '--disable-extensions', url]
        
        xbmc.log(f"[{addon_name}] Launching: {' '.join(cmd)}", xbmc.LOGINFO)
        
        # Launch the process
        subprocess.Popen(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        
        return True
        
    except Exception as e:
        xbmc.log(f"[{addon_name}] Error launching Brave: {str(e)}", xbmc.LOGERROR)
        xbmcgui.Dialog().notification(addon_name, f"Error: {str(e)}", xbmcgui.NOTIFICATION_ERROR)
        return False

def show_streaming_menu():
    """Show the streaming services selection dialog"""
    
    # Create list of service names for the dialog
    service_names = [service['name'] for service in STREAMING_SERVICES]
    
    # Show selection dialog
    dialog = xbmcgui.Dialog()
    selected = dialog.select("Select Streaming Service", service_names)
    
    if selected >= 0:
        service = STREAMING_SERVICES[selected]
        xbmc.log(f"[{addon_name}] User selected: {service['name']}", xbmc.LOGINFO)
        
        # Show loading notification
        xbmcgui.Dialog().notification(addon_name, f"Launching {service['name']}...", xbmcgui.NOTIFICATION_INFO, 2000)
        
        # Launch the service
        if launch_brave_kiosk(service['url']):
            xbmc.log(f"[{addon_name}] Successfully launched {service['name']}", xbmc.LOGINFO)
        else:
            xbmc.log(f"[{addon_name}] Failed to launch {service['name']}", xbmc.LOGERROR)

if __name__ == '__main__':
    xbmc.log(f"[{addon_name}] Starting streaming launcher", xbmc.LOGINFO)
    show_streaming_menu() 