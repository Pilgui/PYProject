from src.DB.database import engine, Base


def init():
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    init()
