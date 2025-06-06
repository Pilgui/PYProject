import tkinter as tk
from tkinter import ttk
from GUI.MainMenuWindow import MainMenuWindow


class ResultsWindow:
    @staticmethod
    def windowSetup(window_size):
        from DB.DAO import gameResultDao
        dao = gameResultDao.GameResultDAO()
        size = window_size

        results = []
        resultsArray = dao.get_all_gameResults()
        for result in resultsArray:
            strResult = str(result)
            results.append(strResult)

        window = tk.Tk()
        window.title("Results")
        window.resizable(False, False)
        window.geometry(f"{size}x{size}")
        window.config(bg="#F2DDDC")

        label = tk.Label(window, text="Results",font=("Arial", 16),background="#C3C7F4").pack(pady=10)

        tree = ttk.Treeview(window, columns=["ID","Player","Game name","Score in Time Game","Score in Game"], show="headings")
        tree.heading("ID", text="ID")
        tree.heading("Player", text="Player")
        tree.heading("Game name", text="Game name")
        tree.heading("Score in Time Game", text="Score in Time Game")
        tree.heading("Score in Game", text="Score in Game")
        tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        for row in results:
            tree.insert("", tk.END, values=row.split(","))

        def backButtonClick():
            window.destroy()
            MainMenuWindow.mainMenu(size)

        backButton = tk.Button(window, text="Back", command=backButtonClick, background="#C3C7F4", width=10,
                               font=("Arial", 16), relief="groove")

        backButton.pack(pady=10)

        window.mainloop()
