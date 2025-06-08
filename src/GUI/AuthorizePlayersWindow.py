
import tkinter as tk
from tkinter import simpledialog, messagebox

from src.GUI.MistakeGame import MistakeGame


class AuthorizePlayersWindow:
    """
    Okno GUI umożliwiające zalogowanie wielu graczy przed rozpoczęciem gry.

    Każdy gracz może się zalogować lub gość jako grać. Po zatwierdzeniu użytkowników
    uruchamiana jest gra z uwzględnieniem wszystkich zarejestrowanych graczy.
    """

    @staticmethod
    def window_setup(window_size, main_user, player_amount):
        """
        Tworzy okno logowania graczy oraz przycisk do rozpoczęcia gry.

        :param window_size: Rozmiar strony kwadratu okienka.
        :type window_size: int
        :param main_user: Obiekt użytkownika, który rozpoczął grę.
        :type main_user: User
        :param player_amount: Liczba graczy (łącznie z głównym użytkownikiem).
        :type player_amount: int
        """
        users = [main_user] + [None] * (player_amount - 1)

        size = window_size

        window = tk.Tk()
        window.title("Gra na czas")
        window.geometry(f"{size}x{size}")
        window.configure(background="#C3C7F4")
        window.resizable(False, False)


        labels = []

        def refresh_labels():
            for i in range(player_amount):
                text = f"Player {i+1}: {users[i].username if users[i] else 'Guest'}"

                labels[i].config(text=text)


        def login_player(index):
            login = simpledialog.askstring("Login", f"Enter your login for player {index}: ")
            password = simpledialog.askstring("Login", f"Enter your password for player {index}: ")
            if not login or not password:
                return
            from src.auth.Person import Person
            if Person.login(login, password):
                print("Successfully logged in")
                user = Person.get_user_by_login(login)
                if user:
                    users[index] = user
                    refresh_labels()
            else:
                messagebox.showerror("Login failed","Wrong login or password")

        frame = tk.Frame(window, background="#C3C7F4")
        frame.pack(pady=10)
        for i in range(player_amount):
            print(users[i].username if users[i] else 'guest')

            text = f"Player {i + 1}: {users[i].username if users[i] else 'Guest'}"
            label = tk.Label(frame, text=text, font=("Arial", 14), bg="#C3C7F4")
            label.pack(pady=10)

            labels.append(label)
            if i > 0:
                btn_login = tk.Button(frame, text="Login", font=("Arial", 12), bg="#DCD6F7",command=lambda idx=i: login_player(idx))
                btn_login.pack(padx=5, pady=2)

        def play():
            window.destroy()
            MistakeGame.startGame(size,users)

        playButton = tk.Button(window, text="Play", font=("Arial", 16), bg="#B8E1FF", command=play)
        playButton.pack(pady=30)

        window.mainloop()


# AuthorizePlayersWindow.window_setup(800, None, 4)