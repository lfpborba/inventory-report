from datetime import date
from collections import Counter

class SimpleReport:
    def __init__(self):
        pass
    
    @classmethod
    def generate(self, inventory: list):

        production_date = min([item["data_de_fabricacao"] for item in inventory])

        date_now = date.today().strftime("%Y-%m-%d")

        validate = min([item["data_de_validade"] for item in inventory
        if item["data_de_validade"] > date_now])

        more_products, _ = Counter([item["nome_da_empresa"] for item in inventory]).most_common()[0]
        
        return (
            f"Data de fabricação mais antiga: {production_date}\n"
            f"Data de validade mais próxima: {validate}\n"
            f"Empresa com mais produtos: {more_products}"
        )