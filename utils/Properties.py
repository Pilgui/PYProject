import json
import os

class Properties:
    def __init__(self, filename='properties.json'):
        base_dir = os.path.dirname(os.path.abspath(__file__))

        self.filename = os.path.join(base_dir, filename)
        self.data = {
            "window-size": 500
        }
        print('start')
        self.load()

    def load(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                self.data.update(json.load(file))
        else:
            self.save()

    def save(self):
        with open(self.filename, 'w') as file:
            json.dump(self.data, file, indent=4)

    def get(self, key):
        return self.data.get(key)

    def set(self, key, value):
        self.data[key] = value
        self.save()