import xbmc
import xbmcgui
import xbmcaddon
import subprocess
import os

# Add debug logging
xbmc.log("Applications Launcher Script Started", xbmc.LOGDEBUG)

def launch_application(app_name, command):
    try:
        xbmc.log(f"Attempting to launch application: {app_name} with command: {command}", xbmc.LOGDEBUG)
        # Launch the application
        subprocess.Popen([command])
        xbmc.log(f"Successfully launched {app_name}", xbmc.LOGDEBUG)
    except Exception as e:
        xbmc.log(f"Failed to launch {app_name}: {str(e)}", xbmc.LOGERROR)
        xbmcgui.Dialog().notification("Error", f"Failed to launch {app_name}: {str(e)}", xbmcgui.NOTIFICATION_ERROR)

def main():
    xbmc.log("Applications Launcher main() started", xbmc.LOGDEBUG)
    # Create a list of applications
    applications = [
        ("Shotwell", "shotwell"),
        ("BackInTime", "backintime-qt4")
    ]
    
    # Show selection dialog
    dialog = xbmcgui.Dialog()
    items = [app[0] for app in applications]
    xbmc.log("Showing applications dialog", xbmc.LOGDEBUG)
    selected = dialog.select("Select Application", items)
    
    if selected >= 0:
        xbmc.log(f"User selected: {applications[selected][0]}", xbmc.LOGDEBUG)
        launch_application(applications[selected][0], applications[selected][1])
    else:
        xbmc.log("User cancelled selection", xbmc.LOGDEBUG)

if __name__ == "__main__":
    xbmc.log("Applications Launcher script __main__", xbmc.LOGDEBUG)
    main() 