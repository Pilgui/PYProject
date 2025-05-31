from DB.database import engine, Base
from DB.model.User import User

def init():
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    init()
