'''
THIS CODE IS NOT USED ANYMORE
import tkinter as tk
from tkinter import ttk

class EnergyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Energy Efficient Home Budgeting")
        self.root.geometry("700x500")
        self.root.configure(bg="#87CEFA")  
        
        self.create_home_page()
    
    def create_home_page(self):
        # Creates the home page with navigation buttons.
        for widget in self.root.winfo_children():  
            widget.destroy()
        
        tk.Label(self.root, text="Welcome Back,\nUserName", font=("Arial", 20, "bold"), bg="#87CEFA", fg="white").place(x=400, y=30)
        
        reminders_frame = tk.Frame(self.root, bg="#FFFF9F", padx=10, pady=10)  # Light yellow
        reminders_frame.place(x=400, y=100, width=260, height=200)
        
        tk.Label(reminders_frame, text="Your Next Reminders:", font=("Arial", 12, "bold"), bg="#FFFF9F", fg = "black").pack(anchor="w")
        tk.Label(reminders_frame, text="TODAY:\n4P.M - Turn off A/C\n10:15P.M - Increase heating to 75°F\n\nTOMORROW:\n11A.M - Replace and test new light-sensitive lights\n\nMARCH 9:\n12A.M - Push clocks an hour forwards", font=("Arial", 8), justify="left", bg="#FFFF9F", fg = "black").pack(anchor="w")
        
        button_frame = tk.Frame(self.root, bg="#87CEFA")
        button_frame.place(x=50, y=100)
        
        tk.Button(button_frame, text="View Your Energy Consumption", font=("Arial", 12, "bold"), bg="#FFFF9F", fg="black", width=30, height=3, command=self.show_graph_page).pack(pady=10)
        tk.Button(button_frame, text="View Neighbourhood Consumption", font=("Arial", 12, "bold"), bg="#FFFF9F", fg="black", width=30, height=3, command=self.show_comparison_page).pack(pady=10)
        
        tk.Button(self.root, text="Settings", font=("Arial", 12, "bold"), bg="#87CEFA", fg="gray", borderwidth=0, command=self.show_settings_page).place(x=100, y=50)
    
    def show_graph_page(self):
        """Placeholder for energy graph page."""
        self.create_placeholder_page("Energy Usage Graph")
    
    def show_comparison_page(self):
        """Placeholder for neighborhood comparison page."""
        self.create_placeholder_page("Neighborhood Comparison")
    
    def show_settings_page(self):
        """Placeholder for settings page."""
        self.create_placeholder_page("Settings")
    
    def create_placeholder_page(self, title):
        """Creates a placeholder page with a back button."""
        for widget in self.root.winfo_children():
            widget.destroy()
        
        frame = tk.Frame(self.root, bg="#ffffff", padx=20, pady=20)
        frame.pack(pady=20, fill="both", expand=True)
        
        tk.Label(frame, text=title, font=("Arial", 14, "bold"), bg="#ffffff").pack(pady=10)
        ttk.Button(frame, text="Back to Home", command=self.create_home_page).pack(pady=10, fill="x")
if __name__ == "__main__":
'''
    root = tk.Tk()
    app = EnergyApp(root)
    root.mainloop()
