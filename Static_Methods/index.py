class Item:
    Pay = 0.8  # adding a 20% discount.
    all = []

    def __init__(self, name: str, price: int, quantity=0):
        # Assign to self objects
        self.name = name
        self.price = price
        self.quantity = quantity

        # Actions to execute.
        Item.all.append(self)

    def totalPrice(self):
        return self.price * self.quantity

    def discount(self):
        self.price = self.price * self.Pay

    # to represent the object of Item in better and readable manner.
    def __repr__(self):
        return f"Item('{self.name}',{self.price},{self.quantity})"


item1 = Item("Phone", 100, 5)
item2 = Item("Laptop", 300, 15)
item3 = Item("AirBag", 200, 2)
item4 = Item("Washing Machine", 1000, 26)
item5 = Item("Tablet", 150, 5)

print(Item.all)  # To print the object of all the items

""" # a loop to print all the item's name.
for instance in Item.all:
    print(instance.name) """
