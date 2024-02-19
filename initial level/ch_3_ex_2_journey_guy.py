import json
import psutil
import tkinter as tk
from tkinter import messagebox

class PomodoroTracker:
    def __init__(self, config_file="config.json"):
        self.config_file = config_file
        self.load_config()

        self.root = tk.Tk()
        self.root.title("Pomodoro Tracker")
        self.root.geometry("300x200")

        self.label = tk.Label(self.root, text="Choose process to track:")
        self.label.pack()

        self.process_entry = tk.Entry(self.root)
        self.process_entry.pack()

        self.start_button = tk.Button(self.root, text="Start Tracking", command=self.start_tracking)
        self.start_button.pack()

        self.root.protocol("WM_DELETE_WINDOW", self.on_close)
        self.root.mainloop()

    def start_tracking(self):
        process_name = self.process_entry.get()
        if process_name:
            self.config["process_name"] = process_name
            self.save_config()
            self.root.withdraw()  # Hide the main window
            self.monitor_process()

    def monitor_process(self):
        while True:
            if self.config["process_name"] in (p.name() for p in psutil.process_iter()):
                messagebox.showinfo("Reminder", f"Process '{self.config['process_name']}' is still running.")
            else:
                messagebox.showinfo("Reminder", f"Process '{self.config['process_name']}' is not running anymore.")
                break

    def load_config(self):
        try:
            with open(self.config_file, "r") as f:
                self.config = json.load(f)
        except FileNotFoundError:
            self.config = {"process_name": ""}

    def save_config(self):
        with open(self.config_file, "w") as f:
            json.dump(self.config, f)

    def on_close(self):
        self.save_config()
        self.root.destroy()

if __name__ == "__main__":
    app = PomodoroTracker()
