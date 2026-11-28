import pytest

from ecommerce.product import Product


@pytest.fixture
def product_fixt():
    return Product("Smartphone", "Samsung Galaxy S28", 1000.00, 5)


@pytest.fixture
def product_fixt_2():
    return Product()


@pytest.fixture
def product_fixt_3():
    return Product("otto", "desk", 10999.99, 47)


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


def test_new_product(product_fixt_3):
    """Проверка основной работы метода new_product"""
    assert product_fixt_3.name == "otto"
    assert product_fixt_3.description == "desk"
    assert product_fixt_3.price == 10999.99
    assert product_fixt_3.quantity == 47


def test_price(product_fixt):
    # тест геттера
    assert product_fixt.price == 1000.00
    # тест сеттера
    product_fixt.price = 10
    assert product_fixt.price == 10
    # тест сеттера на ввод отрицательных значений и нуля
    product_fixt.price = 0
    assert product_fixt.price == 10
    product_fixt.price = -5
    assert product_fixt.price == 10


def test_new_product_creates_instance():
    """Класс-метод new_product реально создаёт объект из словаря"""
    data = {"name": "otto", "description": "desk", "price": 10999.99, "quantity": 47}
    p = Product.new_product(data)
    assert p.name == "otto"
    assert p.description == "desk"
    assert p.price == 10999.99
    assert p.quantity == 47
    assert isinstance(p, Product)


def test_product_str(product_fixt_3):
    """__str__ возвращает строку формата задания"""
    assert str(product_fixt_3) == "otto, 10999.99 руб. Остаток: 47 шт."


def test_add_products():
    """__add__ возвращает сумму произведений цены на количество"""
    a = Product("яблоки", "красные", 100.0, 10)
    b = Product("бананы", "жёлтые", 200.0, 2)
    assert a + b == 100 * 10 + 200 * 2  # 1400
