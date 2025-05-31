class Question:
    def __init__(self,id: int,text: str,theme: str,answer: str, level: int):
        self.id = id
        self.text = text
        self.theme = theme
        self.answer = answer
        self.level = level

    def gettext(self):
        return self.text

    def gettheme(self):
        return self.theme

    def getanswer(self):
        return self.answer

    def getlevel(self):
        return self.level