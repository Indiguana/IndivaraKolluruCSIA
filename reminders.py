import tkinter as tk
import json
from datetime import datetime
from tkinter import messagebox


DATA_FILE = "data.json"


class RemindersPage(tk.Frame):
    def __init__(self, root, controller):
        super().__init__(root)
        self.controller = controller
        self.configure(bg="#87CEFA")


        # Title Label
        tk.Label(self, text="⏰ Manage Your Reminders", font=("Arial", 20, "bold"), bg="#87CEFA", fg="#333333").pack(pady=10)


        # Reminder Listbox
        self.reminder_listbox = tk.Listbox(self, width=50, height=10, font=("Arial", 12), bg="#FFFACD", fg="#333333", borderwidth=2, relief="sunken")
        self.reminder_listbox.pack(pady=10)


        self.load_reminders()


        # Buttons with Styling
        btn_style = {"font": ("Arial", 12), "bg": "#FFFACD", "fg": "#333333", "width": 30, "height": 1, "borderwidth": 2, "relief": "raised"}
        tk.Button(self, text="➕ Add Reminder", command=self.add_reminder, **btn_style).pack(pady=5)
        tk.Button(self, text="❌ Remove Selected Reminder", bg="white", fg="black", font=("Arial", 12), width=30, height=1, command=self.remove_selected_reminder).pack(pady=5)


        # Reminder Input Fields
        tk.Label(self, text="Reminder Text:", font=("Arial", 12), bg="#87CEFA", fg="#333333").pack(pady=5)
        self.new_reminder_entry = tk.Entry(self, width=40, font=("Arial", 12))
        self.new_reminder_entry.pack(pady=5)


        # Date Input
        tk.Label(self, text="Enter Date (YYYY-MM-DD):", font=("Arial", 12), bg="#87CEFA", fg="#333333").pack(pady=5)
        self.date_entry = tk.Entry(self, width=20, font=("Arial", 12))
        self.date_entry.pack(pady=5)


        # Time Input
        tk.Label(self, text="Enter Time (HH:MM) - 24 Hour Format:", font=("Arial", 12), bg="#87CEFA", fg="#333333").pack(pady=5)
        self.time_entry = tk.Entry(self, width=20, font=("Arial", 12))
        self.time_entry.pack(pady=5)


        # Back Button
        tk.Button(self, text="⬅️ Back to Home", font=("Arial", 12), bg="#FFFACD", fg="#333333", width=30, height=1, borderwidth=2, relief="raised", command=self.go_back).pack(pady=10)


    def go_back(self):
        from home_page import HomePage  # Lazy import to fix circular import issue
        self.controller.switch_frame(HomePage)


    def load_reminders(self):
        """ Load reminders and sort them by upcoming time """
        try:
            with open(DATA_FILE, "r") as f:
                data = json.load(f)
                self.reminders = data.get("reminders", [])
        except FileNotFoundError:
            self.reminders = []


        self.sort_reminders()  # Sort as soon as reminders are loaded
        self.refresh_reminder_list()


    def save_reminders(self):
        """ Save sorted reminders to file """
        self.sort_reminders()  # Ensure reminders are sorted before saving
        with open(DATA_FILE, "w") as f:
            json.dump({"reminders": self.reminders}, f, indent=4)


    def refresh_reminder_list(self):
        """ Refresh UI listbox to display sorted reminders """
        self.reminder_listbox.delete(0, tk.END)
        for reminder in self.reminders:
            self.reminder_listbox.insert(tk.END, reminder)


    def remove_selected_reminder(self):
        """ Remove the selected reminder """
        selected_index = self.reminder_listbox.curselection()
        if selected_index:
            del self.reminders[selected_index[0]]
            self.save_reminders()
            self.refresh_reminder_list()


    def add_reminder(self):
        """ Add a new reminder and sort list """
        new_reminder = self.new_reminder_entry.get()
        reminder_date = self.date_entry.get()
        reminder_time = self.time_entry.get()


        # Validate Date & Time
        if not self.validate_datetime(reminder_date, reminder_time):
            messagebox.showerror("Invalid Input", "Please enter a valid future date and time (YYYY-MM-DD & HH:MM in 24-hour format).")
            return


        # Convert date & time into a datetime object
        reminder_datetime = f"{reminder_date} {reminder_time}"
        self.reminders.append(f"{reminder_datetime} - {new_reminder}")
        self.save_reminders()  # Sort and save


        self.refresh_reminder_list()  # Update UI


        # Clear fields after adding
        self.new_reminder_entry.delete(0, tk.END)
        self.date_entry.delete(0, tk.END)
        self.time_entry.delete(0, tk.END)


    def validate_datetime(self, date_str, time_str):
        """ Validates that the date is in YYYY-MM-DD format and time is in HH:MM (24-hour format), and it must be in the future """
        try:
            reminder_datetime = datetime.strptime(f"{date_str} {time_str}", "%Y-%m-%d %H:%M")
            now = datetime.now()
            if reminder_datetime <= now:
                messagebox.showerror("Invalid Date/Time", "The reminder time must be in the future.")
                return False
            return True
        except ValueError:
            return False


    def sort_reminders(self):
        """ Sort reminders by upcoming date and time """
        def extract_datetime(reminder):
            try:
                date_time_str = reminder.split(" - ")[0]  # Extract date & time part
                return datetime.strptime(date_time_str, "%Y-%m-%d %H:%M")
            except ValueError:
                return datetime.max  # If parsing fails, push to the end


        self.reminders.sort(key=extract_datetime)  # Sort based on soonest reminder first





