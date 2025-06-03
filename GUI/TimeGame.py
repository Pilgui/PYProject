import tkinter as tk

from game.QuestionOrganizer import QuestionOrganizer

class TimeGame:
    @staticmethod
    def startTimedGame(size, user):

        if user != None:
            user_name = user.username
        else:
            user_name = "Guest"

        score = 0
        questionNum = 1
        grid_cells = []
        questions = QuestionOrganizer.getQuestions()

        time_left = 3
        timer = None

        window = tk.Tk()
        window.title("Gra na czas")
        window.geometry(f"{size}x{size}")
        window.configure(background="#C3C7F4")
        window.resizable(False, False)

        top_frame = tk.Frame(window, bg="#C3C7F4")
        top_frame.pack(pady=10)

        userNameLabel = tk.Label(top_frame, text=f"User_Name: {user_name}", font=("Arial", 14), bg="#C3C7F4")
        userNameLabel.pack(side="left", padx=20)

        questionLabel = tk.Label(top_frame, text=f"Question: {questionNum}", font=("Arial", 14), bg="#C3C7F4")
        questionLabel.pack(side="left", padx=20)

        scoreLabel = tk.Label(top_frame, text=f"Score: {score}", font=("Arial", 14), bg="#C3C7F4")
        scoreLabel.pack(side="left", padx=20)

        timerLabel = tk.Label(top_frame, text=f"Timer: {time_left}", font=("Arial", 14), bg="#C3C7F4")
        timerLabel.pack(side="left", padx=20)

        board_frame = tk.Frame(window, bg="#C3C7F4")
        board_frame.pack(pady=10)

        for i, (question, correct) in enumerate(questions):
            tk.Label(board_frame, text=f"{question}", font=("Arial", 12), bg="#C3C7F4", anchor="w",
                     justify="left").grid(row=i, column=0, sticky="w", padx=10, pady=2)
            row_cells = []

            for j in range(len(correct)):
                cell = tk.Label(board_frame, width=2, height=1, bg="white", relief="solid", font=("Arial", 10))
                cell.grid(row=i, column=1 + j, padx=1, pady=1)
                row_cells.append(cell)

            grid_cells.append(row_cells)

        bottom_frame = tk.Frame(window, bg="#C3C7F4")
        bottom_frame.pack(pady=10)

        answerEntry = tk.Entry(bottom_frame, font=("Arial", 14), width=25)
        answerEntry.grid(row=0, column=0, padx=10)


        def showAnswer():
            nonlocal questionNum
            correctAnswer = questions[questionNum-1][1]
            for index,letter in enumerate(correctAnswer):
                grid_cells[questionNum-1][index].config(text=letter.upper())

        def showGameEnd():
            from DB.DAO import gameResultDao
            from GUI.MainMenuWindow import MainMenuWindow
            dao = gameResultDao.GameResultDAO().create(user_name,"Time Game", score, 0)

            for widget in window.winfo_children():
                widget.destroy()

            gameEnded = tk.Label(window, text="Game Ended!", font=("Arial", 32, "bold"), bg="#C3C7F4")
            gameEnded.pack(pady=50)

            finalScore = tk.Label(window, text=f"Your score: {score}", font=("Arial", 24), bg="#C3C7F4")
            finalScore.pack(pady=20)

            retryButton = tk.Button(window, text="Retry", command=lambda:(window.destroy(),TimeGame.startTimedGame(size,user)), font=("Arial", 14), bg="#DCD6F7")
            retryButton.pack(pady=20)

            exitButton = tk.Button(window, text="Exit", command=lambda :(window.destroy(),MainMenuWindow.mainMenu(size)), font=("Arial", 14), bg="#DCD6F7")
            exitButton.pack(pady=20)
        def nextQuestion():
            nonlocal questionNum, time_left, timer
            questionNum += 1
            if questionNum > len(questions):
                showGameEnd()
                return
            questionLabel.config(text=f"Question: {questionNum}")
            time_left = 3
            updateTimer()

        def updateTimer():
            nonlocal time_left, timer
            timerLabel.config(text=f"Timer: {time_left}")
            if time_left > 0:
                time_left -= 1
                timer = window.after(1000, updateTimer)
            else:
                showAnswer()
                nextQuestion()

        def checkAnswers():
            nonlocal score, questionNum
            answer = answerEntry.get().strip()

            if questionNum > len(questions):
                return

            correctAnswer = questions[questionNum - 1][1]
            if answer.lower() == correctAnswer.lower():
                score += 1
                scoreLabel.config(text=f"Score: {score}")
                for index, letter in enumerate(answer):
                    grid_cells[questionNum - 1][index].config(text=letter.upper())
            else: showAnswer()

            if timer:
                window.after_cancel(timer)

            answerEntry.delete(0, tk.END)
            nextQuestion()



        confirm_button = tk.Button(bottom_frame, text="Enter", command=checkAnswers, font=("Arial", 12),bg="#DCD6F7")
        confirm_button.grid(row=0, column=1, padx=10)

        updateTimer()

        window.mainloop()

# TimeGame.startTimedGame(1000,None)