import tkinter as tk
from home_page import HomePage

class EnergyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Energy Efficient Home Budgeting")
        self.root.geometry("700x500")
        self.root.configure(bg="#87CEFA")  # Light blue background
        
        self.current_frame = None
        self.show_home_page()
    
    def show_home_page(self):
        """Displays the Home Page."""
        self.switch_frame(HomePage)

    def switch_frame(self, frame_class):
        """Destroys the current frame and replaces it with a new one."""
        if self.current_frame:
            self.current_frame.destroy()
        
        self.current_frame = frame_class(self.root, self)
        self.current_frame.pack(fill="both", expand=True)

if __name__ == "__main__":
    root = tk.Tk()
    app = EnergyApp(root)
    root.mainloop()
