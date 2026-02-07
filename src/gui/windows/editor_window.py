import customtkinter as ctk
import tkinter as tk
from src.gui.components.matrix_table import MatrixTable

class EditorWindow(ctk.CTkToplevel):
    """
    Class containing the widgets for the secondary window to edit the array 
    (the array itself will be in a separate file and will be incorporated into the frame 
    of this window)
    """
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.data_manager = parent.data_manager # Creating a variable to store the instance called in the main window (the array and its methods)
        self.title("Matrix Editor")
        self.geometry("900x600")
        self.config(bg="#a9c2c9")
        self.resizable(False, False)
        self.transient(parent)
        self.lift()
        self.create_widgets()
        self.protocol("WM_DELETE_WINDOW", self.on_close) # For a future message that will appear when trying to close the window
        
    def create_widgets(self):
        """
        Method that creates and places widgets
        """
        frame = ctk.CTkScrollableFrame(
            self, bg_color="#a9c2c9", fg_color="#72577c", scrollbar_fg_color="#562155", 
            width=750, height=380, orientation="horizontal", scrollbar_button_hover_color="#8e8ca3",
            scrollbar_button_color="#c5f7f0")
        frame.place(relx=0.5, rely=0.55, anchor=tk.CENTER) # The frame that will contain the matrix
        
        title = ctk.CTkLabel( # Label for the title
            self, text="Edit weekly study hours matrix", 
            bg_color="#a9c2c9", fg_color="#c5f7f0", text_color="#562155",
            corner_radius=60, font=("Arial", 20, "bold"))
        title.place(relx=0.5, rely=0.05, anchor=tk.CENTER)
        
        instructions = ( # tuple with the instructions for the operation of this window
            "Adjust the times for each activity and day.\n"
            "You can change the names of the activities in each column.\n"
            "Use a period (.) as the decimal separator. Ex: 1.5\n"
            "When you're finished, click on 'Save data'"
        )
        
        subtitle = ctk.CTkLabel(self, text=instructions, # Label where the previously mentioned instructions will go
            font=("Arial", 14, "bold"), text_color="#72577c",
            wraplength=500,
            bg_color="#a9c2c9")
        subtitle.place(relx=0.5, rely=0.14, anchor=tk.CENTER)
        
        def information(texto, info=""):
            info += texto
            self.errors.configure(text=info)
        
        self.errors = ctk.CTkLabel(
            self, text="information", bg_color="#a9c2c9", fg_color="#562155", text_color="#c5f7f0", 
            font=("Arial", 12, "bold"), width=200, height=100, wraplength=190, corner_radius=10
        )
        self.errors.place(relx=0.86, rely=0.1, anchor=tk.CENTER)
        
        self.matrix_table = MatrixTable(frame, self.data_manager, callback=information) # Call to the class to be able to locate the table
        self.matrix_table.grid(row=5, column=3)
        
        self.matrix_table.btn_delete.configure(command=self.delete_column_action) # Pass the method to delete columns to the delete button in matrix_table.py
        
        btn_return = ctk.CTkButton( # Button to return to the main window
            self, text="Return to Menu", bg_color="#a9c2c9", fg_color="transparent",
            hover_color="#8e8ca3", font=("Arial", 14, "bold"), text_color="#562155",
            command=self.on_close, border_color="#8e8ca3", border_width=2)
        btn_return.place(relx=0.1, rely=0.95, anchor=tk.CENTER)
        
        self.btn_add_column = ctk.CTkButton( # Button to add columns
            self, text="Add Column", bg_color="#a9c2c9", fg_color="transparent",
            hover_color="#8e8ca3", font=("Arial", 14, "bold"), text_color="#562155",
            border_color="#8e8ca3", border_width=2, text_color_disabled="#8e8ca3",
            command=self.add_column_action)
        self.btn_add_column.place(relx=0.5, rely=0.95, anchor=tk.CENTER)
        
        btn_save = ctk.CTkButton( # Button to save the modified array data; the data_manager variable will be used here.
            self, text="Save Data", bg_color="#a9c2c9", fg_color="transparent",
            hover_color="#8e8ca3", font=("Arial", 14, "bold"), text_color="#562155",
            border_color="#8e8ca3", border_width=2, command=self.matrix_table.save_values)
        btn_save.place(relx=0.7, rely=0.95, anchor=tk.CENTER)
        
        btn_load = ctk.CTkButton( # Exactly the same as above, but for loading the data
            self, text="Load Data", bg_color="#a9c2c9", fg_color="transparent",
            hover_color="#8e8ca3", font=("Arial", 14, "bold"), text_color="#562155",
            border_color="#8e8ca3", border_width=2, command=self.matrix_table.load_values)
        btn_load.place(relx=0.9, rely=0.95, anchor=tk.CENTER)
        
    def add_column_action(self):
        """
        Method that calls the matrix_table method to add a column, 
        also calls the button_state method
        """
        self.matrix_table.add_columns()
        self.button_state()
        
    def delete_column_action(self):
        """
        Exactly the same as above, but to delete
        """
        self.matrix_table.delete_columns()
        self.button_state()
        
    def button_state(self): 
        """
        Method to activate and deactivate the buttons to add and delete columns, 
        when they are not within the range [3,10]
        """
        if len(self.data_manager.activities) >= 10:
            self.btn_add_column.configure(state="disabled")
        else:
            self.btn_add_column.configure(state="normal")
            
        if len(self.data_manager.activities) <= 3:
            self.matrix_table.btn_delete.configure(state="disabled")
        else:
            self.matrix_table.btn_delete.configure(state="normal")
        
    def on_close(self):
        """
        This method is where the previously mentioned information about the message when 
        trying to close the window will be put
        """
        self.parent.comprobation()
        self.destroy()