import tkinter as tk
import json
from tkinter import messagebox


DATA_FILE = "data.json"
STATE_FILE = "app_state.json" 


class SettingsPage(tk.Frame):
    def __init__(self, root, controller):
        super().__init__(root)
        self.controller = controller
        self.configure(bg="#87CEFA")


        tk.Label(self, text="⚙️ Settings", font=("Arial", 16, "bold"), bg="#87CEFA", fg="#333333").pack(pady=10)



        tk.Button(self, text="🗑️ Delete All Data", font=("Arial", 12), bg="white", fg="black", width=30, height=1,
                  borderwidth=2, relief="raised", command=self.confirm_delete).pack(pady=20)



        tk.Button(self, text="⬅️ Back to Home", font=("Arial", 12), bg="#FFFACD", fg="#333333", width=30, height=1,
                  borderwidth=2, relief="raised", command=lambda: self.controller.switch_frame(__import__("home_page").HomePage)).pack(pady=10)


    def confirm_delete(self):
        # Asks user for confirmation before deleting all data.
        response = messagebox.askyesno("Confirm Delete", "Are you sure you want to delete all data? This cannot be undone.")
        if response:
            self.delete_all_data()


    def delete_all_data(self):
        # Deletes all reminders and sets `energy_reset = True`
        try:
            with open(DATA_FILE, "w") as f:
                json.dump({"reminders": []}, f, indent=4)



            self.save_energy_reset_state(True)


            messagebox.showinfo("Success", "All data has been cleared! Please update energy data.")
            self.controller.switch_frame(__import__("home_page").HomePage)
        except Exception as e:
            messagebox.showerror("Error", f"Could not clear data: {e}")


    def save_energy_reset_state(self, state):
        # Saves energy reset state to a file (persists across restarts).
        try:
            with open(STATE_FILE, "w") as f:
                json.dump({"energy_reset": state}, f, indent=4)
        except Exception as e:
            messagebox.showerror("Error", f"Could not save state: {e}")





