import json

class classJson:

    def readJson(nameFile):
        with open(nameFile + '.json', 'r') as f:
            data = json.load(f)
        return data