class Question:
    """
    Reprezentuje pojedyncze pytanie w Krzyżówce.

    :param id: Unikalny identyfikator pytania.
    :type id: int
    :param text: Treść pytania.
    :type text: str
    :param theme: Temat pytania (np. 'Historia', 'Geografia').
    :type theme: str
    :param answer: Poprawna odpowiedź na pytanie.
    :type answer: str
    :param level: Poziom trudności pytania.
    :type level: int
    """
    def __init__(self, id: int, text: str, theme: str, answer: str, level: int):
        self.id = id
        self.text = text
        self.theme = theme
        self.answer = answer
        self.level = level

    def gettext(self):
        """
        Zwraca treść pytania.

        :return: Tekst pytania.
        :rtype: str
        """
        return self.text

    def gettheme(self):
        """
        Zwraca temat pytania.

        :return: Temat pytania.
        :rtype: str
        """
        return self.theme

    def getanswer(self):
        """
        Zwraca poprawną odpowiedź.

        :return: Odpowiedź.
        :rtype: str
        """
        return self.answer

    def getlevel(self):
        """
        Zwraca poziom trudności pytania.

        :return: Poziom trudności.
        :rtype: int
        """
        return self.level