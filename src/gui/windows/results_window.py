import customtkinter as ctk
import tkinter as tk
from src.core.analyzer import *

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
        
        self.frame1 = ctk.CTkScrollableFrame(
            self, fg_color="#72577c", bg_color="#a9c2c9", width=300
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
        frame1_title2.grid(row=9, column=0)
        
        self.frame2 = ctk.CTkScrollableFrame(
            self, fg_color="#72577c", bg_color="#a9c2c9"
        )
        self.frame2.place(relx=0.6, rely=0.3, anchor=tk.CENTER)
        
        section2 = ctk.CTkLabel(
            self, text="Recomendations:", 
            font=("Arial", 14, "bold"), text_color="#72577c", wraplength=500, 
            bg_color="#a9c2c9")
        section2.place(relx=0.1, rely=0.5, anchor=tk.CENTER)
        
        self.frame3 = ctk.CTkScrollableFrame(
            self, fg_color="#72577c", bg_color="#a9c2c9"
        )
        self.frame3.place(relx=0.3, rely=0.7, anchor=tk.CENTER)
        
        self.analyze_data()
        
    def analyze_data(self):
        total_days = []
        total_weekly = 0
        weakest_day = 0
        min_hours = float("inf")
        
        for i, value in enumerate(self.data_manager.weekly_log):
            total_of_day = total_day(value)
            total_days.append(total_of_day)
            total_weekly += total_of_day
            
            if  total_of_day < min_hours:
                min_hours = total_of_day
                weakest_day = i+1
                
        for i, value in enumerate(total_days):
            hours_days = ctk.CTkLabel(
                self.frame1, text=f"{value:.2f} hours", bg_color="#72577c", fg_color="#72577c", 
                text_color="#c5f7f0", font=("Arial", 14)
            )
            hours_days.grid(row=i+2, column=1)
            
        weekly_hours = ctk.CTkLabel(
            self.frame1, text=f"{total_weekly:.2f} hours", bg_color="#72577c", fg_color="#72577c", 
            text_color="#c5f7f0", font=("Arial", 14)
        )
        weekly_hours.grid(row=9, column=1)