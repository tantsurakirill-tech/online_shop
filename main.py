products = [
    {"name": "Ноутбук", "price": 85000, "stock": 4},
    {"name": "Мышь", "price": 2500, "stock": 15},
    {"name": "Монитор", "price": 32000, "stock": 0},
    {"name": "Клавиатура", "price": 7000, "stock": 8},
]


def show_products(products):
    for product in products:
        print(
            f"{product['name']} — "
            f"{product['price']} руб. — "
            f"{product['stock']} шт."
        )



def search_products(products: list[dict[str, int | str]], query: str) -> list[dict[str, int | str]]:
    return [product for product in products if query.lower() in product["name"].lower()]


def filter_by_price(products: list[dict[str, int | str]], price: int):
    return [product for product in products if product["price"] > price]


show_products(products)

print(search_products(products, 'бук'))

print(filter_by_price(products, 7500))