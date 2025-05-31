from utils.Properties import Properties
from utils.Question import Question
from utils.QuestionsLoader import QuestionsLoader


class QuestionOrganizer:
    @staticmethod
    def getQuestions():
        properties = Properties()
        level = properties.get("level")
        theme = properties.get("theme")

        loader = QuestionsLoader("questions.json")
        questionsObjects = loader.get_by_level_and_theme(level, theme)

        questions = []
        for q in questionsObjects:
            questions.append((f"{q.id}. {q.text}", q.answer))

        return questions



