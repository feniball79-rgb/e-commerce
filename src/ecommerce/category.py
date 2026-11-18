from typing import Optional
from ecommerce.product import  Product

class Category:
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: Optional[list["Product"]] = None):
        self.name = name
        self.description = description
        self.products = products if products is not None else []
        Category.category_count += 1
        Category.product_count += len(products) if products is not None else 0


# if __name__ == "__main__":
#
#     result = Category("Smartphones", "New product")
#     print(result.description)  # New product
#     print(Category.category_count)  # 1
#     print(Category.product_count)  # 0

