from project.product import Product


class ProductRepository:
    def __init__(self):
        self.products = []

    def add(self, product: Product):
        self.products.append(product)

    def find(self, product_name: str):
        return [pr for pr in self.products if pr.name == product_name][0]

    def remove(self, product_name):
        for pr in self.products:
            if pr.name == product_name:
                self.products.remove(pr)

    def __repr__(self):
        result = []
        for pr in self.products:
            result.append(f"{pr.name}: {pr.quantity}")
        return '\n'.join(result)



