import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class NeighborhoodPage(tk.Frame):
    def __init__(self, root, controller):
        super().__init__(root)
        self.controller = controller
        self.configure(bg="#87CEFA")



        tk.Label(self, text="🏡 Neighborhood Energy Comparison", font=("Arial", 16, "bold"), bg="#87CEFA", fg="#333333").pack(pady=10)



        main_frame = tk.Frame(self, bg="#87CEFA")
        main_frame.pack(fill="both", expand=True, padx=20, pady=10)



        left_frame = tk.Frame(main_frame, bg="#87CEFA")
        left_frame.pack(side="left", padx=20)



        tk.Label(left_frame, text="⚡ Your Energy Breakdown", font=("Arial", 12, "bold"), bg="#87CEFA", fg="#333333").pack(pady=5)
        self.plot_pie_chart(left_frame, user=True)



        tk.Label(left_frame, text="🏘️ Neighborhood Avg Breakdown", font=("Arial", 12, "bold"), bg="#87CEFA", fg="#333333").pack(pady=10)
        self.plot_pie_chart(left_frame, user=False)



        right_frame = tk.Frame(main_frame, bg="#87CEFA")
        right_frame.pack(side="right", padx=20)


        self.user_consumption = 450 
        self.neighborhood_avg = 380 



        tk.Label(right_frame, text=f"⚡ Your Monthly Usage: {self.user_consumption} kWh", font=("Arial", 12), bg="#87CEFA", fg="#333333").pack(pady=5)
        tk.Label(right_frame, text=f"🏘️ Neighborhood Avg Usage: {self.neighborhood_avg} kWh", font=("Arial", 12), bg="#87CEFA", fg="#333333").pack(pady=5)



        self.plot_comparison_chart(right_frame)



        if self.user_consumption > self.neighborhood_avg:
            tk.Label(right_frame, text="🔴 Your consumption is higher than average! Try reducing energy waste.", font=("Arial", 12), bg="#87CEFA", fg="red").pack(pady=5)
        else:
            tk.Label(right_frame, text="🟢 Great! Your energy usage is below the neighborhood average.", font=("Arial", 12), bg="#87CEFA", fg="green").pack(pady=5)



        tk.Button(self, text="⬅️ Back to Home", font=("Arial", 12), bg="#FFFACD", fg="#333333", width=30, height=1, borderwidth=2, relief="raised", command=self.go_back).pack(pady=10)


    def go_back(self):
        from home_page import HomePage 
        self.controller.switch_frame(HomePage)


    def plot_pie_chart(self, parent, user=True):
        # Creates a pie chart for energy consumption breakdown
        fig, ax = plt.subplots(figsize=(3, 3))


        if user:
            labels = ["Heating", "Cooling", "Lighting", "Refrigerator", "Electronics"]
            data = [30, 25, 15, 20, 10]  
            title = "Your Consumption"
        else:
            labels = ["Heating", "Cooling", "Lighting", "Refrigerator", "Electronics"]
            data = [25, 20, 20, 15, 20] 
            title = "Neighborhood Avg"


        colors = ["#FFA07A", "#20B2AA", "#FFD700", "#9370DB", "#4682B4"]
        wedges, texts, autotexts = ax.pie(data, labels=labels, autopct='%1.0f%%', startangle=90, colors=colors, textprops={'fontsize': 8})


        ax.set_title(title, fontsize=10, fontweight="bold", color="#333333")


        for text in texts:
            text.set_color("#333333")
            text.set_fontsize(8)  
        for autotext in autotexts:
            autotext.set_color("white")
            autotext.set_fontsize(7) 


        canvas = FigureCanvasTkAgg(fig, master=parent)
        canvas.get_tk_widget().pack(pady=5)
        canvas.draw()


    def plot_comparison_chart(self, parent):
        # Creates a bar chart comparing user and neighborhood energy consumption
        fig, ax = plt.subplots(figsize=(4, 3)) 


        categories = ["You", "Neighborhood Avg"]
        values = [self.user_consumption, self.neighborhood_avg]


        ax.bar(categories, values, color=["#FFA07A", "#4682B4"])


        ax.set_title("Your Usage vs Neighborhood", fontsize=12, fontweight="bold", color="#333333")
        ax.set_ylabel("kWh", fontsize=10, color="#333333")
        ax.set_yticks(range(0, max(values) + 50, 50))


        canvas = FigureCanvasTkAgg(fig, master=parent)
        canvas.get_tk_widget().pack(pady=10)
        canvas.draw()





