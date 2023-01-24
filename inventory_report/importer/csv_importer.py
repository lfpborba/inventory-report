from inventory_report.importer.importer import Importer
from csv import DictReader


class CsvImporter(Importer):
    @classmethod
    def import_data(cls, data):
        if data.endswith(".csv"):
            with open(data, encoding="utf-8") as arquivo:
                result = DictReader(arquivo, delimiter=",", quotechar='"')
                return list(result)
        raise ValueError("Arquivo inválido")
