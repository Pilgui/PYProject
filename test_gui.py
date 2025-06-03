import tkinter as tk
from game.QuestionOrganizer import QuestionOrganizer

class TimeGame:
    @staticmethod
    def startTimedGame(size, user):
        if user is not None:
            user_name = user.username
        else:
            user_name = "Guest"

        score = 0
        questionNum = 1
        grid_cells = []
        questions = QuestionOrganizer.getQuestions()

        window = tk.Tk()
        window.title("Gra na czas")
        window.geometry(f"{size}x{size}")
        window.configure(bg="#C3C7F4")
        window.resizable(False, False)






        window.mainloop()

TimeGame.startTimedGame(800,None)