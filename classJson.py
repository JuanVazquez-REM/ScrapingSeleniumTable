import json

class classJson:

    def readJson(fileName):
        with open(fileName + '.json', 'r') as f:
            data = json.load(f)
        return data