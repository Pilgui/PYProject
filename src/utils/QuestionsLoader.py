import json
import os

from src.utils.Question import Question


class QuestionsLoader(object):
    """
    Wczytuje pytania z pliku JSON i umożliwia ich filtrowanie według poziomu i tematu.

    :param filePath: Nazwa pliku JSON zawierającego pytania (wewnątrz katalogu 'data').
    :type filePath: str

    :ivar filePath: Pełna ścieżka do pliku z pytaniami.
    :type filePath: str
    :ivar questions: Lista załadowanych obiektów typu Question.
    :type questions: list[Question]
    """
    def __init__(self, filePath: str):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        data_dir = os.path.join(base_dir, 'data')

        self.filePath = os.path.join(data_dir, filePath)
        self.questions = self.loadFile()

    def loadFile(self) -> list[Question]:
        """
        Ładuje dane z pliku JSON i przekształca je w listę obiektów typu Question.

        :return: Lista pytań.
        :rtype: list[Question]
        """
        with open(self.filePath, "r") as file:
            data = json.load(file)
        return [Question(**i) for i in data]

    def get_all_questions(self) -> list[Question]:
        """
        Zwraca wszystkie załadowane pytania.

        :return: Lista wszystkich pytań.
        :rtype: list[Question]
        """
        return self.questions

    def get_by_level_and_theme(self, level: int, theme: str) -> list[Question]:
        """
        Zwraca listę pytań o podanym poziomie trudności i temacie.

        :param level: Poziom trudności pytania.
        :type level: int
        :param theme: Temat pytania.
        :type theme: str
        :return: Lista dopasowanych pytań.
        :rtype: list[Question]
        """
        return [i for i in self.questions if i.level == level and i.theme == theme]