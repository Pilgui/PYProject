from DB.database import SessionLocal
from DB.model.User import User

class UserDAO:
    def __init__(self):
        self.session = SessionLocal()


    def create(self, id: int, name: str, login: str, password: str) -> bool:
        user = User(id, name, login, password)
        self.session.add(user)
        try:
            self.session.commit()
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
