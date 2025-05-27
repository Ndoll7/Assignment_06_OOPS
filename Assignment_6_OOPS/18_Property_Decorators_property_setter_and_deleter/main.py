# Create a class Product with a private attribute _price. Use @property to get the price, @price.setter to update it,
#  and @price.deleter to delete it.

class Product:
    def __init__(self, price):
        self._price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, new_price):
        self._price = new_price

    @price.deleter
    def price(self):
        print("Deleting Price...!")
        del self._price

p = Product("2000")
print(p.price)
p.price = "5000"
print(p.price)
del p.price
# print(p.price)
