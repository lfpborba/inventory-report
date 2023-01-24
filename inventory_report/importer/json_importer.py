from inventory_report.importer.importer import Importer
import json


class JsonImporter(Importer):
    @classmethod
    def import_data(cls, data):
        if data.endswith(".json"):
            with open(data, "r") as result:
                return json.load(result)
        raise ValueError("Arquivo inválido")
