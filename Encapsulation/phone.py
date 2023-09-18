from items import Item


class Phone(Item):
    def __init__(self, name: str, price: int, quantity=0, broken_phones=0):
        # Calling 'super' function to access the attributes/methods of parent class
        super().__init__(name, price, quantity)

        # Assign to self objects
        self.broken_phones = broken_phones
