import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class GraphPage(tk.Frame):
    def __init__(self, root, controller):
        super().__init__(root)
        self.controller = controller
        self.configure(bg="#87CEFA")  # Set background color to match theme


        # Title Label
        tk.Label(self, text="📊 Energy Consumption by Appliance", font=("Arial", 16, "bold"), bg="#87CEFA", fg="#333333").pack(pady=10)


        # Graph Area
        self.plot_pie_chart()


        # Back Button
        tk.Button(self, text="⬅️ Back to Home", font=("Arial", 12), bg="#FFFACD", fg="#333333", width=30, height=1, borderwidth=2, relief="raised", command=self.go_back).pack(pady=10)


    def go_back(self):
        from home_page import HomePage  # Lazy import to prevent circular import
        self.controller.switch_frame(HomePage)


    def plot_pie_chart(self):
        """Creates a pie chart for energy consumption distribution"""
        fig, ax = plt.subplots(figsize=(5, 5))  # Adjust figure size for better display
        appliances = ["Heating", "Cooling", "Lighting", "Refrigerator", "Electronics"]
        consumption = [30, 25, 15, 20, 10]  # Example percentage distribution


        # Pastel-themed colors
        colors = ["#FFA07A", "#20B2AA", "#FFD700", "#9370DB", "#4682B4"]


        # Create Pie Chart
        wedges, texts, autotexts = ax.pie(consumption, labels=appliances, autopct='%1.1f%%', startangle=90, colors=colors, textprops={'fontsize': 12})


        # Set title
        ax.set_title("Energy Consumption by Appliance", fontsize=14, fontweight="bold", color="#333333")


        # Improve readability
        for text in texts:
            text.set_color("#333333")
        for autotext in autotexts:
            autotext.set_color("white")


        # Embed Matplotlib Figure in Tkinter
        canvas = FigureCanvasTkAgg(fig, master=self)
        canvas.get_tk_widget().pack(pady=10)
        canvas.draw()





