from src.DB.database import SessionLocal
from src.DB.model.User import User
import bcrypt


class UserDAO:
    """
    DAO (Data Access Object) do zarządzania użytkownikami w bazie danych.

    Odpowiada za tworzenie użytkowników z hashowaniem hasła, wyszukiwanie,
    pobieranie listy użytkowników, usuwanie oraz zamykanie sesji.

    :ivar session: Instancja sesji SQLAlchemy dla bieżącego połączenia z bazą danych.
    :type session: sqlalchemy.orm.Session
    """

    def __init__(self):
        """
        Inicjalizuje obiekt DAO i otwiera nową sesję bazy danych.
        """
        self.session = SessionLocal()

    def create(self, name: str, login: str, password: str) -> bool:
        """
        Tworzy nowego użytkownika w bazie danych, hashuje hasło i rejestruje osobę w module auth.

        :param name: Imię użytkownika.
        :type name: str
        :param login: Login użytkownika (musi być unikalny).
        :type login: str
        :param password: Hasło użytkownika (zostanie zaszyfrowane).
        :type password: str
        :return: True, jeśli użytkownik został utworzony pomyślnie; False w przypadku błędu.
        :rtype: bool
        """
        try:
            from src.auth.Person import Person
            hashedPassword = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")

            user = User(username=name, login=login, password=hashedPassword)
            self.session.add(user)
            self.session.commit()

            person = Person(login=login, password=hashedPassword)
            return True
        except Exception as e:
            self.session.rollback()
            print(e)
            return False

    def get_user_by_id(self, id: int) -> User:
        """
        Zwraca użytkownika o podanym identyfikatorze.

        :param id: ID użytkownika.
        :type id: int
        :return: Obiekt użytkownika lub None, jeśli nie znaleziono.
        :rtype: User
        """
        return self.session.query(User).filter_by(id=id).first()

    def get_user_by_login(self, login: str) -> User:
        """
        Zwraca użytkownika na podstawie loginu.

        :param login: Login użytkownika.
        :type login: str
        :return: Obiekt użytkownika lub None, jeśli nie znaleziono.
        :rtype: User
        """
        return self.session.query(User).filter_by(login=login).first()

    def get_all_users(self) -> list[User]:
        """
        Zwraca listę wszystkich użytkowników w bazie danych.

        :return: Lista użytkowników.
        :rtype: list[User]
        """
        return self.session.query(User).all()

    def delete(self, id: int) -> bool:
        """
        Usuwa użytkownika o podanym ID z bazy danych.

        :param id: ID użytkownika do usunięcia.
        :type id: int
        :return: True, jeśli użytkownik został usunięty; False, jeśli nie znaleziono.
        :rtype: bool
        """
        user = self.get_user_by_id(id)
        if user:
            self.session.delete(user)
            self.session.commit()
            return True
        return False

    def close(self):
        """
        Zamyka bieżącą sesję z bazą danych.
        """
        self.session.close()


