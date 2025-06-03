

# userName gameName scoreinTimeGame scoreInGame

from sqlalchemy import Column, Integer, String
from DB.database import Base

class GameResult(Base):
    __tablename__ = 'GameResult'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    username = Column(String,nullable=False)
    gameName = Column(String,nullable=False)
    scoreInTimeGame = Column(Integer, nullable=False)
    scoreInGame = Column(Integer, nullable=False)


    def __repr__(self):
        return f"{self.id},{self.username},{self.gameName},{self.scoreInTimeGame},{self.scoreInGame}"



