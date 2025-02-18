import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class GraphPage(tk.Frame):
    def __init__(self, root, controller):
        super().__init__(root)
        self.controller = controller
        self.configure(bg="#ffffff")
        
        tk.Label(self, text="Energy Consumption by Appliance", font=("Arial", 14, "bold"), bg="#ffffff").pack()
        self.plot_pie_chart()
        
        tk.Button(self, text="Back", command=self.go_back).pack()

    def go_back(self):
        from home_page import HomePage  # Import here to avoid circular import
        self.controller.switch_frame(HomePage)

    def plot_pie_chart(self):
        fig, ax = plt.subplots()
        appliances = ["Heating", "Cooling", "Lighting", "Refrigerator", "Electronics"]
        consumption = [30, 25, 15, 20, 10]  # Example percentage distribution
        
        ax.pie(consumption, labels=appliances, autopct='%1.1f%%', startangle=90, colors=["red", "blue", "green", "orange", "purple"])
        ax.set_title("Energy Consumption by Appliance")
        
        canvas = FigureCanvasTkAgg(fig, master=self)
        canvas.get_tk_widget().pack()
        canvas.draw()