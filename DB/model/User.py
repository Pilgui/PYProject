
# id name login password

from sqlalchemy import Column, Integer, String
from DB.database import Base

class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String,nullable=False)
    login = Column(String,nullable=False, unique=True)
    password = Column(String,nullable=False)

    def __repr__(self):
        return f"<User(id={self.id}, username={self.username}, login={self.login})>"