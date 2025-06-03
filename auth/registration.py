import bcrypt

from DB import DAO
from DB.DAO import userDao


class Person(object):
    """This class is an example of a person object.

    Attributes:
        class variable personDict (dict): Represents registered persons.
        variable nickname (str): The person's nickname.
        variable password (str): The person's password.

    Methods:

    """
    personDict = dict()

    def __init__(self, login, password):
        self.login = login
        self.password = password
        Person.personDict[login] = password

    @staticmethod
    def check_password(input_password: str, hashed_password_from_db: str) -> bool:
        return bcrypt.checkpw(input_password.encode('utf-8'), hashed_password_from_db.encode('utf-8'))

    @staticmethod
    def login(login, password):
        dao = userDao.UserDAO()
        user = dao.get_user_by_login(login)
        return Person.check_password(password, user.password)

    @staticmethod
    def register(name,login, password):
        dao = userDao.UserDAO()
        dao.create(name, login, password)

    @staticmethod
    def get_user_by_login (login):
        dao = userDao.UserDAO()
        user = dao.get_user_by_login(login)
        return user

    @staticmethod
    def getLog():
        keys = Person.personDict.keys()
        result = ""
        for key in keys:
            result += f'{key}\t{Person.personDict.get(key)}\n'
        return result

    def __str__(self):
        return self.login

