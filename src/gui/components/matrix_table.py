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
        self.entries = [] # List that will store all the entries in the matrix
        self.activities = [] # List that will store all activity entries
        self.columns = [] # List that stores all the labels that list the columns
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
            
        lbl_delete = ctk.CTkLabel( # Label to indicate that columns can be deleted by choosing one from the ComboBox
            self, text="Delete Columns (Choose)", bg_color="#72577c", 
            fg_color="#562155", text_color="#c5f7f0",
            corner_radius=60, font=("Arial", 14, "bold"))
        lbl_delete.grid(row=9, column=0, columnspan=2, pady=20)
        
        list_columns = [] # Temporary list for writing column indexes
        for i, value in enumerate(self.data_manager.activities):
            list_columns.append(f"Column {i}")
        
        self.cb_columns = ctk.CTkComboBox(self, values=list_columns, width=250) # ComboBox to select a column that you want to delete
        self.cb_columns.grid(row=9, column=2, columnspan=2, pady=20)
        
        self.btn_delete = ctk.CTkButton( # Button to delete columns
            self, text="Delete", bg_color="#72577c", fg_color="#562155", 
            text_color="#c5f7f0", corner_radius=60,font=("Arial", 14, "bold"),
            hover_color="#8e8ca3")
        self.btn_delete.grid(row=9, column=4, pady=20)
            
    def update_data_from_gui(self):
        """
        Method that saves the most up-to-date data of the matrix in data_manager.py
        """
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
        """
        Method that deletes (if it exists) and creates all entries in the array
        """
        for i, value1 in enumerate(self.entries):
            for j, value2 in enumerate(value1):
                value2.destroy()
        self.entries = []
                
        for i, value in enumerate(self.activities):
            value.destroy()
        self.activities = []
        
        for i, value in enumerate(self.columns):
            value.destroy()
        self.columns = []
        
        # Loop to create activity titles (editable)
        for i in range(len(self.data_manager.activities)):
            activities = ctk.CTkEntry(
                self, bg_color="#72577c", fg_color="#562155", text_color="#c5f7f0",
                corner_radius=60, font=("Arial", 14, "bold"), width=150, justify="center", 
                placeholder_text="Activity")
            activities.insert(0, self.data_manager.activities[i])
            self.activities.append(activities)
            activities.grid(row=0, column=i+1)
            
            column = ctk.CTkLabel(
                self, text=f"Column {i}", bg_color="#72577c", fg_color="#562155", 
                text_color="#c5f7f0", corner_radius=60, font=("Arial", 14, "bold"))
            column.grid(row=8, column=i+1)
            self.columns.append(column) 
            
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
        """
        This method saves the data by calling one of the previously mentioned functions, 
        then adds default values ​​(0.0, Activity) to the data_manager, updates the ComboBox values,
        and finally calls the function that deletes and recreates the table based on the 
        data_manager array values
        """
        self.update_data_from_gui()
        
        for i, value in enumerate(self.data_manager.weekly_log):
            self.data_manager.weekly_log[i].append(0.0)
            
        self.data_manager.activities.append("Activity")
        
        list_columns = []
        for i, value in enumerate(self.data_manager.activities):
            list_columns.append(f"Column {i}")
        self.cb_columns.configure(values=list_columns)
        
        self.redraw_table()
        
    def delete_columns(self):
        """
        It's practically the same as the previous method, but checking the current value of the 
        ComboBox to remove the column and activity with that index in the data_manager
        """
        self.update_data_from_gui()
        
        for i, value in enumerate(self.cb_columns._values):
            if self.cb_columns.get() == value:
                for j, value in enumerate(self.data_manager.weekly_log):
                    self.data_manager.weekly_log[j].pop(i)
                self.data_manager.activities.pop(i)
                list_columns = []
                for i, value in enumerate(self.data_manager.activities):
                    list_columns.append(f"Column {i}")
                self.cb_columns.configure(values=list_columns)
                
        self.redraw_table()
            
    def save_values(self):
        """
        A method that calls the method to save the current data in the data_manager, 
        and then calls the data_manager's method to save everything to a .json file
        """
        self.update_data_from_gui()
            
        self.data_manager.save_to_file()
        
    def load_values(self):
        """
        The same as in the method above, but loading the data from the .json file that must 
        have been previously created
        """
        self.data_manager.load_from_file()
        
        self.redraw_table()