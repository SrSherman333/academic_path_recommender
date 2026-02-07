import customtkinter as ctk
from PIL import Image, ImageTk
import tkinter as tk

class MainWindow(ctk.CTk):
    """
    Class that creates all the widgets of the main window, as well as its functionality 
    to call the secondary windows
    """
    def __init__(self):
        super().__init__()
        from src.core.data_manager import data_manager # An instance of the StudyDataManager class is imported, which contains the array and several necessary methods; it will be used later
        """
        Basic window settings
        """
        self.title("Academic Path Recommender")
        self.geometry("500x450")
        self.config(bg="#a9c2c9")
        self.resizable(False, False)
        self.data_manager = data_manager # Variable to access the imported instance
        self.editor_window = None
        self.survey_window = None
        self.step1 = False
        self.step2 = False
        self.create_widgets() # Call the method responsible for creating and placing widgets
        
    def create_widgets(self):
        """
        Method for creating and placing widgets
        """
        title = ctk.CTkLabel( # Label for the title
            self, text="Welcome to the Academic Path Recommender", 
            bg_color="#a9c2c9", fg_color="#c5f7f0", text_color="#562155",
            corner_radius=60, font=("Arial", 20, "bold"))
        title.place(relx=0.5, rely=0.1, anchor=tk.CENTER)
        
        try: # Upload image for decoration
            icon_menu_original = Image.open("docs/images/img_icon_menu.png")
            icon_menu = ctk.CTkImage(light_image=icon_menu_original, size=(100, 100))
        except Exception as e:
            print(f"Error to loading the image: {e}")
            icon_menu = None
            
        if icon_menu: # Creation and placement of the label where the image will go
            icon = ctk.CTkLabel(self, text="", image=icon_menu, bg_color="#a9c2c9")
            icon.image = icon_menu
        else:
            icon = ctk.CTkLabel(self, text="😇", bg_color="#a9c2c9", font=("Arial", 20, "bold"))
            
        icon.place(relx=0.5, rely=0.25, anchor=tk.CENTER)
        
        
        subtitle = ctk.CTkLabel( # Label for the subtitle
            self, text="This application analyzes your study habits and suggests a personalized learning path",
            font=("Arial", 14, "bold"), text_color="#72577c",
            wraplength=500,
            bg_color="#a9c2c9")
        subtitle.place(relx=0.5, rely=0.4, anchor=tk.CENTER)
        
        btn_matrix = ctk.CTkButton( # Button to open the secondary window where the matrix will be edited
            self, text="1. Edit my weekly matrix", bg_color="#a9c2c9", fg_color="#c5f7f0",
            hover_color="#a9c2c9", font=("Arial", 14,"bold"), text_color="#562155",
            command=self.open_editor_window)
        btn_matrix.place(relx=0.5, rely=0.55, anchor=tk.CENTER)

        btn_survey = ctk.CTkButton( # Button to open the window where the respective survey will be answered
            self, text="2. Conduct Skills Survey", bg_color="#a9c2c9", fg_color="#c5f7f0",
            hover_color="#a9c2c9", font=("Arial", 14, "bold"), text_color="#562155",
            command=self.open_survey_window)
        btn_survey.place(relx=0.5, rely=0.65, anchor=tk.CENTER)
        
        self.btn_results = ctk.CTkButton( # Button to open the window where the results, including the graphs, will be displayed
            self, text="3. View results", bg_color="#a9c2c9", fg_color="#8e8ca3",
            hover_color="#72577c", font=("Arial", 14, "bold"), text_color="white",
            state="disable") # Disabled until the survey is completed
        self.btn_results.place(relx=0.5, rely=0.75, anchor=tk.CENTER)
        
        btn_exit = ctk.CTkButton( # Button to close the app
            self, text="Exit", bg_color="#a9c2c9", fg_color="transparent",
            hover_color="#8e8ca3", font=("Arial", 14, "bold"), text_color="#562155",
            command=self.destroy, border_color="#8e8ca3", border_width=2)
        btn_exit.place(relx=0.5, rely=0.9, anchor=tk.CENTER)
        
    def comprobation(self):
        total_matrix = []
        for i in self.data_manager.weekly_log:
            total_matrix.append(sum(i))
        
        if sum(total_matrix) > 0:
            self.step1 = True
            print(f"Paso 1: {self.step1}")
        else:
            self.step1 = False
            print(f"Paso 1: {self.step1}")
            
        if self.data_manager.survey_data["h"] > 0:
            self.step2 = True
            print(f"Paso 2: {self.step2}")
        else:
            self.step2 = False
            print(f"Paso 2: {self.step2}")
            
        if self.step1 and self.step2:
            self.btn_results.configure(state="normal", fg_color="#c5f7f0", 
                                    hover_color="#a9c2c9", text_color="#562155")
        else:
            self.btn_results.configure(state="disabled", fg_color="#8e8ca3", text_color="white")
        
    def open_editor_window(self):
        """
        The method that is called when the first button is pressed is the one that opens the window to edit the matrix
        """
        from src.gui.windows.editor_window import EditorWindow
        if self.editor_window is None or not self.editor_window.winfo_exists():
            self.editor_window = EditorWindow(self)
            self.editor_window.grab_set()
        else:
            self.editor_window.focus()
            
    def open_survey_window(self):
        from src.gui.windows.survey_window import SurveyWindow
        if self.survey_window is None or not self.survey_window.winfo_exists():
            self.survey_window = SurveyWindow(self)
            self.survey_window.grab_set()
        else:
            self.survey_window.focus()