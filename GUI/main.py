import tkinter as tk

from GUI import TimeGame, ResultsWindow
import SettingsWindow
from GUI.AuthorizationWindow import AuthorizationWindow
from GUI.SettingsWindow import windowSetup
from utils.Properties import Properties
from GUI.startMenu import mainMenu


properties = Properties()
main_size = properties.get("window-size")


def gameTypeMenu(size):
    window = tk.Tk()
    window.title("Game Type")
    window.resizable(False, False)
    window.geometry(f"{size}x{size}")
    window.config(bg="#F2DDDC")

    for i in range(5):
        window.grid_columnconfigure(i, weight=1)

    gameTypeLabel = tk.Label(window, text="Game Type", font=("Arial", 16),background="#C3C7F4")

    def startTimedGame():
        window.destroy()
        TimeGame.startTimedGame(size)
    startTimeGameButton = tk.Button(window,text="Gra na czas", background="#C3C7F4", width=25, font=("Arial", 14), relief="groove",command=startTimedGame)

    startFailGameButton = tk.Button(window,text="Gra do pierwszego błędu", background="#C3C7F4",width=25, font=("Arial", 14), relief="groove")

    def backButtonClick():
        window.destroy()
        mainMenu(size)

    backButton = tk.Button(window, text="Back", command=backButtonClick, background="#C3C7F4", width=10, font=("Arial", 16), relief="groove")

    gameTypeLabel.grid(row=0, column=0, columnspan=5, pady=80,sticky="ew")
    startTimeGameButton.grid(row=1, column=1, pady=10, padx=10)
    startFailGameButton.grid(row=1, column=3, pady=10, padx=10)
    backButton.grid(row=3, column=0, columnspan=5, pady=40)

    window.mainloop()


if(__name__ == "__main__"):
    mainMenu(main_size)