from src.DB.database import SessionLocal
from src.DB.model.GameResult import GameResult
from src.utils import ProjectUtil


class GameResultDAO:
    """
    DAO (Data Access Object) do obsługi wyników gier w bazie danych.

    Umożliwia tworzenie, pobieranie i usuwanie rekordów wyników gry oraz eksport do PDF.

    :ivar session: Obiekt sesji bazy danych SQLAlchemy.
    :type session: Session
    """
    def __init__(self):
        """
        Inicjalizuje obiekt DAO i tworzy nową sesję bazodanową.
        """
        self.session = SessionLocal()

    def create(self, userName: str, gameName: str, scoreInTimeGame: int, scoreInGame: int) -> bool:
        """
        Tworzy nowy rekord wyniku gry i eksportuje go do PDF.

        :param userName: Nazwa użytkownika.
        :type userName: str
        :param gameName: Nazwa gry.
        :type gameName: str
        :param scoreInTimeGame: Wynik w grze na czas.
        :type scoreInTimeGame: int
        :param scoreInGame: Wynik ogólny w grze.
        :type scoreInGame: int
        :return: True, jeśli operacja się powiodła; False w przypadku błędu.
        :rtype: bool
        """
        try:
            gameResult = GameResult(username=userName, gameName=gameName, scoreInTimeGame=scoreInTimeGame,scoreInGame=scoreInGame)
            self.session.add(gameResult)
            self.session.commit()
            ProjectUtil.ProjectUtil.exportPDF()
            return True
        except Exception as e:
            self.session.rollback()
            print(e)
            return False

    def get_gameResult_by_id(self, id: int) -> GameResult:
        """
        Zwraca wynik gry o podanym identyfikatorze.

        :param id: ID rekordu w bazie danych.
        :type id: int
        :return: Obiekt GameResult lub None.
        :rtype: GameResult
        """
        return self.session.query(GameResult).filter_by(id=id).first()

    def get_all_gameResults(self) -> list[GameResult]:
        """
        Zwraca wszystkie wyniki gier zapisane w bazie.

        :return: Lista obiektów GameResult.
        :rtype: list[GameResult]
        """
        return self.session.query(GameResult).all()

    def delete(self, id: int) -> bool:
        """
        Usuwa rekord wyniku gry na podstawie ID.

        :param id: ID rekordu do usunięcia.
        :type id: int
        :return: True, jeśli rekord został usunięty; False, jeśli nie znaleziono.
        :rtype: bool
        """
        gameResult = self.get_gameResult_by_id(id)
        if gameResult:
            self.session.delete(gameResult)
            self.session.commit()
            return True
        return False

    def close(self):
        """
        Zamyka aktywną sesję bazy danych.
        """
        self.session.close()


