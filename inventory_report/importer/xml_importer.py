from inventory_report.importer.importer import Importer
import xml.etree.ElementTree as ET


class XmlImporter(Importer):
    @classmethod
    def import_data(cls, data):
        if data.endswith(".xml"):
            with open(data, "r", encoding="utf-8") as file:
                products_list = list()
                tree = ET.parse(file)
                root = tree.getroot()
                for record in root:
                    product = {element.tag: element.text for element in record}
                    products_list.append(product)
                return products_list
        raise ValueError("Arquivo inválido")