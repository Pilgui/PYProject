from DB.database import SessionLocal
from DB.model.GameResult import GameResult


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

    def get_gameResult_by_id(self, id: int) -> GameResult:
        return self.session.query(GameResult).filter_by(id=id).first()

    def get_all_gameResults(self) -> list[GameResult]:
        return self.session.query(GameResult).all()

    def delete(self, id: int) -> bool:
        gameResult = self.get_gameResult_by_id(id)
        if gameResult:
            self.session.delete(gameResult)
            self.session.commit()
            return True
        return False

    def close(self):
        self.session.close()


