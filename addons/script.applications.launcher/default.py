import xbmc
import xbmcgui
import xbmcaddon
import subprocess
import os

def launch_application(app_name, command):
    try:
        # Launch the application
        subprocess.Popen([command])
    except Exception as e:
        xbmcgui.Dialog().notification("Error", f"Failed to launch {app_name}: {str(e)}", xbmcgui.NOTIFICATION_ERROR)

def main():
    # Create a list of applications
    applications = [
        ("Shotwell", "shotwell"),
        ("BackInTime", "backintime-qt4")
    ]
    
    # Show selection dialog
    dialog = xbmcgui.Dialog()
    items = [app[0] for app in applications]
    selected = dialog.select("Select Application", items)
    
    if selected >= 0:
        launch_application(applications[selected][0], applications[selected][1])

if __name__ == "__main__":
    main() 