import xbmc
import xbmcgui
import xbmcaddon
import subprocess
import os

def launch_streaming_service(url):
    try:
        # Get the path to brave-browser
        brave_path = "/usr/bin/brave-browser"
        if not os.path.exists(brave_path):
            xbmcgui.Dialog().notification("Error", "Brave browser not found", xbmcgui.NOTIFICATION_ERROR)
            return

        # Launch brave in kiosk mode
        subprocess.Popen([brave_path, "--kiosk", url])
    except Exception as e:
        xbmcgui.Dialog().notification("Error", str(e), xbmcgui.NOTIFICATION_ERROR)

def main():
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
    selected = dialog.select("Select Streaming Service", items)
    
    if selected >= 0:
        launch_streaming_service(services[selected][1])

if __name__ == "__main__":
    main() 