import customtkinter as ctk
import tkinter as tk

class MatrixTable(ctk.CTkFrame):
    """
    Class where the entire table and its logic will be created
    """
    def __init__(self, master, data_manager):
        super().__init__(master)
        self.data_manager = data_manager
        self.configure(fg_color="#72577c")
        self.entries = []
        self.create_widgets()
        
    def create_widgets(self):
        # Loop to create activity titles (editable)
        for i in range(len(self.data_manager.activities)):
            activities = ctk.CTkEntry(
                self, bg_color="#72577c", fg_color="#562155", text_color="#c5f7f0",
                corner_radius=60, font=("Arial", 14, "bold"), width=150, justify="center")
            activities.insert(0, self.data_manager.activities[i])
            activities.grid(row=0, column=i+1)
            
        # Loop to create the titles for the 7 days of the week
        days_names = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
        for i in range(len(days_names)):
            days = ctk.CTkLabel(
                self, text=days_names[i], bg_color="#72577c", fg_color="#562155", text_color="#c5f7f0",
                corner_radius=60, font=("Arial", 14, "bold"))
            days.grid(row=i+1, column=0, pady=5)
            
        # Loop to create all entries with their respective predefined information from the matrix
        day_entries = []
        for i, value1 in enumerate(self.data_manager.weekly_log):
            for j, value2 in enumerate(value1):
                entries = ctk.CTkEntry(self, width=50)
                entries.insert(0, value2)
                day_entries.append(value2)
                entries.grid(row=i+1, column=j+1)
        
        print(day_entries)