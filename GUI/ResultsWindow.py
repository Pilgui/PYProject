import tkinter as tk
from tkinter import ttk

from GUI.main import mainMenu
from utils.Properties import Properties




def windowSetup(results = None):
    properties = Properties()
    size = properties.get("window-size")

    results = [
        ("Anna", 10, 1),
        ("Piotr", 8, 2),
        ("Maria", 12, 3),
    ]

    window = tk.Tk()
    window.title("Results")
    window.resizable(False, False)
    window.geometry(f"{size}x{size}")
    window.config(bg="#F2DDDC")

    label = tk.Label(window, text="Results",font=("Arial", 16),background="#C3C7F4").pack(pady=10)

    tree = ttk.Treeview(window, columns=["Player","Score1","Score2"], show="headings")
    tree.heading("Player", text="Player")
    tree.heading("Score1", text="Score1")
    tree.heading("Score2", text="Score2")
    tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=10 )

    for row in results:
        tree.insert("", tk.END, values=row)

    def backButtonClick():
        window.destroy()
        mainMenu(size)

    backButton = tk.Button(window, text="Back", command=backButtonClick, background="#C3C7F4", width=10,
                           font=("Arial", 16), relief="groove")

    backButton.pack(pady=10)

    window.mainloop()
