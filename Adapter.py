from analyze_machine import DataAnalyzeMachine
import json
import xmltodict


class XmlAdapter:
    def __init__(self, xml_file):
        with open(xml_file, 'r') as f:
            self.xml_data = xmltodict.parse(f.read())

    def converted_data(self):
        print('converting xml to json ...')
        return json.dumps(self.xml_data)


if __name__ == '__main__':
    file = XmlAdapter('sample.xml')
    data = file.converted_data()
    machine = DataAnalyzeMachine(data)
    machine.analyze()

