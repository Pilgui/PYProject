class Dimension:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getDimension(self):
        return self.x, self.y

    def __str__(self):
        return str(self.x) + "," + str(self.y)

class GameOptions:
    standardlevel = 1
    standardtheme = "all"
    standardDimension = Dimension(720, 720)

    def __init__(self):
        self.level = self.standardlevel
        self.theme = self.standardtheme
        self.dimension = self.standardDimension

    def __init__(self, gameOptions):
        self.gameOptions = gameOptions

    def __init__(self,level: int,theme: str,dimension: Dimension):
        self.level = level
        self.theme = theme
        self.dimension = dimension

    def setlevel(self,level: int):
        self.level = level

    def settheme(self,theme: str):
        self.theme = theme

    def setdimension(self,dimension: Dimension):
        self.dimension = dimension

    def getlevel(self):
        return self.level

    def gettheme(self):
        return self.theme

    def getdimension(self):
        return self.dimension