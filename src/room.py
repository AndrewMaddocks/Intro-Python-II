# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.s_to = None
        self.w_to = None
        self.e_to = None
        self.n_to = None

    # def move_room(self, product):
    #     purchase = Purchase(product, self)
    #     self.purchases.append(purchase)
