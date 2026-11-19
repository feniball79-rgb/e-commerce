from typing import Optional

from ecommerce.product import Product


class Category:
    category_count = 0
    product_count = 0

    def __init__(
        self,
        name: str | None = None,
        description: str | None = None,
        products: Optional[list["Product"]] | None = None,
    ):
        self.name = name
        self.description = description
        self.products = products if products is not None else []
        Category.category_count += 1
        Category.product_count += len(self.products)
