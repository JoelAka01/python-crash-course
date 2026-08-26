class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.stock = 0

    def add_stock(self, quantity):
        self.stock += quantity
    def get_total_price(self, tax_rate):
        print(self.price * (1 + tax_rate) )
class PerishableProduct(Product):
    def __init__(self, name, price, expiration_date):
        super().__init__(name, price)
        self.expiration_date = expiration_date
    def is_expired (self, days_on_shelf):
        if self.expiration_days < 3 :
            return self.price * 0.8
return get_total_price()