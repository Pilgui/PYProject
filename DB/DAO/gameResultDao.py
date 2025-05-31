from DB.database import SessionLocal
from DB.model.GameResult import GameResult
from DB.model.User import User

class GameResultDAO:
    def __init__(self):
        self.session = SessionLocal()


    def create(self, userName: str, gameName: str, scoreInTimeGame: int, scoreInGame: int) -> bool:
        try:
            gameResult = GameResult(username=userName, gameName=gameName, scoreInTimeGame=scoreInTimeGame,scoreInGame=scoreInGame)
            self.session.add(gameResult)
            self.session.commit()
            return True
        except Exception as e:
            self.session.rollback()
            print(e)
            return False

    def get_gameResult_by_id(self, id: int) -> User:
        return self.session.query(User).filter_by(id=id).first()

    def get_all_gameResults(self) -> list[User]:
        return self.session.query(User).all()

    def delete(self, id: int) -> bool:
        user = self.get_gameResult_by_id(id)
        if user:
            self.session.delete(user)
            self.session.commit()
            return True
        return False

    def close(self):
        self.session.close()


