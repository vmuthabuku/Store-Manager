class Sale():
    """This is the product model"""

    def __init__(self, item, price, amount_sold):
        self.item = item
        self.price = price
        self.amount_sold = amount_sold       


    def make_dict(self,item_id):
        """receives the item as an object and turns it to a dict"""
        return dict(
            item = self.item,
            price = self.price,
            amount_sold = self.amount_sold,
            item_id = item_id
        )