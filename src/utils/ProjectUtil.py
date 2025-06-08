from json import load
from json import dump
from fpdf import FPDF

from src.utils.Properties import Properties
from src.utils.QuestionsLoader import QuestionsLoader


class ProjectUtil:
    """
    Klasa pomocnicza zawierająca metody statyczne do obsługi pytań, opcji gry oraz eksportu wyników do PDF.

    Zawiera narzędzia do:
    - wczytywania pytań,
    - odczytu i zapisu ustawień,
    - zapisu nowych pytań,
    - eksportu wyników do pliku PDF.
    """

    @staticmethod
    def getQuestions():
        """
        Wczytuje wszystkie pytania z pliku `questions.json`.

        :return: Lista pytań wczytana z pliku.
        :rtype: list[Question]
        """
        questionLoader = QuestionsLoader("questions.json")
        questions = questionLoader.get_all_questions()
        return questions

    @staticmethod
    def getSavedOptions():
        """
        Wczytuje zapisane ustawienia z pliku `properties.json`.

        :return: Słownik zawierający okno gry, poziom i motyw.
        :rtype: dict[str, Any]
        """
        properties = Properties()
        options = {
            "window-size": properties.get(key="window-size"),
            "level": properties.get(key="level"),
            "theme": properties.get(key="theme")
        }
        return options

    @staticmethod
    def saveOptions(optionsToSave):
        """
        Zapisuje przekazane opcje do pliku `options.json`.

        :param optionsToSave: Słownik z opcjami do zapisania.
        :type optionsToSave: dict
        """
        with open('options.json', 'w') as options:
            dump(optionsToSave, options, indent=4)

    @staticmethod
    def saveQuestion(question):
        """
        Zapisuje pytanie do pliku `questions.json`.

        :param question: Obiekt pytania do zapisania. Wymaga, by `question.id` był unikalny i zapisywalny jako klucz JSON.
        :type question: Question
        """
        with open('questions.json', 'r') as questions:
            data = load(questions)
        data[question.id] = question
        with open('questions.json', 'w') as questions:
            dump(data, questions, indent=4)

    @staticmethod
    def exportPDF():
        """
        Eksportuje wyniki graczy z bazy danych do pliku PDF o nazwie `Highscore.pdf`.

        Dane pobierane są za pomocą `GameResultDAO`, a następnie renderowane jako tabela w pliku PDF.
        """
        from src.DB.DAO import gameResultDao
        dao = gameResultDao.GameResultDAO()

        results = []
        resultsArray = dao.get_all_gameResults()
        for result in resultsArray:
            strResult = str(result)
            results.append(strResult)

        cellW = 200
        pdf = FPDF()
        col = 3
        pdf.add_page()
        pdf.set_font("Arial", size=25)
        pdf.cell(cellW, 25, txt="Highscore", ln=1, align="C")
        line_height = 15

        pdf.set_font("Arial", size=line_height)
        headers = ["Player", "Game name", "Score in Game"]
        for i in range(col):
            pdf.cell(cellW/3, line_height, headers[i], border=1, align="L")
        pdf.ln(line_height)

        for row in results:
            values = row.split(",")
            i = 0
            k = False
            for value in values:
                if i > 0:
                    if i == 1:
                        pdf.cell(cellW/3, line_height, value, border=1, align="L")
                    if i == 2 and not k:
                        if value != "Time Game":
                            k = True
                        pdf.cell(cellW/3, line_height, value, border=1, align="L")
                    if i == 3 and not k:
                        pdf.cell(cellW/3, line_height, value, border=1, align="R")
                        k = False
                    if i == 4 and k:
                        pdf.cell(cellW/3, line_height, value, border=1, align="R")
                        k = False
                if i == 4:
                    i = 0
                    pdf.ln(line_height)
                else:
                    i += 1

        pdf.output("Highscore.pdf")