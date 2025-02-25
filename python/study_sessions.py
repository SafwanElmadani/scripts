import time
import subprocess

# Set the study and break intervals (in seconds)
study_time = 25 * 60   # 50 minutes
break_time = 10 * 60   # 10 minutes

def send_notification(title, message):
    """Send a notification using notify-send (dunst compatible)."""
    subprocess.run(["notify-send", "-u", "normal", title, message])

def main():
    while True:
        # Study period
        send_notification("Study Time!", "Focus for the next 25 minutes.")
        subprocess.run(["paplay", "/usr/share/sounds/freedesktop/stereo/service-login.oga"])
        time.sleep(study_time)

        # Break period
        send_notification("Break Time!", "Take a 10-minute break.")
        subprocess.run(["paplay", "/usr/share/sounds/freedesktop/stereo/alarm-clock-elapsed.oga"])
        time.sleep(break_time)

if __name__ == "__main__":
    main()

