class Person(object):
    """This class is an example of a person object.

    Attributes:
        class variable personDict (dict): Represents registered persons.
        variable nickname (str): The person's nickname.
        variable password (str): The person's password.

    Methods:

    """
    personDict = dict()

    def __init__(self, nickname, password):
        self.nickname = nickname
        self.password = password
        Person.personDict[nickname] = password

    @staticmethod
    def login(nickname, password):
        return password == Person.personDict.get(nickname)

    @staticmethod
    def getLog():
        keys = Person.personDict.keys()
        result = ""
        for key in keys:
            result += f'{key}\t{Person.personDict.get(key)}\n'
        return result

    def __str__(self):
        return self.nickname

