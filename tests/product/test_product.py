from inventory_report.inventory.product import Product


def test_cria_produto():
    product = Product(
        1,
        "Apple",
        "Iphone X",
        "03/11/17",
        "00/00/00",
        "03112017",
        "Local seco",
    )

assert product_test.id == 1
assert product_test.nome_da_empresa == "Apple"
assert product_test.nome_do_produto == "Iphone X"
assert product_test.data_de_fabricacao == "03/11/17"
assert product_test.data_de_validade == "00/00/00"
assert product_test.numero_de_serie == "03112017"
assert product_test.instrucoes_de_armazenamento == "Local seco"