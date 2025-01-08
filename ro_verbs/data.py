import json
from const import DATAFILE


class VerbData:
    def __init__(self):
        with open(DATAFILE, 'r', encoding='utf-8') as file:
            self.dat = json.load(file)

    def get_menu(self):
        lst = []
        for item in self.dat:
            lst.append(item["title"])
        return lst

    def get_table(self, selection):
        return self.dat[selection]["table"]

    def get_test(self, selection):
        return self.dat[selection]["test"]

    def get_desc(self, selection):
        return self.dat[selection]["desc"]

    def get_title(self, selection):
        return self.dat[selection]["title"]
