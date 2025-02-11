import tkinter as tk

class HomePage(tk.Frame):
    def __init__(self, root, controller):
        super().__init__(root)
        self.controller = controller
        self.configure(bg="#87CEFA")  # Light blue background

        tk.Label(self, text="Welcome Back,\nUserName", font=("Arial", 20, "bold"), bg="#87CEFA", fg="white").place(x=400, y=30)
        
        reminders_frame = tk.Frame(self, bg="#FFFF9F", padx=10, pady=10)  # Light yellow
        reminders_frame.place(x=400, y=100, width=260, height=200)
        
        tk.Label(reminders_frame, text="Your Next Reminders:", font=("Arial", 12, "bold"), bg="#FFFF9F", fg="black").pack(anchor="w")
        self.reminders_label = tk.Label(reminders_frame, text="TODAY:\n4P.M - Turn off A/C\n10:15P.M - Increase heating to 75°F\n\nTOMORROW:\n11A.M - Replace and test new light-sensitive lights\n\nMARCH 9:\n12A.M - Push clocks an hour forwards", font=("Arial", 8), justify="left", bg="#FFFF9F", fg="black")
        self.reminders_label.pack(anchor="w")     

        tk.Button(reminders_frame, text="Update Reminders", font=("Arial", 10, "bold"), bg="white", fg="black", command=self.show_update_reminders).pack(pady=5)

        button_frame = tk.Frame(self, bg="#87CEFA")
        button_frame.place(x=50, y=100)
        
        tk.Button(button_frame, text="View Your Energy Consumption", font=("Arial", 12, "bold"), bg="#FFFF9F", fg="black", width=30, height=3, command=self.show_graph_page).pack(pady=10)
        tk.Button(button_frame, text="View Neighbourhood Consumption", font=("Arial", 12, "bold"), bg="#FFFF9F", fg="black", width=30, height=3, command=self.show_comparison_page).pack(pady=10)
        
        tk.Button(self, text="Settings", font=("Arial", 12, "bold"), bg="#87CEFA", fg="gray", borderwidth=0, command=self.show_settings_page).place(x=100, y=50)

    def show_graph_page(self):
        self.controller.switch_frame(PlaceholderPage)

    def show_comparison_page(self):
        self.controller.switch_frame(PlaceholderPage)

    def show_settings_page(self):
        self.controller.switch_frame(PlaceholderPage)

    def show_update_reminders(self):
        """Switch to the update reminders page."""
        self.controller.switch_frame(UpdateRemindersPage)


class UpdateRemindersPage(tk.Frame):
    """Page for updating reminders."""
    def __init__(self, root, controller):
        super().__init__(root)
        self.controller = controller
        self.configure(bg="#ffffff")

        self.reminders = [
            "4P.M - Turn off A/C",
            "10:15P.M - Increase heating to 75°F",
            "11A.M - Replace and test new light-sensitive lights",
            "12A.M - Push clocks an hour forwards"
        ]

        tk.Label(self, text="Update Your Reminders", font=("Arial", 14, "bold"), bg="#ffffff").pack(pady=10)

        self.reminder_listbox = tk.Listbox(self, width=50, height=10)
        self.reminder_listbox.pack(pady=10)
        self.refresh_reminder_list()

        tk.Button(self, text="Remove Selected Reminder", font=("Arial", 10, "bold"), bg="red", fg="white", command=self.remove_selected_reminder).pack(pady=5)

        tk.Label(self, text="Add a New Reminder:", font=("Arial", 10, "bold"), bg="#ffffff").pack(pady=5)
        self.new_reminder_entry = tk.Entry(self, width=40)
        self.new_reminder_entry.pack(pady=5)
        tk.Button(self, text="Add Reminder", font=("Arial", 10, "bold"), bg="green", fg="white", command=self.add_reminder).pack(pady=5)

        tk.Button(self, text="Back to Home", font=("Arial", 12, "bold"), command=self.go_back).pack(pady=10)

    def refresh_reminder_list(self):
        self.reminder_listbox.delete(0, tk.END)
        for reminder in self.reminders:
            self.reminder_listbox.insert(tk.END, reminder)

    def remove_selected_reminder(self):
        selected_index = self.reminder_listbox.curselection()
        if selected_index:
            del self.reminders[selected_index[0]]
            self.refresh_reminder_list()

    def add_reminder(self):
        new_reminder = self.new_reminder_entry.get()
        if new_reminder:
            self.reminders.append(new_reminder)
            self.refresh_reminder_list()
            self.new_reminder_entry.delete(0, tk.END)

    def go_back(self):
        self.controller.switch_frame(HomePage)

