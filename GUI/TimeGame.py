import tkinter as tk
score = 0
questionNum = 1
grid_cells = []
questions = [
    ("1. Name of the biggest ocean:", "Pacific"),
    ("2. Capital of France:", "Paris"),
    ("3. Fastest land animal:", "Cheetah"),
    ("4. Largest planet:", "Jupiter"),
    ("5. Color of the sky:", "Blue"),
    ("6. Longest river:", "Nile"),
    ("7. Hardest mineral:", "Diamond"),
    ("8. Largest mammal:", "Bluewhale"),
    ("9. Smallest continent:", "Australia")
]

def startTimedGame(size):

    window = tk.Tk()
    window.title("Gra na czas")
    window.geometry(f"{size}x{size}")
    window.configure(background="#C3C7F4")
    window.resizable(False, False)

    for i in range(24):
        window.grid_columnconfigure(i, weight=1)

    scoreLabel = tk.Label(window,text=f"Score:{score}", font=("Arial", 16), background="#C3C7F4")

    questionCountLabel = tk.Label(window, text=f"Question : {questionNum}", font=("Arial", 16), background="#C3C7F4")

    boardFrame = tk.Frame(window, bg="#C3C7F4")
    boardFrame.grid(row=2, column=0, columnspan=25)



    for i in range(len(questions)):
        q_label = tk.Label(boardFrame, text=questions[i][0], font=("Arial", 12), bg="#C3C7F4", anchor="e", width=25)
        q_label.grid(row=i, column=0, sticky="e", padx=5, pady=2)

        row_cells = []
        for j in range(questions[i][1].__len__()):
            cell = tk.Label(boardFrame, bg="#ffffff", width=2, height=1, relief="solid")
            cell.grid(row=i, column=1 + j, padx=1, pady=1)
            row_cells.append(cell)

        grid_cells.append(row_cells)


    answerEntry = tk.Entry(window, font=("Arial", 14))

    def checkAnswers():
        global score, questionNum
        answer = answerEntry.get().strip().lower()
        correctAnswer = questions[questionNum - 1][1]

        if answer.lower() == correctAnswer.lower():
            score += 1
            scoreLabel.config(text=f"Score:{score}")

            for index,letter in enumerate(answer):
                grid_cells[questionNum - 1][index].configure(text=letter.upper())

            questionNum += 1
            questionCountLabel.config(text=f"Question : {questionNum}")

    answerEntryButton = tk.Button(window, text="Zatwierdź",font=("Arial", 10),command=checkAnswers)

    timerLabel = tk.Label(window, text="Timer: 00:00 ", font=("Arial", 14))

    questionCountLabel.grid(column=0, row=0, pady=15)
    scoreLabel.grid(column=24, row=0, padx=10)

    emptyLabel = tk.Label(text=" ", background="#C3C7F4")
    emptyLabel.grid(column=1,row=19,pady=10)

    answerEntry.grid(row=20, column=0, columnspan=12)
    answerEntryButton.grid(row=21, column=0,columnspan=12, pady=10, padx=10)
    timerLabel.grid(column=12, row=20,columnspan=12)

    window.mainloop()

# startTimedGame()