import tkinter as tk

from GUI import TimeGame
import SettingsWindow
from GUI.SettingsWindow import windowSetup
from utils.Properties import Properties

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
        mainMenu()
    backButton = tk.Button(window, text="Powrót", command=backButtonClick, background="#C3C7F4", width=10, font=("Arial", 16), relief="groove")

    gameTypeLabel.grid(row=0, column=0, columnspan=5, pady=80,sticky="ew")
    startTimeGameButton.grid(row=1, column=1, pady=10, padx=10)
    startFailGameButton.grid(row=1, column=3, pady=10, padx=10)
    backButton.grid(row=3, column=0, columnspan=5, pady=40)

    window.mainloop()


def mainMenu(size):
    menuWindow = tk.Tk()
    menuWindow.geometry(f"{size}x{size}")
    menuWindow.resizable(False, False)
    menuWindow.title("Krzyżówka")
    menuWindow.config(bg="#F2DDDC")
    main_size = size

    print(main_size)

    for i in range(5):
        menuWindow.grid_columnconfigure(i, weight=1)

    menuNameLabel = tk.Label(menuWindow,text="Krzyżówka", font=("Arial", 16),background="#C3C7F4",width=100)
    menuNameLabel.grid(row=2, column=2,pady=50)


    def buttonQuit():
        menuWindow.destroy()

    def buttonStart():
        menuWindow.destroy()
        gameTypeMenu(size)

    def settingsMenu():
        menuWindow.destroy()
        windowSetup()

    menuButtonStart = tk.Button(menuWindow, text="Start", command=buttonStart, background="#C3C7F4", width=10, font=("Arial", 16), relief="groove")
    menuButtonQuit = tk.Button(menuWindow, text="Quit", command=buttonQuit, background="#C3C7F4", width=10, font=("Arial", 16), relief="groove")
    menuSettingsMenu = tk.Button(menuWindow, text="Settings", command=settingsMenu, background="#C3C7F4", width=10, font=("Arial", 16), relief="groove")

    menuButtonStart.grid(row=3, column=2,pady=50)
    menuButtonQuit.grid(row=4, column=2)
    menuSettingsMenu.grid(row=5, column=2, pady=50)

    menuWindow.mainloop()

if(__name__ == "__main__"):
    mainMenu(main_size)