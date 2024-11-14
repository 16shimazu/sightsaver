import subprocess, time, plyer
while True:
    time.sleep(1200)
    plyer.notification.notify(title="SightSaver", message="Your health matters. Look 20 feet away from your screen for 20 seconds.", timeout=20)