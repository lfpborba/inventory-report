from inventory_report.inventory.product import Product


def test_relatorio_produto():
    test_product = Product(
        "18",
        "World of Warcraft",
        "Blizzard",
        "23/11/2004",
        "11/11/2040",
        "23112004",
        "em um SSD",
    )

    report = test_product.__repr__()

    assert report == (
        "O produto World of Warcraft fabricado em 23/11/2004 "
        "por Blizzard com validade até 11/11/2040 "
        "precisa ser armazenado em um SSD."
    )