class Item:
    Pay = 0.8  # adding a 20% discount.

    def __init__(self, name: str, price: int, quantity=0):
        # Assign to self objects
        self.name = name
        self.price = price
        self.quantity = quantity

    def totalPrice(self):
        return self.price * self.quantity

    def discount(self):
        self.price = self.price * self.Pay


item1 = Item("Phone", 100, 5)
print(item1.name)
print(item1.price)
item1.discount()
print(item1.price)


item2 = Item("Tablet", 200, 3)
print(item2.name)
item2.Pay = 0.6
item2.discount()
print(item2.price)


# The second print will first search the attribute in instance level and then in the class level.
""" print(Item.Pay)
print(item2.Pay) """

""" print(Item.__dict__)# This prints all the attributes of Item in dictionary format.
print(item2.__dict__) """
