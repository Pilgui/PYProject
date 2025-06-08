import tkinter as tk
from tkinter import messagebox

from src.GUI.MainMenuWindow import MainMenuWindow
from src.utils.Properties import Properties


def windowSetup():
    """
    Tworzy okienko ustawień gry.
    """
    properties = Properties()
    current_size = properties.get("window-size")
    current_level = properties.get("level")
    current_theme = properties.get("theme")

    window = tk.Tk()
    window.title("Settings")
    window.geometry(f"{current_size}x{current_size}")
    window.configure(background="#C3C7F4")
    window.resizable(False, False)

    for i in range(5):
        window.grid_columnconfigure(i, weight=1)

    for i in range(6):
        window.rowconfigure(i, weight=1)

    label = tk.Label(window, text="Settings", font=("Arial", 16), background="#C3C7F4")
    label.grid(row=0, column=0, columnspan=5, pady=40)

    sizeLabel = tk.Label(window, text="Window size:", font=("Arial", 12), background="#F2DDDC")
    sizeLabel.grid(row=1, column=1, pady=10, sticky=tk.E)

    levelLabel = tk.Label(window, text="Level :", font=("Arial", 12), background="#F2DDDC")
    levelLabel.grid(row=2, column=1, pady=10, sticky=tk.E)

    themeLabel = tk.Label(window, text="Theme :", font=("Arial", 12), background="#F2DDDC")
    themeLabel.grid(row=3, column=1, pady=10, sticky=tk.E)

    size_options = ["800 x 800", "1000 x 1000"]
    size_var = tk.StringVar()
    size_var.set(f"{current_size} x {current_size}")

    sizeMenu = tk.OptionMenu(window, size_var, *size_options)
    sizeMenu.config(font=("Arial", 12), bg="#C3C7F4", relief="groove", width=12)
    sizeMenu.grid(row=1, column=2, pady=10, padx=10)

    level_options = ["1","2","3"]
    level_var = tk.StringVar()
    level_var.set(current_level)

    levelMenu = tk.OptionMenu(window, level_var, *level_options)
    levelMenu.config(font=("Arial", 12), bg="#C3C7F4", relief="groove", width=12)
    levelMenu.grid(row=2, column=2, pady=10, padx=10)

    theme_options = ["Geography", "Animals", "Science","Technology","History"]
    theme_var = tk.StringVar()
    theme_var.set(current_theme)

    themeMenu = tk.OptionMenu(window, theme_var, *theme_options)
    themeMenu.config(font=("Arial", 12), bg="#C3C7F4", relief="groove", width=12)
    themeMenu.grid(row=3, column=2, pady=10, padx=10)



    def save():
        selected = size_var.get()
        try:
            new_size = int(selected.split("x")[0].strip())
            properties.set("window-size", new_size)
            properties.set("level", int(level_var.get()))
            properties.set("theme", theme_var.get())
            print(int(level_var.get()))
            messagebox.showinfo("Settings Saved", "Settings saved")
            window.destroy()
            MainMenuWindow.mainMenu(new_size)
        except Exception as e:
            messagebox.showerror("Error", e)

    def goBack():
        window.destroy()
        MainMenuWindow.mainMenu(current_size)

    saveButton = tk.Button(window, text="Save", command=save, background="#C3C7F4", font=("Arial", 14), relief="groove", width=12)
    saveButton.grid(row=4, column=2, pady=10)

    backButton = tk.Button(window, text="Go back", command=goBack, background="#C3C7F4", font=("Arial", 14),relief="groove", width=12)
    backButton.grid(row=5, column=2, pady=20)

    window.mainloop()




