class Product:
    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


# if __name__ == "__main__":
#     prod = Product("Smartphone", "Samsung Galaxy S28", 1000.00, 5)
#     print(prod.name)
#     print(prod.description)
#     print(prod.price)
#     print(prod.quantity)