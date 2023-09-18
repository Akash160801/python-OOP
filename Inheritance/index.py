import csv


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

    @classmethod
    def itemsCsv(cls):
        with open("4/items.csv", "r") as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            # print(item)
            Item(
                name=item.get("name"),
                price=float(item.get("price")),
                quantity=int(item.get("quantity")),
            )

    @staticmethod
    def is_integer(num):
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    # to represent the object of Item in better and readable manner.
    def __repr__(self):
        return f"Item('{self.name}',{self.price},{self.quantity})"


# Item.itemsCsv()
# print(Item.all)
print(Item.is_integer(7.0))
