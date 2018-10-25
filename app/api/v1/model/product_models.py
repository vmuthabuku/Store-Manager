class Item():
    """This is the product model"""

    def __init__(self, name, price, quantity, description):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.description = description


    def make_dict(self, item_id):
        """receives the item as an object and turns it to a dict"""
        return dict(
            name = self.name,
            price = self.price,
            quantity = self.quantity,
            description = self.description,
            item_id = item_id

        )