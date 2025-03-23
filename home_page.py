import tkinter as tk
import json
from datetime import datetime
from tkinter import messagebox
from energyGraph import GraphPage
from reminders import RemindersPage
from neighborhood import NeighborhoodPage
from settings import SettingsPage


DATA_FILE = "data.json"
STATE_FILE = "app_state.json" 


class HomePage(tk.Frame):
    def __init__(self, root, controller):
        super().__init__(root)
        self.controller = controller
        self.configure(bg="#87CEFA")



        self.energy_reset = self.load_energy_reset_state()



        main_frame = tk.Frame(self, bg="#87CEFA")
        main_frame.pack(fill="both", expand=True, padx=20, pady=20)



        left_frame = tk.Frame(main_frame, bg="#87CEFA")
        left_frame.pack(side="left", fill="y", padx=20)


        tk.Label(left_frame, text="🏠 Welcome Back, User!", font=("Arial", 20, "bold"), bg="#87CEFA", fg="#333333").pack(pady=10)


        btn_style = {"font": ("Arial", 14), "width": 30, "height": 2, "borderwidth": 2, "relief": "raised"}



        self.btn_graph = tk.Button(left_frame, text="📊 View Your Energy Consumption",
                                   command=lambda: self.controller.switch_frame(GraphPage),
                                   **btn_style, bg=("#FFFACD" if not self.energy_reset else "#D3D3D3"),
                                   state=("normal" if not self.energy_reset else "disabled"))
        self.btn_graph.pack(pady=10)


        self.btn_neighborhood = tk.Button(left_frame, text="🏡 Compare with Neighborhood",
                                          command=lambda: self.controller.switch_frame(NeighborhoodPage),
                                          **btn_style, bg=("#FFFACD" if not self.energy_reset else "#D3D3D3"),
                                          state=("normal" if not self.energy_reset else "disabled"))
        self.btn_neighborhood.pack(pady=10)


        self.btn_reminders = tk.Button(left_frame, text="⏰ Update Reminders",
                                       command=lambda: self.controller.switch_frame(RemindersPage),
                                       **btn_style, bg=("#FFFACD" if not self.energy_reset else "#D3D3D3"),
                                       state=("normal" if not self.energy_reset else "disabled"))
        self.btn_reminders.pack(pady=10)


        self.btn_settings = tk.Button(left_frame, text="⚙️ Settings",
                                      command=lambda: self.controller.switch_frame(SettingsPage),
                                      **btn_style, bg=("#FFFACD" if not self.energy_reset else "#D3D3D3"),
                                      state=("normal" if not self.energy_reset else "disabled"))
        self.btn_settings.pack(pady=10)



        tk.Button(left_frame, text="🔄 Update Energy", font=("Arial", 14), bg="red", fg="white", width=30, height=2,
                  borderwidth=2, relief="raised", command=self.update_energy).pack(pady=10)



        right_frame = tk.Frame(main_frame, bg="#87CEFA")
        right_frame.pack(side="right", fill="both", expand=True, padx=20)



        tk.Label(right_frame, text="⏳ Upcoming Reminders:", font=("Arial", 16, "bold"), bg="#87CEFA", fg="#333333").pack(pady=5)
        self.reminders_frame = tk.Frame(right_frame, bg="#87CEFA")
        self.reminders_frame.pack(pady=5)
        self.load_upcoming_reminders()


    def update_energy(self):
        """Unlocks the app by setting energy_reset to False and refreshing buttons."""
        self.energy_reset = False
        self.save_energy_reset_state(False)  



        self.btn_graph.config(state="normal", bg="#FFFACD")
        self.btn_neighborhood.config(state="normal", bg="#FFFACD")
        self.btn_reminders.config(state="normal", bg="#FFFACD")
        self.btn_settings.config(state="normal", bg="#FFFACD")


        messagebox.showinfo("Success", "Energy data updated. You can now access the app.")
    def load_energy_reset_state(self):
        """Loads the energy reset state from a file (persists across sessions)."""
        try:
            with open(STATE_FILE, "r") as f:
                data = json.load(f)
                return data.get("energy_reset", False)  
        except (FileNotFoundError, json.JSONDecodeError):
            return False  
    def save_energy_reset_state(self, state):
        """Saves the energy reset state to a file (persists across sessions)."""
        try:
            with open(STATE_FILE, "w") as f:
                json.dump({"energy_reset": state}, f, indent=4)
        except Exception as e:
            messagebox.showerror("Error", f"Could not save state: {e}")
    def load_upcoming_reminders(self):
        """Load and display the next 3 upcoming reminders"""
        try:
            with open(DATA_FILE, "r") as f:
                data = json.load(f)
                reminders = data.get("reminders", [])
        except FileNotFoundError:
            reminders = []
        upcoming_reminders = []
        now = datetime.now()
        for reminder in reminders:
            try:
                date_time_str, text = reminder.split(" - ", 1)
                reminder_datetime = datetime.strptime(date_time_str, "%Y-%m-%d %H:%M")
                if reminder_datetime > now:
                    upcoming_reminders.append((reminder_datetime, text))
            except ValueError:
                continue
        upcoming_reminders.sort(key=lambda x: x[0])
        upcoming_reminders = upcoming_reminders[:3]
        for widget in self.reminders_frame.winfo_children():
            widget.destroy()
        if upcoming_reminders:
            for reminder in upcoming_reminders:
                tk.Label(self.reminders_frame, text=f"📅 {reminder[0].strftime('%Y-%m-%d %H:%M')} - {reminder[1]}", font=("Arial", 12), bg="#FFFACD", fg="#333333", width=50, height=1).pack(pady=2)
