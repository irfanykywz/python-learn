from plyer import notification
import time

# Desktop Notification with custom icon
notification.notify(
    title='Reminder',
    message='Please take a break!',
    # app_icon='C:/path/to/icon.ico', # optional
    timeout=10, # notification stays for 10 seconds
)

# This is just a pause for the demonstration. 
# You can remove it from your actual code.
time.sleep(15)

# Notification without icon
notification.notify(
    title='Another Reminder',
    message='Your lunch is ready!',
    timeout=10, # notification stays for 10 seconds
)