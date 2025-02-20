import tkinter as tk
import json
from home_page import HomePage

DATA_FILE = "data.json"

class RemindersPage(tk.Frame):
    def __init__(self, root, controller):
        super().__init__(root)
        self.controller = controller
        self.configure(bg="#ffffff")

        tk.Label(self, text="Manage Your Reminders", font=("Arial", 14, "bold"), bg="#ffffff").pack(pady=10)
        
        self.reminder_listbox = tk.Listbox(self, width=50, height=10)
        self.reminder_listbox.pack(pady=10)
        
        self.load_reminders()
        
        tk.Button(self, text="Remove Selected Reminder", font=("Arial", 10), bg="red", fg="white", command=self.remove_selected_reminder).pack(pady=5)
        
        tk.Label(self, text="Add a New Reminder:", font=("Arial", 10), bg="#ffffff").pack(pady=5)
        self.new_reminder_entry = tk.Entry(self, width=40)
        self.new_reminder_entry.pack(pady=5)
        tk.Button(self, text="Add Reminder", font=("Arial", 10), bg="green", fg="white", command=self.add_reminder).pack(pady=5)
        
        tk.Button(self, text="Back", font=("Arial", 12), command=lambda: controller.switch_frame(HomePage)).pack(pady=10)
    
    def load_reminders(self):
        try:
            with open(DATA_FILE, "r") as f:
                data = json.load(f)
                self.reminders = data.get("reminders", [])
        except FileNotFoundError:
            self.reminders = []
        self.refresh_reminder_list()
    
    def save_reminders(self):
        with open(DATA_FILE, "w") as f:
            json.dump({"reminders": self.reminders}, f, indent=4)
    
    def refresh_reminder_list(self):
        self.reminder_listbox.delete(0, tk.END)
        for reminder in self.reminders:
            self.reminder_listbox.insert(tk.END, reminder)
    
    def remove_selected_reminder(self):
        selected_index = self.reminder_listbox.curselection()
        if selected_index:
            del self.reminders[selected_index[0]]
            self.save_reminders()
            self.refresh_reminder_list()
    
    def add_reminder(self):
        new_reminder = self.new_reminder_entry.get()
        if new_reminder:
            self.reminders.append(new_reminder)
            self.save_reminders()
            self.refresh_reminder_list()
            self.new_reminder_entry.delete(0, tk.END)
