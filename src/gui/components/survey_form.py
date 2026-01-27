import customtkinter as ctk
import tkinter as tk

class SurveyForm1(ctk.CTkFrame):
    def __init__(self, master, data_manager):
        super().__init__(master)
        self.data_manager = data_manager
        self.configure(fg_color="#72577c")
        self.create_widgets()
        
    def create_widgets(self):
        for i, value in enumerate(self.data_manager.activities):
            activities = ctk.CTkLabel(
                self, text=value, bg_color="#72577c", fg_color="#562155", text_color="#c5f7f0",
                corner_radius=60, font=("Arial", 14, "bold")
            )
            activities.grid(row=i, column=0, pady=5)
            
            radio_var = tk.IntVar(value=0)
            
            option1 = ctk.CTkRadioButton(
                self, text="Theory", variable=radio_var, value=1, text_color="#c5f7f0",
                hover_color="#8e8ca3", fg_color="#562155",font=("Arial", 14, "bold")
            )
            option1.grid(row=i, column=1, padx=50)
            
            option2 = ctk.CTkRadioButton(
                self, text="Practice", variable=radio_var, value=2, text_color="#c5f7f0",
                hover_color="#8e8ca3", fg_color="#562155", font=("Arial", 14, "bold")
            )
            option2.grid(row=i, column=2, padx=5)
            
class SurveyForm2(ctk.CTkFrame):
    def __init__(self, master, data_manager):
        super().__init__(master)
        self.data_manager = data_manager
        self.configure(fg_color="#72577c")
        self.create_widgets()
        
    def create_widgets(self):
        order1 = ctk.CTkLabel(
            self, text="How difficult are you finding the following activities? (Difficulty (1-5))", 
            bg_color="#72577c", fg_color="#562155", text_color="#c5f7f0",
            corner_radius=60, font=("Arial", 14, "bold")
            )
        order1.grid(row=0, column=0, columnspan=2)
        
        for i, value in enumerate(self.data_manager.activities):
            activities = ctk.CTkLabel(
                self, text=value, bg_color="#72577c", fg_color="#562155", text_color="#c5f7f0",
                corner_radius=60, font=("Arial", 14, "bold")
            )
            activities.grid(row=i+1, column=0, pady=5)
            
            sliders = ctk.CTkSlider(
                self, from_=0, to=4
            )
            sliders.grid(row=i+1, column=1)