import customtkinter as ctk
import tkinter as tk
from src.gui.components.survey_form import SurveyForm1, SurveyForm2

class SurveyWindow(ctk.CTkToplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.data_manager = parent.data_manager
        self.title("Academic Survey")
        self.geometry("900x600")
        self.config(bg="#a9c2c9")
        self.resizable(False, False)
        self.transient(parent)
        self.lift()
        self.create_widgets()
        
    def create_widgets(self):
        title = ctk.CTkLabel(
            self, text="Take the academic survey", bg_color="#a9c2c9", fg_color="#c5f7f0", 
            text_color="#562155", corner_radius=60, font=("Arial", 20, "bold"))
        title.place(relx=0.5, rely=0.05, anchor=tk.CENTER)
        
        instructions1 = ctk.CTkLabel(
            self, text="Section 1: Classify each activity as theoretical or practical", 
            font=("Arial", 14, "bold"), text_color="#72577c", wraplength=500, 
            bg_color="#a9c2c9")
        instructions1.place(relx=0.3, rely=0.1, anchor=tk.CENTER)
        
        frame1 = ctk.CTkScrollableFrame(
            self, bg_color="#a9c2c9", fg_color="#72577c", scrollbar_fg_color="#562155", 
            width=750, height=200, orientation="vertical", scrollbar_button_hover_color="#8e8ca3",
            scrollbar_button_color="#c5f7f0")
        frame1.place(relx=0.5, rely=0.3, anchor=tk.CENTER)
        
        self.survey_form1 = SurveyForm1(frame1, self.data_manager)
        self.survey_form1.grid(row=0, column=0)
        
        instructions2 = ctk.CTkLabel(
            self, text="Section 2: Answer the following questions", 
            font=("Arial", 14, "bold"), text_color="#72577c", wraplength=500, 
            bg_color="#a9c2c9")
        instructions2.place(relx=0.24, rely=0.52, anchor=tk.CENTER)
        
        frame2 = ctk.CTkScrollableFrame(
            self, bg_color="#a9c2c9", fg_color="#72577c", scrollbar_fg_color="#562155", 
            width=750, height=200, orientation="vertical", scrollbar_button_hover_color="#8e8ca3",
            scrollbar_button_color="#c5f7f0")
        frame2.place(relx=0.5, rely=0.72, anchor=tk.CENTER)
        
        self.survey_form2 = SurveyForm2(frame2, self.data_manager)
        self.survey_form2.grid(row=0, column=0)
        
        btn_return = ctk.CTkButton( # Button to return to the main window
            self, text="Return to Menu", bg_color="#a9c2c9", fg_color="transparent",
            hover_color="#8e8ca3", font=("Arial", 14, "bold"), text_color="#562155",
            command=self.destroy, border_color="#8e8ca3", border_width=2)
        btn_return.place(relx=0.1, rely=0.95, anchor=tk.CENTER)
        
        self.btn_save = ctk.CTkButton(
            self, text="Survey Completed", bg_color="#a9c2c9", fg_color="transparent",
            hover_color="#8e8ca3", font=("Arial", 14, "bold"), text_color="#562155", 
            border_color="#8e8ca3", border_width=2, state="disabled", text_color_disabled="#8e8ca3",
            command=self.save_values)
        self.btn_save.place(relx=0.9, rely=0.95, anchor=tk.CENTER)
        
        for i in self.survey_form1.radio_buttons:
            i.configure(command=self.check_values)
        
        self.survey_form2.hours_var.trace_add("write", self.check_values)
        self.survey_form2.Hmin_var.trace_add("write", self.check_values)
        self.survey_form2.Pmin_var.trace_add("write", self.check_values)
        
    def check_values(self, *args):
        enable = None
        values = []
        for i, j in self.survey_form1.radio_vars.items():
            values.append(j.get())
        if 0 in values:
            enable = False
        else:
            enable = True
        
        if enable == True and self.survey_form2.hours_var.get() != "" and self.survey_form2.Hmin_var.get() != "" and self.survey_form2.Pmin_var.get() != "":
            self.btn_save.configure(state="normal")
        else:
            self.btn_save.configure(state="disabled")
            
    def save_values(self):
        try:
            h = float(self.survey_form2.hours_entrie.get())
            Hmin = float(self.survey_form2.Hmin_entrie.get())
            Pmin = float(self.survey_form2.Pmin_entrie.get())
        except ValueError:
            self.survey_form2.errors.configure(text="Error: Enter only numbers, not letters or symbols")
            self.after(3000, lambda:self.survey_form2.errors.configure(text="Possible errors will appear here"))
            
        fails = 0
        if not 0 < h <= 24:
            fails += 1
            self.survey_form2.hours_entrie.configure(border_color="red")
        else:
            self.survey_form2.hours_entrie.configure(border_color="gray")
            
        if not 0 < Hmin <= h:
            fails += 1
            self.survey_form2.Hmin_entrie.configure(border_color="red")
        else:
            self.survey_form2.Hmin_entrie.configure(border_color="gray")
            
        if not 0 <= Pmin <= 1:
            fails += 1
            self.survey_form2.Pmin_entrie.configure(border_color="red")
        else:
            self.survey_form2.Pmin_entrie.configure(border_color="gray")
            
        if fails > 0:
            self.survey_form2.errors.configure(text=f"Error: There are {fails} value(s) out of range, Correct it to continue")
            self.after(3000, lambda:self.survey_form2.errors.configure(text="Possible errors will appear here"))
        else:
            self.data_manager.survey_data.clear()
            count = 0
            for i, j in self.survey_form1.radio_vars.items():
                self.data_manager.survey_data[i] = (j.get(), int(self.survey_form2.widgets_sliders[count].get()))
                count += 1
            self.data_manager.survey_data["h"] = h
            self.data_manager.survey_data["Hmin"] = Hmin
            self.data_manager.survey_data["Pmin"] = Pmin
        print(self.data_manager.survey_data)