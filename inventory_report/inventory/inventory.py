import csv
import json
import xml.etree.ElementTree as ET
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    @staticmethod
    def import_data(path, type):
        if "csv" in path:
            return Inventory.inventory_csv(path, type)
        elif "json" in path:
            return Inventory.inventory_json(path, type)
        elif "xml" in path:
            return Inventory.inventory_xml(path, type)
        else:
            raise ValueError("Arquivo inválido")

    @staticmethod
    def inventory_csv(path, type):
        with open(path, encoding="utf-8") as file:
            data = csv.DictReader(file, delimiter=",", quotechar='"')
            if type == "simples":
                return SimpleReport.generate(list(data))
            elif type == "completo":
                return CompleteReport.generate(list(data))
            else:
                raise ValueError("Arquivo inválido")

    @staticmethod
    def inventory_json(path, type):
        with open(path, encoding="utf-8") as file:
            data = json.load(file)
            if type == "simples":
                return SimpleReport.generate(data)
            elif type == "completo":
                return CompleteReport.generate(data)
            else:
                raise ValueError("Arquivo inválido")

    @staticmethod
    def inventory_xml(path, type):
        with open(path, "r", encoding="utf-8") as file:
            data = list()
            tree = ET.parse(file)
            root = tree.getroot()
            for record in root:
                product = {element.tag: element.text for element in record}
                data.append(product)
            if type == "simples":
                return SimpleReport.generate(data)
            elif type == "completo":
                return CompleteReport.generate(data)
            else:
                raise ValueError("Arquivo inválido")