import json
import os

class Properties:
    """
    Obsługuje zapis i odczyt ustawień gry z pliku JSON.

    :param filename: Nazwa pliku właściwości.
    :type filename: str
    """
    def __init__(self, filename='properties.json'):
        """Inicjalizuje obiekt właściwości, tworzy plik jeśli nie istnieje.

        :param filename: Nazwa pliku z danymi.
        :type filename: str
        """
        base_dir = os.path.dirname(os.path.abspath(__file__))
        data_dir = os.path.join(base_dir, 'data')

        self.filename = os.path.join(data_dir, filename)
        self.data = {
            "window-size": 500,
            "level": 1,
            "theme": "Geography"
        }
        print('start')
        self.load()

    def load(self):
        """
        Ładuje dane z pliku JSON. Tworzy nowy plik, jeśli nie istnieje.
        """
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                self.data.update(json.load(file))
        else:
            self.save()

    def save(self):
        """
        Zapisuje dane do pliku JSON.
        """
        with open(self.filename, 'w') as file:
            json.dump(self.data, file, indent=4)

    def get(self, key):
        """
        Zwraca wartość dla podanego klucza.

        :param key: Poziom do pobrania.
        :type key: str

        :return: wartość dla klucza.
        :rtype: str
        """
        return self.data.get(key)

    def set(self, key, value):
        """
        Ustawia wartość dla danego klucza i zapisuje zmiany.

        :param key: Klucz do zapisu.
        :type key: str
        :param value: Wartość do zapisania.
        :type value: Any
        """
        self.data[key] = value
        self.save()