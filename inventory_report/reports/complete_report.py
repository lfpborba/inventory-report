from .simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):
    @staticmethod
    def generate(report):
        simple_report = SimpleReport.generate(report)
        companies = [company["nome_da_empresa"] for company in report]
        company_counter = Counter(companies).most_common()

        products_by_company = ""
        for (company, quantity) in company_counter:
            products_by_company += f"- {company}: {quantity}\n"

        return (
            f"{simple_report}\n"
            f"Produtos estocados por empresa:\n"
            f"{products_by_company}"
        )