from src.utils.Properties import Properties
from src.utils.Question import Question
from src.utils.QuestionsLoader import QuestionsLoader


class QuestionOrganizer:
    """
    Klasa pomocnicza zawierająca metody statyczne do pobierania pytań do gry.

    Zawiera narzędzia do:
    - pobrania pytań
    """
    @staticmethod
    def getQuestions():
        """
        Wczytuje wszystkie pytania z pliku `questions.json` odpowiadające ustawieniam.

        :return: Lista pytań wczytana z pliku.
        :rtype: list[Question]
        """
        properties = Properties()
        level = properties.get("level")
        theme = properties.get("theme")

        loader = QuestionsLoader("questions.json")
        questionsObjects = loader.get_by_level_and_theme(level, theme)

        questions = []
        for q in questionsObjects:
            questions.append((q.text, q.answer))

        return questions



