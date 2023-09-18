from items import Item

item1 = Item("MyItem", 900)

# item1.apply_increment(0.2)
# print(item1.price)

item1.send_email()

# It will show attribute error as the method is made private using abstraction.
item1.__prepare_body()
