from ecommerce.product import Product
from ecommerce.category import Category

prod = Product("Smartphone", "Samsung Galaxy S28", 1000.00, 5)
print(prod.name)
print(prod.description)
print(prod.price)
print(prod.quantity)

result = Category("Smartphones", "New product")
print(result.description)  # New product
print(Category.category_count)  # 1
print(Category.product_count)  # 0