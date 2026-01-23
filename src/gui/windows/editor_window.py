import customtkinter as ctk
import tkinter as tk

class EditorWindow(ctk.CTkToplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.data_manager = parent.data_manager
        self.title("Matrix Editor")
        self.geometry("900x600")
        self.config(bg="#a9c2c9")
        self.resizable(False, False)
        self.transient(parent)
        self.lift()
        self.create_widgets()
        self.protocol("WM_DELETE_WINDOW", self.on_close)
        
    def create_widgets(self):
        frame = ctk.CTkScrollableFrame(self, bg_color="#a9c2c9", fg_color="#72577c", width=750, height=450)
        frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        
        title = ctk.CTkLabel(
            self, text="Edit weekly study hours matrix", 
            bg_color="#a9c2c9", fg_color="#c5f7f0", text_color="#562155",
            corner_radius=60, font=("Arial", 20, "bold"))
        title.place(relx=0.5, rely=0.05, anchor=tk.CENTER)
        
        instructions = (
            "Adjust the times for each activity and day.\n"
            "You can change the names of the activities in each column.\n"
            "Use a period (.) as the decimal separator. Ex: 1.5"
        )
        
        subtitle = ctk.CTkLabel(frame, text=instructions,
            font=("Arial", 14, "bold"), text_color="#a9c2c9",
            wraplength=500,
            bg_color="#72577c")
        subtitle.grid(row=0, column=5)
        
        btn_return = ctk.CTkButton(
            self, text="Return to Menu", bg_color="#a9c2c9", fg_color="transparent",
            hover_color="#8e8ca3", font=("Arial", 14, "bold"), text_color="#562155",
            command=self.destroy, border_color="#8e8ca3", border_width=2)
        btn_return.place(relx=0.1, rely=0.95, anchor=tk.CENTER)
        
        btn_save = ctk.CTkButton(
            self, text="Save Data", bg_color="#a9c2c9", fg_color="transparent",
            hover_color="#8e8ca3", font=("Arial", 14, "bold"), text_color="#562155",
            border_color="#8e8ca3", border_width=2)
        btn_save.place(relx=0.7, rely=0.95, anchor=tk.CENTER)
        
        btn_load = ctk.CTkButton(
            self, text="Load Data", bg_color="#a9c2c9", fg_color="transparent",
            hover_color="#8e8ca3", font=("Arial", 14, "bold"), text_color="#562155",
            border_color="#8e8ca3", border_width=2)
        btn_load.place(relx=0.9, rely=0.95, anchor=tk.CENTER)
        
    def on_close(self):
        self.destroy()