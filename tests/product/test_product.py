from inventory_report.inventory.product import Product


def test_cria_produto():
    product = Product(
        1,
        "Iphone X",
        "Apple",
        "03/11/17",
        "00/00/00",
        "03112017",
        "Local seco"
        )

    assert product.id == 1
    assert product.nome_do_produto == "Iphone X"
    assert product.nome_da_empresa == "Apple"
    assert product.data_de_fabricacao == "03/11/17"
    assert product.data_de_validade == "00/00/00"
    assert product.numero_de_serie == "03112017"
    assert product.instrucoes_de_armazenamento == "Local seco"
