
# id name login password

from sqlalchemy import Column, Integer, String
from src.DB.database import Base

class User(Base):
    """
        Model ORM reprezentujący użytkowników gry zapisywanych w bazie danych.
        """
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    username = Column(String,nullable=False)
    login = Column(String,nullable=False, unique=True)
    password = Column(String,nullable=False)

    def __repr__(self):
        """
        Zwraca reprezentację tekstową obiektu `user`.

        :return: Łańcuch zawierający wszystkie dane rekordu, oddzielone przecinkami.
        :rtype: str
        """
        return f"<User(id={self.id}, username={self.username}, login={self.login}, password={self.password})>"