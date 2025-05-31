from DB.database import SessionLocal
from DB.model.User import User
import bcrypt

from auth.registration import Person


class UserDAO:
    def __init__(self):
        self.session = SessionLocal()


    def create(self, name: str, login: str, password: str) -> bool:
        try:
            hashedPassword = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")

            user = User(username=name, login=login, password=hashedPassword)
            self.session.add(user)
            self.session.commit()

            person = Person(nickname=name, password=hashedPassword)
            return True
        except Exception as e:
            self.session.rollback()
            print(e)
            return False

    def get_user_by_id(self, id: int) -> User:
        return self.session.query(User).filter_by(id=id).first()

    def get_all_users(self) -> list[User]:
        return self.session.query(User).all()

    def delete(self, id: int) -> bool:
        user = self.get_user_by_id(id)
        if user:
            self.session.delete(user)
            self.session.commit()
            return True
        return False

    def close(self):
        self.session.close()

    # def check_password(input_password: str, hashed_password_from_db: str) -> bool:
    #     return bcrypt.checkpw(input_password.encode('utf-8'), hashed_password_from_db.encode('utf-8'))
