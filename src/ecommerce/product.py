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

    def __str__(self) -> str:
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: "Product") -> float | Any:
        sum_price = self.price * self.quantity
        sum_quant = other.price * other.quantity
        res = sum_price + sum_quant
        return res


# if __name__ == "__main__":
#
#     aaa = {"name": "otto", "description": "burger", "price": 10, "quantity": 11}
#     bbb = {"name": "baltika", "description": "beer", "price": 20, "quantity": 22}
#
#     fff = Product.new_product(aaa)
#     ooo = Product.new_product(bbb)
#
#     print()
#     print(fff.name)
#     print(fff.description)
#     print(fff.price)
#     print(fff.quantity)
#     print()
#     print(fff)
#     print(ooo)
#     print()
#     print(fff + ooo)
#
#     ## ********************************************************
#
#     # проверка @price.setter
#     print()
#     fff.price = 55.83
#     print(fff.price)
#     fff.quantity = 8
#     print(fff.quantity)
#
#     # *********************************************
