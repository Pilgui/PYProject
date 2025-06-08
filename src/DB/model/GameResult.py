from sqlalchemy import Column, Integer, String
from src.DB.database import Base

class GameResult(Base):
    """
    Model ORM reprezentujący wynik gry zapisywany w bazie danych.
    """
    __tablename__ = 'GameResult'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    username = Column(String,nullable=False)
    gameName = Column(String,nullable=False)
    scoreInTimeGame = Column(Integer, nullable=False)
    scoreInGame = Column(Integer, nullable=False)

    def __repr__(self):
        """
        Zwraca reprezentację tekstową obiektu `GameResult`.

        :return: Łańcuch zawierający wszystkie dane rekordu, oddzielone przecinkami.
        :rtype: str
        """
        return f"{self.id},{self.username},{self.gameName},{self.scoreInTimeGame},{self.scoreInGame}"



