class Product:
    def __init__(self, name: str | None = None, description: str | None = None, price: float = 0.0, quantity: int = 0):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
