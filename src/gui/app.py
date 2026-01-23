"""
This program serves as the main window configuration
"""
import customtkinter as ctk
from src.gui.windows.main_window import MainWindow # Here, it is imported as a module into main_window.py, which contains all the widgets and general design

def run_app():
    """
    Function to configure the app's theme, in addition to calling the MainWindow class 
    that was imported earlier
    """
    ctk.set_appearance_mode("light")
    app = MainWindow()
    app.mainloop()
    
if __name__ == "__main__":
    run_app()