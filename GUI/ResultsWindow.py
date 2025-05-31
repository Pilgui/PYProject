import tkinter as tk

from utils.Properties import Properties


def windowSetup():
    properties = Properties
    size = Properties.get("window-size")

    window = tk.Tk()
    window.title("Results")
    window.resizable(False, False)
    window.geometry(f"{size}x{size}")
    window.config(bg="#F2DDDC")


    window.mainloop()
