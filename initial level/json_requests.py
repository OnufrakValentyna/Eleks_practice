import psutil
import json
import time
import threading
import win32gui
import pystray
from pystray import MenuItem as item
from PIL import Image

class WindowWatcher:
    def __init__(self):
        self.active_windows = {}
        self.config = self.load_config()
        self.running = True
        self.last_active_time = time.time()

    def load_config(self):
        try:
            with open('config.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return {"tracked_program": "notepad.exe", "work_duration": 25, "break_duration": 5}

    def save_config(self):
        with open('config.json', 'w') as f:
            json.dump(self.config, f)

    def track_windows(self):
        while self.running:
            active_window = win32gui.GetWindowText(win32gui.GetForegroundWindow())
            if active_window.endswith(self.config["tracked_program"]):
                self.last_active_time = time.time()
            time.sleep(1)

    def check_activity(self):
        while self.running:
            current_time = time.time()
            if current_time - self.last_active_time > self.config["work_duration"] * 60:
                self.notify("Time for a break!")
                time.sleep(self.config["break_duration"] * 60)
                self.last_active_time = time.time()
            time.sleep(1)

    def notify(self, message):
        # Implement notification logic
        pass

    def run(self):
        threading.Thread(target=self.track_windows).start()
        threading.Thread(target=self.check_activity).start()

def on_quit_callback(icon, item):
    icon.stop()

def main():
    watcher = WindowWatcher()
    watcher.run()

    image = Image.open("icon.png")
    menu = (item('Quit', on_quit_callback),)
    icon = pystray.Icon("name", image, "title", menu)
    icon.run()

if __name__ == "__main__":
    main()
