from GUI import SettingsWindow, ResultsWindow
from GUI.AuthorizationWindow import AuthorizationWindow
import tkinter as tk


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
        AuthorizationWindow.windowSetup()
        # gameTypeMenu(size)

    def settingsMenu():
        menuWindow.destroy()
        SettingsWindow.windowSetup()

    def buttonResults():
        menuWindow.destroy()
        ResultsWindow.windowSetup()


    menuButtonStart = tk.Button(menuWindow, text="Start", command=buttonStart, background="#C3C7F4", width=10, font=("Arial", 16), relief="groove")
    menuButtonQuit = tk.Button(menuWindow, text="Quit", command=buttonQuit, background="#C3C7F4", width=10, font=("Arial", 16), relief="groove")
    menuSettingsMenu = tk.Button(menuWindow, text="Settings", command=settingsMenu, background="#C3C7F4", width=10, font=("Arial", 16), relief="groove")
    menuButtonResults = tk.Button(menuWindow, text="Results", command=buttonResults, background="#C3C7F4", width=10, font=("Arial", 16), relief="groove")

    menuButtonStart.grid(row=3, column=2,pady=50)
    menuButtonResults.grid(row=4, column=2)
    menuSettingsMenu.grid(row=5, column=2, pady=50)
    menuButtonQuit.grid(row=6, column=2)


    menuWindow.mainloop()