import tkinter as tk

from game.QuestionOrganizer import QuestionOrganizer

class MistakeGame:
    @staticmethod
    def startGame(size, users):
        usernames = [user.username if user is not None else "Guest" for user in users]
        scores = [0] * len(usernames)
        active_users = [True] * len(usernames)

        questionNum = 1
        grid_cells = []
        questions = QuestionOrganizer.getQuestions()
        active_user_index = 0

        eliminated_players = []

        window = tk.Tk()
        window.title("Gra na czas")
        window.geometry(f"{size}x{size}")
        window.configure(background="#C3C7F4")
        window.resizable(False, False)

        top_frame = tk.Frame(window, bg="#C3C7F4")
        top_frame.pack(pady=10)

        activeUserLabel = tk.Label(top_frame, text=f"Player '{active_user_index+1}' is moving", font=("Arial", 14), bg="#C3C7F4")
        activeUserLabel.pack(side="left", padx=20)

        questionLabel = tk.Label(top_frame, text=f"Question: {questionNum}", font=("Arial", 14), bg="#C3C7F4")
        questionLabel.pack(side="left", padx=20)

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


        pre_bottom_frame = tk.Frame(window, bg="#C3C7F4")
        pre_bottom_frame.pack(pady=10)

        user_labels = []
        for index, name in enumerate(usernames):
            lbl = tk.Label(pre_bottom_frame, text=f"Player{index+1} : {name} : {scores[index]}", font=("Arial", 14), bg="#C3C7F4")
            lbl.pack(side="left", padx=20)
            user_labels.append(lbl)


        bottom_frame = tk.Frame(window, bg="#C3C7F4")
        bottom_frame.pack(pady=10)

        status_label = tk.Label(window, text="", font=("Arial", 14), bg="#C3C7F4", fg="red")
        status_label.pack(pady=5)

        answerEntry = tk.Entry(bottom_frame, font=("Arial", 14), width=25)
        answerEntry.grid(row=1, column=0, padx=10)


        def showAnswer():
            nonlocal questionNum
            correctAnswer = questions[questionNum-1][1]
            for index,letter in enumerate(correctAnswer):
                grid_cells[questionNum-1][index].config(text=letter.upper())

        def showGameEnd():
            from DB.DAO import gameResultDao
            from GUI.MainMenuWindow import MainMenuWindow
            # dao = gameResultDao.GameResultDAO().create(user_name1,"Time Game", score, 0)

            for widget in window.winfo_children():
                widget.destroy()

            gameEnded = tk.Label(window, text="Game Ended!", font=("Arial", 32, "bold"), bg="#C3C7F4")
            gameEnded.pack(pady=50)

            retryButton = tk.Button(window, text="Retry", command=lambda:(window.destroy(),MistakeGame.startGame(size, users)), font=("Arial", 14), bg="#DCD6F7")
            retryButton.pack(pady=20)

            exitButton = tk.Button(window, text="Exit", command=lambda :(window.destroy(),MainMenuWindow.mainMenu(size)), font=("Arial", 14), bg="#DCD6F7")
            exitButton.pack(pady=20)

        def nextActiveUser():
            nonlocal active_user_index
            for _ in range(len(users)):
                active_user_index = (active_user_index + 1) % len(users)
                if active_users[active_user_index]:
                    activeUserLabel.config(text=f"Player '{active_user_index + 1}' is moving")
                    return
            showGameEnd()

        def nextQuestion():
            nonlocal questionNum
            questionNum += 1
            if questionNum > len(questions):
                showGameEnd()
                return
            questionLabel.config(text=f"Question: {questionNum}")

        def updateUserLabels():
            for index, label in enumerate(user_labels):
                label.config(text=f"Player{index+1} : {usernames[index]} : {scores[index]}")


        def checkAnswers():
            nonlocal active_user_index, questionNum
            answer = answerEntry.get().strip()

            if questionNum > len(questions):
                return

            correctAnswer = questions[questionNum - 1][1]

            if answer.lower() == correctAnswer.lower():
                scores[active_user_index] += 1
                for index, letter in enumerate(answer):
                    grid_cells[questionNum - 1][index].config(text=letter.upper())
                updateUserLabels()
                answerEntry.delete(0, tk.END)
                nextActiveUser()
                nextQuestion()
            else:
                active_users[active_user_index] = False
                eliminated_players.append(active_user_index + 1)
                text = " ".join([f"Player  {i} eliminated\n" for i in eliminated_players])
                status_label.config(text=text)
                showAnswer()
                updateUserLabels()
                nextActiveUser()
                nextQuestion()


        confirm_button = tk.Button(bottom_frame, text="Enter", command=checkAnswers, font=("Arial", 12),bg="#DCD6F7")
        confirm_button.grid(row=1, column=1, padx=10)


        window.mainloop()


MistakeGame.startGame(800,[None,None,None,None])