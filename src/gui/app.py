import customtkinter as ctk
from src.gui.windows.main_window import MainWindow

def run_app():
    ctk.set_appearance_mode("dark")
    app = MainWindow()
    app.mainloop()
    
if __name__ == "__main__":
    run_app()