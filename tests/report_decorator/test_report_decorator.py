from inventory_report.reports.colored_report import ColoredReport
from inventory_report.reports.simple_report import SimpleReport


def test_decorar_relatorio():
    mock_list = [
        {
            "id": "1",
            "nome_do_produto": "Urfwick",
            "nome_da_empresa": "Riot Games",
            "data_de_fabricacao": "2017-11-08",
            "data_de_validade": "2025-10-10",
            "numero_de_serie": "08112017",
            "instrucoes_de_armazenamento": "em sua Riot Account",
        },
        {
            "id": "2",
            "nome_do_produto": "Frosted Ezreal",
            "nome_da_empresa": "Riot Games",
            "data_de_fabricacao": "2010-07-19",
            "data_de_validade": "2025-10-10",
            "numero_de_serie": "19072010",
            "instrucoes_de_armazenamento": "em sua Riot Account",
        },
    ]

    colored_simple = ColoredReport(SimpleReport)
    report = colored_simple.generate(mock_list)

    assert report == (
        "\033[32mData de fabricação mais antiga:\033[0m "
        "\033[36m2010-07-19\033[0m\n"
        "\033[32mData de validade mais próxima:\033[0m "
        "\033[36m2025-10-10\033[0m\n"
        "\033[32mEmpresa com mais produtos:\033[0m "
        "\033[31mRiot Games\033[0m"
    )
