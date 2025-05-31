import json
import os

from utils.Question import Question


class QuestionsLoader(object):
    def __init__(self, filePath: str):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        data_dir = os.path.join(base_dir, 'data')

        self.filePath = os.path.join(data_dir, filePath)
        self.questions = self.loadFile()

    def loadFile(self) -> list[Question]:
        with open(self.filePath, "r") as file:
            data = json.load(file)
        return [Question(**i) for i in data]

    def get_all_questions(self) -> list[Question]:
        return self.questions

    def get_by_level_and_theme(self, level: int, theme: str) -> list[Question]:
        return [i for i in self.questions if i.level == level and i.theme == theme]