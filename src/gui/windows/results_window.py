import customtkinter as ctk
import tkinter as tk
from src.core.analyzer import *
from src.core.visualizer import create_graphics

class ResultsWindow(ctk.CTkToplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.data_manager = self.parent.data_manager
        self.title("Results Panel")
        self.geometry("900x600")
        self.config(bg="#a9c2c9")
        self.resizable(False, False)
        self.transient(parent)
        self.lift()
        self.create_widgets()
        
    def create_widgets(self):
        title = ctk.CTkLabel( # Label for the title
            self, text="Academic Recommendation Report", 
            bg_color="#a9c2c9", fg_color="#c5f7f0", text_color="#562155",
            corner_radius=60, font=("Arial", 20, "bold"))
        title.place(relx=0.5, rely=0.05, anchor=tk.CENTER)
        
        section1 = ctk.CTkLabel(
            self, text="Weekly Metrics:", 
            font=("Arial", 14, "bold"), text_color="#72577c", wraplength=500, 
            bg_color="#a9c2c9")
        section1.place(relx=0.1, rely=0.1, anchor=tk.CENTER)
        
        # First frame
        self.frame1 = ctk.CTkScrollableFrame(
            self, fg_color="#72577c", bg_color="#a9c2c9", width=250
        )
        self.frame1.place(relx=0.2, rely=0.3, anchor=tk.CENTER)
        
        frame1_title1 = ctk.CTkLabel(
            self.frame1, text="Hours per day:", bg_color="#72577c", fg_color="#562155", 
            text_color="#c5f7f0", corner_radius=60, font=("Arial", 14, "bold")
        )
        frame1_title1.grid(row=0, column=0)
        
        for i in range(7):
            days = ctk.CTkLabel(
                self.frame1, text=f"Day {i+1}:", bg_color="#72577c", fg_color="#72577c", 
                text_color="#c5f7f0", font=("Arial", 14, "bold")
            )
            days.grid(row=i+2, column=0)
            
        frame1_title2 = ctk.CTkLabel(
            self.frame1, text="Weekly total:", bg_color="#72577c", fg_color="#562155", 
            text_color="#c5f7f0", corner_radius=60, font=("Arial", 14, "bold")
        )
        frame1_title2.grid(row=9, column=0, pady=5)
        
        # Second frame
        self.frame2 = ctk.CTkScrollableFrame(
            self, fg_color="#72577c", bg_color="#a9c2c9", width=500
        )
        self.frame2.place(relx=0.66, rely=0.3, anchor=tk.CENTER)
        
        frame2_title1 = ctk.CTkLabel(
            self.frame2, text="Hours per activity:", bg_color="#72577c", fg_color="#562155", 
            text_color="#c5f7f0", corner_radius=60, font=("Arial", 14, "bold")
        )
        frame2_title1.grid(row=0, column=0)
        
        for i, value in enumerate(self.data_manager.activities):
            activities = ctk.CTkLabel(
                self.frame2, text=value, bg_color="#72577c", fg_color="#72577c", 
                text_color="#c5f7f0", font=("Arial", 14, "bold")
            )
            activities.grid(row=i+2, column=0)
            
        frame2_title2 = ctk.CTkLabel(
            self.frame2, text="Practice ratio (P):", bg_color="#72577c", fg_color="#562155", 
            text_color="#c5f7f0", corner_radius=60, font=("Arial", 14, "bold")
        )
        frame2_title2.grid(row=len(self.data_manager.activities)+2, column=0, pady=5)
        
        frame2_title3 = ctk.CTkLabel(
            self.frame2, text="Day with the least study:", bg_color="#72577c", fg_color="#562155", 
            text_color="#c5f7f0", corner_radius=60, font=("Arial", 14, "bold")
        )
        frame2_title3.grid(row=len(self.data_manager.activities)+3, column=0, pady=5)
        
        frame2_title4 = ctk.CTkLabel(
            self.frame2, text="Dominant activity:", bg_color="#72577c", fg_color="#562155", 
            text_color="#c5f7f0", corner_radius=60, font=("Arial", 14, "bold")
        )
        frame2_title4.grid(row=len(self.data_manager.activities)+4, column=0,pady=5)
        
        # Section 2 -------------------------------------
        section2 = ctk.CTkLabel(
            self, text="Recomendations:", 
            font=("Arial", 14, "bold"), text_color="#72577c", wraplength=500, 
            bg_color="#a9c2c9")
        section2.place(relx=0.1, rely=0.52, anchor=tk.CENTER)
        
        self.frame3 = ctk.CTkScrollableFrame(
            self, fg_color="#72577c", bg_color="#a9c2c9", width=750
        )
        self.frame3.place(relx=0.5, rely=0.72, anchor=tk.CENTER)
        
        frame3_title1 = ctk.CTkLabel(
            self.frame3, text="Suggested route:", bg_color="#72577c", fg_color="#562155", 
            text_color="#c5f7f0", corner_radius=60, font=("Arial", 14, "bold")
        )
        frame3_title1.grid(row=0, column=0, pady=5)
        
        frame3_title2 = ctk.CTkLabel(
            self.frame3, text="Weekly status:", bg_color="#72577c", fg_color="#562155", 
            text_color="#c5f7f0", corner_radius=60, font=("Arial", 14, "bold")
        )
        frame3_title2.grid(row=1, column=0, pady=5)
        
        frame3_title3 = ctk.CTkLabel(
            self.frame3, text="Specific action:", bg_color="#72577c", fg_color="#562155", 
            text_color="#c5f7f0", corner_radius=60, font=("Arial", 14, "bold")
        )
        frame3_title3.grid(row=2, column=0, pady=5)
        
        btn_return = ctk.CTkButton(
            self, text="Return to Menu", bg_color="#a9c2c9", fg_color="transparent",
            hover_color="#8e8ca3", font=("Arial", 14, "bold"), text_color="#562155",
            command=self.destroy, border_color="#8e8ca3", border_width=2)
        btn_return.place(relx=0.1, rely=0.95, anchor=tk.CENTER)
        
        btn_charts = ctk.CTkButton(
            self, text="Generate Charts", bg_color="#a9c2c9", fg_color="transparent",
            hover_color="#8e8ca3", font=("Arial", 14, "bold"), text_color="#562155",
            border_color="#8e8ca3", border_width=2, command=self.create_graphics)
        btn_charts.place(relx=0.7, rely=0.95, anchor=tk.CENTER)
        
        btn_report = ctk.CTkButton(
            self, text="Generate Report", bg_color="#a9c2c9", fg_color="transparent",
            hover_color="#8e8ca3", font=("Arial", 14, "bold"), text_color="#562155",
            border_color="#8e8ca3", border_width=2)
        btn_report.place(relx=0.9, rely=0.95, anchor=tk.CENTER)
        
        self.analyze_data()
        
    def analyze_data(self):
        # Data from the first frame
        self.total_days = []
        total_weekly = 0
        weakest_day = 0
        min_hours = float("inf")
        
        for i, value in enumerate(self.data_manager.weekly_log):
            total_of_day = total_day(value)
            self.total_days.append(total_of_day)
            total_weekly += total_of_day
            
            if  total_of_day < min_hours:
                min_hours = total_of_day
                weakest_day = i+1
                
        for i, value in enumerate(self.total_days):
            hours_days = ctk.CTkLabel(
                self.frame1, text=f"{value:.2f} hours", bg_color="#72577c", fg_color="#72577c", 
                text_color="#c5f7f0", font=("Arial", 14)
            )
            hours_days.grid(row=i+2, column=1)
            
        weekly_hours = ctk.CTkLabel(
            self.frame1, text=f"{total_weekly:.2f} hours", bg_color="#72577c", fg_color="#72577c", 
            text_color="#c5f7f0", font=("Arial", 14, "bold")
        )
        weekly_hours.grid(row=9, column=1, pady=5)
        
        # Data from the second frame
        self.totals_act = totals_activity(self.data_manager.weekly_log)
        
        for i, value in enumerate(self.totals_act):
            hours_activities = ctk.CTkLabel(
                self.frame2, text=f"{value:.2f} hours", bg_color="#72577c", fg_color="#72577c", 
                text_color="#c5f7f0", font=("Arial", 14)
            )
            hours_activities.grid(row=i+2, column=1)
            
        self.P = practical_proportion(self.totals_act)
        
        result_P = ctk.CTkLabel(
            self.frame2, text=f"{self.P:.2%}", bg_color="#72577c", fg_color="#72577c", 
            text_color="#c5f7f0", font=("Arial", 14, "bold")
        )
        result_P.grid(row=len(self.data_manager.activities)+2, column=1, pady=5)
        
        weak_day = ctk.CTkLabel(
            self.frame2, text=f"Day {weakest_day}", bg_color="#72577c", fg_color="#72577c", 
            text_color="#c5f7f0", font=("Arial", 14, "bold")
        )
        weak_day.grid(row=len(self.data_manager.activities)+3, column=1, pady=5)
        
        dominant_activity = data_manager.activities[self.totals_act.index(max(self.totals_act))]
        
        dom_activitiy = ctk.CTkLabel(
            self.frame2, text=dominant_activity , bg_color="#72577c", fg_color="#72577c", 
            text_color="#c5f7f0", font=("Arial", 14, "bold")
        )
        dom_activitiy.grid(row=len(self.data_manager.activities)+4, column=1, pady=5)
        
        # Data from the third frame
        h = data_manager.survey_data["h"]
        d = []
        for i in data_manager.activities:
            d.append(data_manager.survey_data[i][1])
        self.Hmin = data_manager.survey_data["Hmin"]
        self.Pmin = data_manager.survey_data["Pmin"]
            
        route, action, state = recommend_route(h, d, self.P, self.Hmin, self.Pmin)
        
        route_result = ctk.CTkLabel(
            self.frame3, text=route , bg_color="#72577c", fg_color="#72577c", 
            text_color="#c5f7f0", font=("Arial", 14, "bold"), wraplength=620
        )
        route_result.grid(row=0, column=1, pady=5, padx=10)
        
        state_result = ctk.CTkLabel(
            self.frame3, text=state , bg_color="#72577c", fg_color="#72577c", 
            text_color="#c5f7f0", font=("Arial", 14, "bold")
        )
        state_result.grid(row=1, column=1, pady=5, padx=10)
        
        action_result = ctk.CTkLabel(
            self.frame3, text=action , bg_color="#72577c", fg_color="#72577c", 
            text_color="#c5f7f0", font=("Arial", 14, "bold")
        )
        action_result.grid(row=2, column=1, pady=5, padx=10)
        
    def create_graphics(self):
        create_graphics(self.total_days, self.Hmin, self.totals_act, self.P, self.Pmin)