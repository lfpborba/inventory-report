# initial commit - plus ultra.
import sys
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.xml_importer import XmlImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.inventory.inventory_refactor import InventoryRefactor


def main():
    if len(sys.argv) < 3:
        return print("Verifique os argumentos", file=sys.stderr)

    inventory_report, file, type = sys.argv

    if file.endswith(".csv"):
        inventory = InventoryRefactor(CsvImporter)
    elif file.endswith(".xml"):
        inventory = InventoryRefactor(XmlImporter)
    elif file.endswith(".json"):
        inventory = InventoryRefactor(JsonImporter)

    data = inventory.import_data(file, type)

    return print(data, end="")
