import tkinter as tk

from src.GUI.TimeGame import TimeGame
from src.GUI.MainMenuWindow import MainMenuWindow

class GameTypeMenuWindow:
    """
    Okno wyboru typu gry w krzyżówcę.

    Wyświetla menu z trzema opcjami:
    - Gra na czas
    - Gra do pierwszego błędu
    - Powrót do głównego menu

    Zależnie od zalogowanego użytkownika pokazuje imię lub "Guest".
    """
    def window_setup(size, user):
        """
        Tworzy i wyświetla okno wyboru typu gry.

        :param size: Rozmiar strony kwadratu okienka.
        :type size: int
        :param user: Obiekt użytkownika lub None (jeśli gra jako gość).
        :type user: User | None
        """
        if user != None:
            user_name = user.username
        else:
            user_name = "Guest"

        window = tk.Tk()
        window.title("Game Type")
        window.resizable(False, False)
        window.geometry(f"{size}x{size}")
        window.config(bg="#F2DDDC")

        for i in range(5):
            window.grid_columnconfigure(i, weight=1)

        gameTypeLabel = tk.Label(window, text="Game Type", font=("Arial", 16),background="#C3C7F4")
        nameUserLabel = tk.Label(window, text=f"Name: {user_name}", font=("Arial", 16),background="#C3C7F4")

        def startTimedGame():
            window.destroy()
            TimeGame.startTimedGame(size,user)

        def startMistakeGame():
            window.destroy()
            from src.GUI.MistakeAmountOfPlayersWindow import MistakeAmountOfPlayersWindow
            MistakeAmountOfPlayersWindow.window_setup(size,user)

        startTimeGameButton = tk.Button(window,text="Gra na czas", background="#C3C7F4", width=25, font=("Arial", 14), relief="groove",command=startTimedGame)

        startFailGameButton = tk.Button(window,text="Gra do pierwszego błędu", background="#C3C7F4",width=25, font=("Arial", 14), relief="groove",command=startMistakeGame)

        def backButtonClick():
            window.destroy()
            MainMenuWindow.mainMenu(size)

        backButton = tk.Button(window, text="Back", command=backButtonClick, background="#C3C7F4", width=10, font=("Arial", 16), relief="groove")

        nameUserLabel.grid(row=0, column=0, columnspan=3)
        gameTypeLabel.grid(row=1, column=0, columnspan=5, pady=80,sticky="ew")
        startTimeGameButton.grid(row=2, column=1, pady=10, padx=10)
        startFailGameButton.grid(row=2, column=3, pady=10, padx=10)
        backButton.grid(row=4, column=0, columnspan=5, pady=40)

        window.mainloop()

