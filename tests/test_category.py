import pytest

from ecommerce.category import Category
from ecommerce.product import Product

product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)


@pytest.fixture
def category_fxt():
    counters_before = (Category.category_count, Category.product_count)
    category = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3],
    )
    category.counters_before = counters_before
    return category


def test_category_init(category_fxt):
    cat_before, prod_before = category_fxt.counters_before
    assert Category.category_count == cat_before + 1
    assert Category.product_count == prod_before + 3
    assert category_fxt.name == "Смартфоны"

    # splitlines() возвращает список строк — по нему видно и количество товаров,
    # и формат каждого. Проверка in ловит точный шаблон «Название, цена руб. Остаток: N шт.
    products_str = category_fxt.products
    assert len(products_str.splitlines()) == 3  # три товара = три строки
    assert "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт." in products_str
    assert products_str.endswith("\n")  # шаблон требует \n в конце


def test_price_setter(capsys):
    """capsys — штатная фикстура pytest для перехвата print-вывода:"""
    p = Product("TV", "телевизор", 50000.0, 2)
    p.price = -100
    captured = capsys.readouterr()
    assert captured.out == "Цена не должна быть нулевая или отрицательная\n"
    assert p.price == 50000.0  # цена НЕ изменилась — главное требование
    p.price = 60000.0
    assert p.price == 60000.0


def test_add_product(category_fxt):
    """add_product добавляет товар и увеличивает счётчик продуктов"""
    cat_before, prod_before = category_fxt.counters_before
    new_product = Product("Наушники", "беспроводные", 15000.0, 7)

    category_fxt.add_product(new_product)

    assert Category.product_count == prod_before + 4  # было 3, стало 4
    assert "Наушники, 15000.0 руб. Остаток: 7 шт." in category_fxt.products


def test_category_str(category_fxt):
    """__str__ показывает сумму количеств всех товаров категории"""
    assert str(category_fxt) == "Смартфоны, количество продуктов: 27 шт."


def test_products_getter_uses_product_str(category_fxt):
    lines = category_fxt.products.strip().split("\n")
    assert lines[0] == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."
