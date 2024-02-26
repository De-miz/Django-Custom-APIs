import json
import os

class JSONManager:
    # Make sure u load data before writing, we're using an overwrite mechanism

    def __init__(self, filename) -> None:
        self.filename = filename


    def json_writer(self, dict_obj):
        filepath = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'json', self.filename)
        with open(filepath, "w") as writer:
            json.dump(dict_obj, writer)
        

    def json_loader(self):
        filepath = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'json', self.filename)
        with open(filepath, "r") as loader:
            dict_obj = json.load(loader)

        return dict_obj