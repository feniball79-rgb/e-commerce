from typing import Any


class Product:
    def __init__(
        self,
        name: str | None = None,
        description: str | None = None,
        price: float = 0.0,
        quantity: int = 0,
    ) -> None:
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, product_data: dict[str, Any]) -> "Product":
        return cls(
            name=product_data.get("name"),
            description=product_data.get("description"),
            price=product_data.get("price", 0.0),
            quantity=product_data.get("quantity", 0),
        )

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, new_price: float) -> None:
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = new_price


# if __name__ == "__main__":
#
#     aaa = {'name':'otto', 'description':'burger', 'price':0.0, 'quantity':1}
#     fff = Product.new_product(aaa)
#
#     print()
#     print(fff)
#     print(fff.name)
#     print(fff.description)
#     print(fff.price)
#     print(fff.quantity)
# ## ********************************************************
#
#     # проверка @price.setter
#     print()
#     fff.price = 55.83
#     print(fff.price)
#     fff.quantity = 8
#     print(fff.quantity)
