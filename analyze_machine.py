import json


class DataAnalyzeMachine:
    def __init__(self, json_data):
        self.json_data = json_data

    def analyze(self):
        print('analyzing ...')
        print(self.json_data)


def json_loader(json_file):
    with open(json_file, 'r') as f:
        data = json.load(f)
        return data


if __name__ == '__main__':
    data = json_loader('sample.json')
    machine = DataAnalyzeMachine(data)
    machine.analyze()
