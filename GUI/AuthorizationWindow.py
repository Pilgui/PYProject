import tkinter as tk


from GUI.GameTypeMenuWindow import GameTypeMenuWindow
from auth import registration
from utils.Properties import Properties

class AuthorizationWindow:

    @staticmethod
    def register(window_size):
        size = window_size


        window = tk.Tk()
        window.geometry(f"{size}x{size}")
        window.resizable(False, False)
        window.title("Authorization")
        window.config(bg="#F2DDDC")

        for i in range(6):
            window.grid_columnconfigure(i, weight=1)

        for j in range(7):
            window.grid_rowconfigure(j, weight=1)

        titleLabel = tk.Label(window, text="User Registration", font=("Arial", 18, "bold"), bg="#F2DDDC")
        titleLabel.grid(row=1, column=2, pady=10)

        nameLabel = tk.Label(window, text="Name:", bg="#F2DDDC", font=("Arial", 12))
        nameEntry = tk.Entry(window, font=("Arial", 12))

        nameLabel.grid(row=2, column=1, sticky="e", padx=10, pady=5)
        nameEntry.grid(row=2, column=2, padx=10, pady=5)

        loginLabel = tk.Label(window, text="Login:", bg="#F2DDDC", font=("Arial", 12))
        loginEntry = tk.Entry(window, font=("Arial", 12))

        loginLabel.grid(row=3, column=1, sticky="e", padx=10, pady=5)
        loginEntry.grid(row=3, column=2, padx=10, pady=5)

        passwordLabel = tk.Label(window, text="Password:", bg="#F2DDDC", font=("Arial", 12))
        passwordEntry = tk.Entry(window, show="*", font=("Arial", 12))

        passwordLabel.grid(row=4, column=1, sticky="e", padx=10, pady=5)
        passwordEntry.grid(row=4, column=2, padx=10, pady=5)

        def registerUser():
            registration.Person.register(nameEntry.get(), loginEntry.get(), passwordEntry.get())
            user = registration.Person.get_user_by_login(loginEntry.get())
            window.destroy()
            GameTypeMenuWindow.window_setup(size, user)

        def back():
            window.destroy()
            AuthorizationWindow.windowSetup(size)


        registerButton = tk.Button(window, text="Register",command=registerUser, background="#C3C7F4", width=10, font=("Arial", 16), relief="groove")
        registerButton.grid(row=5, column=2, pady=20)
        backButton = tk.Button(window, text="back", command=back, background="#C3C7F4", width=10, font=("Arial", 16),relief="groove")
        backButton.grid(row=5, column=0, pady=20, columnspan=2)



    @staticmethod
    def login(window_size):
        size = window_size

        window = tk.Tk()
        window.geometry(f"{size}x{size}")
        window.resizable(False, False)
        window.title("Authorization")
        window.config(bg="#F2DDDC")

        for i in range(6):
            window.grid_columnconfigure(i, weight=1)

        for j in range(7):
            window.grid_rowconfigure(j, weight=1)

        titleLabel = tk.Label(window, text="Login", font=("Arial", 18, "bold"), bg="#F2DDDC")
        titleLabel.grid(row=1, column=2, pady=10)

        loginLabel = tk.Label(window, text="Login:", bg="#F2DDDC", font=("Arial", 12))
        loginEntry = tk.Entry(window, font=("Arial", 12))

        loginLabel.grid(row=2, column=1, sticky="e", padx=10, pady=5)
        loginEntry.grid(row=2, column=2, padx=10, pady=5)

        passwordLabel = tk.Label(window, text="Password:", bg="#F2DDDC", font=("Arial", 12))
        passwordEntry = tk.Entry(window, show="*", font=("Arial", 12))

        passwordLabel.grid(row=3, column=1, sticky="e", padx=10, pady=5)
        passwordEntry.grid(row=3, column=2, padx=10, pady=5)


        def loginUser():
            if registration.Person.login(loginEntry.get(), passwordEntry.get()):
                print("Login Successful" , loginEntry.get())
                user = registration.Person.get_user_by_login(loginEntry.get())
                window.destroy()
                GameTypeMenuWindow.window_setup(size, user)
            else:
                print("Login Failed")

        def back():
            window.destroy()
            AuthorizationWindow.windowSetup(size)


        logginButton = tk.Button(window, text="login",command=loginUser, background="#C3C7F4", width=10, font=("Arial", 16), relief="groove")
        logginButton.grid(row=4, column=2, pady=20)
        backButton = tk.Button(window, text="back",command=back, background="#C3C7F4", width=10, font=("Arial", 16), relief="groove")
        backButton.grid(row=4, column=0, pady=20,columnspan=2)




    @staticmethod
    def guest(size):
        GameTypeMenuWindow.window_setup(size, None)

    @staticmethod
    def windowSetup(window_size):
        size = window_size

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
            from GUI.MainMenuWindow import MainMenuWindow
            MainMenuWindow.mainMenu(size)

        registerButton = tk.Button(window, text="Register",command=lambda : (window.destroy(), AuthorizationWindow.register(size)), background="#C3C7F4", width=10, font=("Arial", 16), relief="groove")
        loginButton = tk.Button(window, text="Login",command=lambda : (window.destroy(), AuthorizationWindow.login(size)), background="#C3C7F4", width=10, font=("Arial", 16), relief="groove")
        guestButton = tk.Button(window, text="Guest",command=lambda :(window.destroy(), AuthorizationWindow.guest(size)), background="#C3C7F4", width=10, font=("Arial", 16), relief="groove")
        backButton = tk.Button(window, text="Back",command=back, background="#C3C7F4", width=10, font=("Arial", 16), relief="groove")


        registerButton.grid(row=2, column=2, pady=10)
        loginButton.grid(row=3, column=2, pady=10)
        guestButton.grid(row=4, column=2, pady=10)
        backButton.grid(row=5, column=2, pady=10)

