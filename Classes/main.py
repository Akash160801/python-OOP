class Item:
    def __init__(self, name: str, price: int, quantity=0):
        # Running validations to the received arguments
        assert price >= 0, f"{price} is not greater than or equal to zero."

        """print(f"An instance creted from:{name}")"""

        # Assign to self objects
        self.name = name
        self.price = price
        self.quantity = quantity

    """ def totalPrice(self, x, y):
        return x * y """

    def totalPrice(self):
        return self.price * self.quantity


item1 = Item("Phone", -100, 5)
print(item1.name)

""" item1.name = "Phone"
item1.price = 100
item1.quantity = 5 """
""" print(item1.totalPrice(item1.price, item1.quantity)) """

item2 = Item("Tablet", 200, 3)
print(item2.name)

""" item2.name = "Tablet"
item2.price = 200
item2.quantity = 3 """

""" print(item1.name)
print(item2.name)

print(item1.price)
print(item2.price)

print(item1.quantity)
print(item2.quantity) """

print(item1.totalPrice())
print(item2.totalPrice())
