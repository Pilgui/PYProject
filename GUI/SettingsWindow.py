import tkinter as tk
from tkinter import messagebox

import GUI.main as main
from utils.Properties import Properties


def windowSetup():
    properties = Properties()
    current_size = properties.get("window-size")

    window = tk.Tk()
    window.title("Settings")
    window.geometry(f"{current_size}x{current_size}")
    window.configure(background="#C3C7F4")
    window.resizable(False, False)

    for i in range(5):
        window.grid_columnconfigure(i, weight=1)

    label = tk.Label(window, text="Settings", font=("Arial", 16), background="#C3C7F4")
    label.grid(row=0, column=0, columnspan=5, pady=40)

    sizeLabel = tk.Label(window, text="Window size:", font=("Arial", 12), background="#F2DDDC")
    sizeLabel.grid(row=1, column=1, pady=10)

    size_options = ["500 x 500", "800 x 800", "1000 x 1000"]
    size_var = tk.StringVar()
    size_var.set(f"{current_size} x {current_size}")

    sizeMenu = tk.OptionMenu(window, size_var, *size_options)
    sizeMenu.config(font=("Arial", 12), bg="#C3C7F4", relief="groove", width=12)
    sizeMenu.grid(row=1, column=2, pady=10, padx=10)



    def save():
        selected = size_var.get()
        try:
            new_size = int(selected.split("x")[0].strip())
            properties.set("window-size", new_size)
            messagebox.showinfo("Settings Saved", "Settings saved")
            window.destroy()
            main.mainMenu(new_size)
        except Exception as e:
            messagebox.showerror("Error", e)

    def goBack():
        window.destroy()
        main.mainMenu(current_size)

    saveButton = tk.Button(window, text="Save", command=save, background="#C3C7F4", font=("Arial", 14), relief="groove", width=12)
    saveButton.grid(row=2, column=2, pady=10)

    backButton = tk.Button(window, text="Go back", command=goBack, background="#C3C7F4", font=("Arial", 14),relief="groove", width=12)
    backButton.grid(row=3, column=2, pady=20)

    window.mainloop()




