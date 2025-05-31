from json import load
from json import dump

from utils.QuestionsLoader import QuestionsLoader


class ProjectUtil:

    @staticmethod
    def getQuestions():
        questionLoader = QuestionsLoader("questions.json")
        questions = questionLoader.get_all_questions()
        return questions

    @staticmethod
    def getSavedOptions():
        # nie jestem pewny wyniku, jeśli niema pliku...
        with open('options.json', 'r') as options:
            return load(options)

    @staticmethod
    def saveOptions(optionsToSave):
        with open('options.json', 'w') as options:
            dump(optionsToSave, options, indent=4)

    @staticmethod
    def saveQuestion(question):
        # może być do poprawy, bo może nie istnieć plik
        with open('questions.json', 'r') as questions:
            data = load(questions)
        data[question.id] = question
        with open('questions.json', 'w') as questions:
            dump(data, questions, indent=4)
