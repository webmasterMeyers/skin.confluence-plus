import xbmc
import xbmcgui
import xbmcaddon
import subprocess
import os

# Add debug logging
xbmc.log("Streaming Launcher Script Started", xbmc.LOGDEBUG)

def launch_streaming_service(url):
    try:
        xbmc.log(f"Attempting to launch streaming service: {url}", xbmc.LOGDEBUG)
        # Get the path to brave-browser
        brave_path = "/usr/bin/brave-browser"
        if not os.path.exists(brave_path):
            xbmc.log("Brave browser not found at: " + brave_path, xbmc.LOGERROR)
            xbmcgui.Dialog().notification("Error", "Brave browser not found", xbmcgui.NOTIFICATION_ERROR)
            return

        # Launch brave in kiosk mode
        xbmc.log(f"Launching brave with command: {brave_path} --kiosk {url}", xbmc.LOGDEBUG)
        subprocess.Popen([brave_path, "--kiosk", url])
    except Exception as e:
        xbmc.log(f"Error launching streaming service: {str(e)}", xbmc.LOGERROR)
        xbmcgui.Dialog().notification("Error", str(e), xbmcgui.NOTIFICATION_ERROR)

def main():
    xbmc.log("Streaming Launcher main() started", xbmc.LOGDEBUG)
    # Create a list of streaming services
    services = [
        ("Angel Studios", "https://www.angel.com/watch"),
        ("PureFlix", "https://www.pureflix.com/watch"),
        ("Dove Channel", "https://www.dovechannel.com/watch"),
        ("YouTube", "https://www.youtube.com")
    ]
    
    # Show selection dialog
    dialog = xbmcgui.Dialog()
    items = [service[0] for service in services]
    xbmc.log("Showing streaming services dialog", xbmc.LOGDEBUG)
    selected = dialog.select("Select Streaming Service", items)
    
    if selected >= 0:
        xbmc.log(f"User selected: {services[selected][0]}", xbmc.LOGDEBUG)
        launch_streaming_service(services[selected][1])
    else:
        xbmc.log("User cancelled selection", xbmc.LOGDEBUG)

if __name__ == "__main__":
    xbmc.log("Streaming Launcher script __main__", xbmc.LOGDEBUG)
    main() 