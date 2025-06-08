from src.DB.DAO import gameResultDao

# session = SessionLocal()
# dao = DAO.UserDAO()
# listUser = dao.get_all_users()
# print(listUser)
# user1 = User(id=1, username="user1",login="testLogin", password="123")
# session.add(user1)
# session.commit()
#
# users = session.query(User).all()
# for user in users:
#     print(user.id, user.username, user.login, user.password)
#
# session.close()

dao = gameResultDao.GameResultDAO()
dao.create("Piotr","TimeGame",1,1)

