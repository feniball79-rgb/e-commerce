from ecommerce.product import Product


class Category:
    category_count = 0
    product_count = 0

    def __init__(
        self,
        name: str | None = None,
        description: str | None = None,
        products: list["Product"] | None = None,
    ) -> None:
        self.name = name
        self.description = description
        self.__products = products if products is not None else []
        Category.category_count += 1
        Category.product_count += len(self.__products)

    # Оптимизированный геттер
    @property
    def products(self) -> str:
        return "".join(f"{prod}\n" for prod in self.__products)

    def add_product(self, new_product: "Product") -> None:
        self.__products.append(new_product)
        Category.product_count += 1

    # Генераторное выражение sum(prod.quantity for ..) —
    # - способ обойти все продукты и сложить их количества
    def __str__(self) -> str:
        total_quantity = sum(prod.quantity for prod in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."


# if __name__ == "__main__":
#
#     # проверка совместной работы классов Product и Category
#     prd = Product("Cubic-Rubik", "brain-braker", 10.23, 5)
#     ddd = Category("Toys", "games", [prd])
#     print(ddd.products)
#
#     # вторая проверка совместной работы классов Product и Category
#     prd2 = Product("Ball", "football", 30.55, 5)
#     ddd2 = Category("Sport", "team games", [prd2])
#     print(ddd2.products)
#
#     print(ddd2.product_count)  # счётчик 1
#     print(ddd2.category_count)  # счётчик 2
#
#     # проверка работы метода add_product
#     prd3 = Product("Triangle", "billiard", 10.44, 4)
#     ddd2.add_product(prd3)
#     print(ddd2.products)
#
#     print(ddd2.product_count)  # счётчики
#     print(ddd2.category_count)
#
#     prd = Product("Stick", "billiard", 299, 1)
#     ddd2.add_product(prd)
#
#     print(ddd)
#     print(ddd2)
#
#     print(ddd.product_count)  # счётчики
#     print(ddd.category_count)
