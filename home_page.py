import tkinter as tk
from energyGraph import GraphPage
from reminders import RemindersPage

class HomePage(tk.Frame):
    def __init__(self, root, controller):
        super().__init__(root)
        self.controller = controller
        self.configure(bg="#87CEFA")

        tk.Label(self, text="Welcome Back, User", font=("Arial", 20, "bold"), bg="#87CEFA").pack(pady=20)
        tk.Button(self, text="View Your Energy Consumption", font=("Arial", 12), command=self.show_graph_page).pack(pady=5)
        tk.Button(self, text="Compare with Neighborhood", font=("Arial", 12), command=self.show_comparison_page).pack(pady=5)
        tk.Button(self, text="Update Reminders", font=("Arial", 12), command=self.show_update_reminders).pack(pady=5)
        tk.Button(self, text="Settings", font=("Arial", 12), command=self.show_settings_page).pack(pady=5)

    def show_graph_page(self):
        self.controller.switch_frame(GraphPage)
    
    def show_comparison_page(self):
        pass  # Placeholder for comparison page navigation
    
    def show_update_reminders(self):
        self.controller.switch_frame(RemindersPage)
    
    def show_settings_page(self):
        pass  # Placeholder for settings navigation
