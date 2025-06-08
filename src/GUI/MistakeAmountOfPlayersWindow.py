import tkinter as tk

from src.GUI.AuthorizePlayersWindow import AuthorizePlayersWindow


class MistakeAmountOfPlayersWindow:
    """
    Wyprowadza na ekran okno do dodania graczy dla gry do pierwszej pomyłki.
    """
    @staticmethod
    def window_setup(window_size, user):
        """
        Tworzy okienko do dodania graczy dla gry do pierwszej pomyłki.

        :param window_size: Rozmiar strony kwadratu okienka.
        :type window_size: int
        :param user: Użytkownik który uruchomił grę do pierwszej pomyłki.
        :type user: User
        """
        size = window_size

        window = tk.Tk()
        window.title("Gra na czas")
        window.geometry(f"{size}x{size}")
        window.configure(background="#C3C7F4")
        window.resizable(False, False)


        for i in range(5):
            window.grid_columnconfigure(i, weight=1)

        for j in range(7):
            window.grid_rowconfigure(j, weight=1)


        def back():
            window.destroy()
            from src.GUI.MainMenuWindow import MainMenuWindow
            MainMenuWindow.mainMenu(size)


        label = tk.Label(window, text="Amount of players", font=("Arial", 16),background="#C3C7F4")


        onePlayerButton = tk.Button(window, text="1 player",command=lambda : (window.destroy(), AuthorizePlayersWindow.window_setup(size,user,1)), background="#C3C7F4", width=10, font=("Arial", 16), relief="groove")
        twoPlayerButton = tk.Button(window, text="2 player",command=lambda : (window.destroy(), AuthorizePlayersWindow.window_setup(size,user,2)), background="#C3C7F4", width=10, font=("Arial", 16), relief="groove")
        threePlayerButton = tk.Button(window, text="3 player",command=lambda :(window.destroy(), AuthorizePlayersWindow.window_setup(size,user,3)), background="#C3C7F4", width=10, font=("Arial", 16), relief="groove")
        fourPlayerButton = tk.Button(window, text="4 player",command=lambda :(window.destroy(), AuthorizePlayersWindow.window_setup(size,user,4)), background="#C3C7F4", width=10, font=("Arial", 16), relief="groove")


        backButton = tk.Button(window, text="Back",command=back, background="#C3C7F4", width=10, font=("Arial", 16), relief="groove")



        label.grid(row=1, column=2, pady=10)
        onePlayerButton.grid(row=2, column=2, pady=10)
        twoPlayerButton.grid(row=3, column=2, pady=10)
        threePlayerButton.grid(row=4, column=2, pady=10)
        fourPlayerButton.grid(row=5, column=2, pady=10)
        backButton.grid(row=6, column=2, pady=10)



