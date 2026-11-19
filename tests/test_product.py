import pytest

from ecommerce.product import Product


@pytest.fixture
def product_fixt():
    return Product("Smartphone", "Samsung Galaxy S28", 1000.00, 5)


@pytest.fixture
def product_fixt_2():
    return Product()


def test_prod_init(product_fixt):
    """Проверка инициализации Product"""
    assert product_fixt.name == "Smartphone"
    assert product_fixt.description == "Samsung Galaxy S28"
    assert product_fixt.price == 1000.00
    assert product_fixt.quantity == 5


def test_empty_data(product_fixt_2):
    """Проверка с пустыми значениями в параметрах вызова класса"""
    assert product_fixt_2.name is None
    assert product_fixt_2.description is None
    assert product_fixt_2.price == 0.0
    assert product_fixt_2.quantity == 0
