import tkinter as tk

from sqlalchemy.testing.provision import register

import GUI.startMenu as startMenu
from utils.Properties import Properties


class AuthorizationWindow:

    @staticmethod
    def register():
        properties = Properties()
        size = properties.get("window-size")

        window = tk.Tk()
        window.geometry(f"{size}x{size}")
        window.resizable(False, False)
        window.title("Authorization")
        window.config(bg="#F2DDDC")

        for i in range(5):
            window.grid_columnconfigure(i, weight=1)

    @staticmethod
    def login():
        properties = Properties()
        size = properties.get("window-size")

        window = tk.Tk()
        window.geometry(f"{size}x{size}")
        window.resizable(False, False)
        window.title("Authorization")
        window.config(bg="#F2DDDC")

        for i in range(5):
            window.grid_columnconfigure(i, weight=1)


    @staticmethod
    def guest():
        pass

    @staticmethod
    def windowSetup():
        properties = Properties()
        size = properties.get("window-size")

        window = tk.Tk()
        window.geometry(f"{size}x{size}")
        window.resizable(False, False)
        window.title("Authorization")
        window.config(bg="#F2DDDC")

        for i in range(5):
            window.grid_columnconfigure(i, weight=1)

        for j in range(7):
            window.grid_rowconfigure(j, weight=1)


        def back():
            window.destroy()
            startMenu.mainMenu(size)

        registerButton = tk.Button(window, text="Register",command=AuthorizationWindow.register, background="#C3C7F4", width=10, font=("Arial", 16), relief="groove")
        loginButton = tk.Button(window, text="Login",command=AuthorizationWindow.login, background="#C3C7F4", width=10, font=("Arial", 16), relief="groove")
        guestButton = tk.Button(window, text="Guest",command=AuthorizationWindow.guest, background="#C3C7F4", width=10, font=("Arial", 16), relief="groove")
        backButton = tk.Button(window, text="Back",command=back, background="#C3C7F4", width=10, font=("Arial", 16), relief="groove")


        registerButton.grid(row=2, column=2, pady=10)
        loginButton.grid(row=3, column=2, pady=10)
        guestButton.grid(row=4, column=2, pady=10)
        backButton.grid(row=5, column=2, pady=10)

