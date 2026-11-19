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
    assert category_fxt.name == "Смартфоны"
    assert (
        category_fxt.description
        == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    )
    assert len(category_fxt.products) == 3
    assert category_fxt.category_count == 1

def test_category_init(category_fxt):
    cat_before, prod_before = category_fxt.counters_before
    assert Category.category_count == cat_before + 1
    assert Category.product_count == prod_before + 3
    assert category_fxt.name == "Смартфоны"
    assert len(category_fxt.products) == 3
