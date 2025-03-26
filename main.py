import tkinter as tk
from home_page import HomePage
from energyGraph import GraphPage
from reminders import RemindersPage
from neighborhood import NeighborhoodPage
from settings import SettingsPage 


class EnergyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Energy Efficient Home Budgeting")
        self.root.geometry("800x600")
        self.root.configure(bg="#87CEFA")


        self.current_frame = None
        self.show_home_page()


    def switch_frame(self, frame_class):
        #Destroy current frame and load a new one
        if self.current_frame:
            self.current_frame.destroy()
        self.current_frame = frame_class(self.root, self)
        self.current_frame.pack(fill="both", expand=True)


    def show_home_page(self):
        self.switch_frame(HomePage)


if __name__ == "__main__":
    root = tk.Tk()
    app = EnergyApp(root)
    root.mainloop()





