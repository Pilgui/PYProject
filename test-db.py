from DB.database import SessionLocal
from DB.model.User import User

session = SessionLocal()

user1 = User(id=1, username="user1",login="testLogin", password="123")
session.add(user1)
session.commit()

users = session.query(User).all()
for user in users:
    print(user.id, user.username, user.login, user.password)

session.close()