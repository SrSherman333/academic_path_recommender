import customtkinter as ctk
import tkinter as tk

class SurveyForm1(ctk.CTkFrame):
    def __init__(self, master, data_manager):
        super().__init__(master)
        self.data_manager = data_manager
        self.configure(fg_color="#72577c")
        self.radio_buttons = []
        self.create_widgets()
        
    def create_widgets(self):
        title = ctk.CTkLabel(
            self, text="Classification of Activities", bg_color="#72577c", fg_color="#562155", text_color="#c5f7f0",
            corner_radius=60, font=("Arial", 14, "bold")
        )
        title.grid(row=0, column=1, columnspan=2, pady=5)
        
        self.radio_vars = {}
        
        for i, value in enumerate(self.data_manager.activities):
            activities = ctk.CTkLabel(
                self, text=value, bg_color="#72577c", fg_color="#562155", text_color="#c5f7f0",
                corner_radius=60, font=("Arial", 14, "bold")
            )
            activities.grid(row=i+1, column=0, pady=5, padx=5)
            
            self.radio_vars[value] = tk.IntVar(value=0)
            current_var = self.radio_vars[value]
            
            self.option1 = ctk.CTkRadioButton(
                self, text="Theory", variable=current_var, value=1, text_color="#c5f7f0",
                hover_color="#8e8ca3", fg_color="#562155",font=("Arial", 14, "bold")
            )
            self.option1.grid(row=i+1, column=1, padx=50)
            
            self.radio_buttons.append(self.option1)
            
            self.option2 = ctk.CTkRadioButton(
                self, text="Practice", variable=current_var, value=2, text_color="#c5f7f0",
                hover_color="#8e8ca3", fg_color="#562155", font=("Arial", 14, "bold")
            )
            self.option2.grid(row=i+1, column=2, padx=5)
            
            self.radio_buttons.append(self.option2)
            
class SurveyForm2(ctk.CTkFrame):
    def __init__(self, master, data_manager):
        super().__init__(master)
        self.data_manager = data_manager
        self.configure(fg_color="#72577c")
        self.create_widgets()
        
    def create_widgets(self):
        title = ctk.CTkLabel(
            self, text="Academic Survey", bg_color="#72577c", fg_color="#562155", text_color="#c5f7f0",
            corner_radius=60, font=("Arial", 14, "bold")
        )
        title.grid(row=0, column=0, columnspan=2, pady=5)
        
        order1 = ctk.CTkLabel(
            self, text="1. Difficulty of the activities (1:low - 5:very difficult):", 
            bg_color="#72577c", fg_color="#72577c", text_color="#c5f7f0", font=("Arial", 14, "bold")
            )
        order1.grid(row=1, column=0, pady=5, padx=5)
        
        self.widgets_sliders = []
        widgets_levels = []
        
        def slider_event(event):
            for i, value in enumerate(self.widgets_sliders):
                value = value.get()
                widgets_levels[i].configure(text=f"{int(value)}")
        
        for i, value in enumerate(self.data_manager.activities):
            activities = ctk.CTkLabel(
                self, text=value, bg_color="#72577c", fg_color="#562155", text_color="#c5f7f0",
                corner_radius=60, font=("Arial", 14, "bold")
            )
            activities.grid(row=i+2, column=0, pady=5)
            
            sliders = ctk.CTkSlider(
                self, from_=1, to=5, fg_color="#c5f7f0", progress_color="#8e8ca3",
                button_color="#562155", button_hover_color="#8e8ca3", number_of_steps=4,
                command=slider_event
            )
            sliders.grid(row=i+2, column=1)
            sliders.set(1)
            self.widgets_sliders.append(sliders)
            
            levels = ctk.CTkLabel(
                self, text="1", bg_color="#72577c", fg_color="#562155", text_color="#c5f7f0",
                corner_radius=60, font=("Arial", 14, "bold")
            )
            levels.grid(row=i+2, column=2, pady=5, padx=5)
            widgets_levels.append(levels)
            
        order2 = ctk.CTkLabel(
            self, text="2. Available hours per day (e.g., 4.5):", 
            bg_color="#72577c", fg_color="#72577c", text_color="#c5f7f0", font=("Arial", 14, "bold")
            )
        order2.grid(row=(len(widgets_levels)+3)-1, column=0, pady=5, padx=5)
        
        self.hours_var = ctk.StringVar(value="")
        
        self.hours_entrie = ctk.CTkEntry(self, width=50, placeholder_text="0.0", textvariable=self.hours_var)
        self.hours_entrie.grid(row=(len(widgets_levels)+3)-1, column=1, pady=5, padx=5)
        
        self.errors = ctk.CTkLabel(
            self, text="Possible errors will appear here", bg_color="#72577c", fg_color="#562155", text_color="#c5f7f0", 
            font=("Arial", 12, "bold"), width=150, height=100, wraplength=90, corner_radius=10
        )
        self.errors.grid(row=(len(widgets_levels)+3)-1, column=2, columnspan=2, rowspan=3, pady=5)
        
        order3 = ctk.CTkLabel(
            self, text="3. Minimum threshold of hours/day (Hmin, e.g., 3.0):", 
            bg_color="#72577c", fg_color="#72577c", text_color="#c5f7f0", font=("Arial", 14, "bold")
            )
        order3.grid(row=(len(widgets_levels)+4)-1, column=0, pady=5, padx=5)
        
        self.Hmin_var = ctk.StringVar(value="")
        
        self.Hmin_entrie = ctk.CTkEntry(self, width=50, placeholder_text="0.0", textvariable=self.Hmin_var)
        self.Hmin_entrie.grid(row=(len(widgets_levels)+4)-1, column=1, pady=5, padx=5)
        
        order4 = ctk.CTkLabel(
            self, text="4. Minimum practice threshold (Pmin, 0.0-1.0, e.g., 0.3):", 
            bg_color="#72577c", fg_color="#72577c", text_color="#c5f7f0", font=("Arial", 14, "bold")
            )
        order4.grid(row=(len(widgets_levels)+5)-1, column=0, pady=5, padx=5)
        
        self.Pmin_var = ctk.StringVar(value="")
        
        self.Pmin_entrie = ctk.CTkEntry(self, width=50, placeholder_text="0.0", textvariable=self.Pmin_var)
        self.Pmin_entrie.grid(row=(len(widgets_levels)+5)-1, column=1, pady=5, padx=5)