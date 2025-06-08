import bcrypt
from src.DB.DAO import userDao


class Person(object):
    """
    Klasa reprezentująca użytkownika w kontekście logowania i rejestracji.

    Obsługuje:
    - rejestrację użytkowników,
    - logowanie z weryfikacją hasła,
    - dostęp do użytkownika po loginie,
    - wypisywanie tymczasowego słownika loginów i haseł.
    """

    personDict = dict()

    def __init__(self, login, password):
        """
        Inicjalizuje obiekt użytkownika i zapisuje dane do tymczasowego słownika.

        :param login: Login użytkownika.
        :type login: str
        :param password: Hasło użytkownika.
        :type password: str
        """
        self.login = login
        self.password = password
        Person.personDict[login] = password

    @staticmethod
    def check_password(input_password: str, hashed_password_from_db: str) -> bool:
        """
        Sprawdza, czy podane hasło pasuje do hasha z bazy danych.

        :param input_password: Wprowadzone przez użytkownika hasło.
        :type input_password: str
        :param hashed_password_from_db: Zaszyfrowane hasło z bazy danych.
        :type hashed_password_from_db: str
        :return: True, jeśli hasło jest poprawne; False w przeciwnym razie.
        :rtype: bool
        """
        return bcrypt.checkpw(input_password.encode('utf-8'), hashed_password_from_db.encode('utf-8'))

    @staticmethod
    def login(login, password):
        """
        Próbuje zalogować użytkownika przy użyciu loginu i hasła.

        :param login: Login użytkownika.
        :type login: str
        :param password: Hasło użytkownika.
        :type password: str
        :return: True, jeśli logowanie zakończone sukcesem; False w przeciwnym razie.
        :rtype: bool
        """
        dao = userDao.UserDAO()
        hashed_password = ""
        try:
            user = dao.get_user_by_login(login)
            hashed_password = user.password
        except:
            return False
        return Person.check_password(password, hashed_password)

    @staticmethod
    def register(name, login, password):
        """
        Rejestruje nowego użytkownika za pomocą DAO.

        :param name: Imię użytkownika.
        :type name: str
        :param login: Login użytkownika.
        :type login: str
        :param password: Hasło użytkownika.
        :type password: str
        """
        dao = userDao.UserDAO()
        dao.create(name, login, password)

    @staticmethod
    def get_user_by_login(login):
        """
        Pobiera użytkownika z bazy danych po loginie.

        :param login: Login użytkownika.
        :type login: str
        :return: Obiekt użytkownika lub None.
        :rtype: User
        """
        dao = userDao.UserDAO()
        user = dao.get_user_by_login(login)
        return user

    @staticmethod
    def getLog():
        """
        Zwraca listę tymczasowych loginów i haseł w postaci tekstowej (np. do debugowania).

        :return: Tekst z loginami i hasłami.
        :rtype: str
        """
        keys = Person.personDict.keys()
        result = ""
        for key in keys:
            result += f'{key}\t{Person.personDict.get(key)}\n'
        return result

    def __str__(self):
        """
        Reprezentacja tekstowa użytkownika.

        :return: Login użytkownika.
        :rtype: str
        """
        return self.login

