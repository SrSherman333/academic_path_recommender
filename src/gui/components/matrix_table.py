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
        self.activities = []
        self.create_widgets()
        
    def create_widgets(self):
        self.redraw_table()
        # Loop to create the titles for the 7 days of the week
        days_names = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
        for i in range(len(days_names)):
            days = ctk.CTkLabel(
                self, text=days_names[i], bg_color="#72577c", fg_color="#562155", text_color="#c5f7f0",
                corner_radius=60, font=("Arial", 14, "bold"))
            days.grid(row=i+1, column=0, pady=5)
            
    def update_data_from_gui(self):
        day_entries_past = []
        activities_past = []
        for i in self.entries:
            temp = []
            for j in i:
                temp.append(j.get())
            day_entries_past.append(temp)
            
        for i in self.activities:
            activities_past.append(i.get())
        
        for i, value1 in enumerate(day_entries_past):
            for j, value2 in enumerate(value1):
                self.data_manager.update_matrix(i, j, value2)
                
        for i, value in enumerate(activities_past):
            self.data_manager.update_activities(i, value)
            
    def redraw_table(self):
        for i, value1 in enumerate(self.entries):
            for j, value2 in enumerate(value1):
                value2.destroy()
        self.entries = []
                
        for i, value in enumerate(self.activities):
            value.destroy()
        self.activities = []
        
        # Loop to create activity titles (editable)
        for i in range(len(self.data_manager.activities)):
            activities = ctk.CTkEntry(
                self, bg_color="#72577c", fg_color="#562155", text_color="#c5f7f0",
                corner_radius=60, font=("Arial", 14, "bold"), width=150, justify="center", 
                placeholder_text="Activity")
            activities.insert(0, self.data_manager.activities[i])
            self.activities.append(activities)
            activities.grid(row=0, column=i+1)
            
        # Loop to create all entries with their respective predefined information from the matrix
        for i, value1 in enumerate(self.data_manager.weekly_log):
            day_entries = []
            for j, value2 in enumerate(value1):
                entries = ctk.CTkEntry(self, width=50)
                entries.insert(0, value2)
                day_entries.append(entries)
                entries.grid(row=i+1, column=j+1)
            self.entries.append(day_entries)
            
    def add_columns(self):
        self.update_data_from_gui()

        for i, value in enumerate(self.data_manager.weekly_log):
            self.data_manager.weekly_log[i].append(0.0)
            
        self.data_manager.activities.append("")

        self.redraw_table()
            
    def save_values(self):
        self.update_data_from_gui()
            
        self.data_manager.save_to_file()
        
    def load_values(self):
        self.data_manager.load_from_file()
        
        self.redraw_table()