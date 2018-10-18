def check_using_id(list_name, other_id):
    """use the relevant id to find item in a product carts list"""

    my_item = next((item for item in list_name if item[
                   'item_id'] == other_id), None)

    if my_item:
        return my_item
    return False

def check_sale_id(list_name, other_id):
    """use the relevant id to find item in a sale record list"""

    my_item = next((item for item in list_name if item[
                   'sale_id'] == other_id), None)

    if my_item:
        return my_item
    return False

def verify_product_information(name, price, quantity, description):
    """Check the quality of product information this is characters and minimum 
       length allowed
    """
    if len(name) < 1:
        return 'You cannot post an empty name, Please add a name'
    if len(price) < 1:
        return 'You cannot post an empty price, Please add a price'
    if len(quantity) < 1:
        return 'You cannot post an empty quantity, Please add quantity'    
    if price.isalpha():
        return 'The price has to be an integer'
    if quantity.isalpha():
        return 'The quantity has to be a digit'
    if len(description) < 1:
        return 'You cannot post an empty description'

def verify_sales_information(item, price, amount_sold):
    """Check the quality of sale record information this is characters and minimum 
       length allowed
    """
    if len(item) < 1:
            return 'You cannot post an empty item name, Please add a name'
    if len(price) < 1:
        return 'You cannot post an empty price, Please add a price'
    if price.isalpha():
        return 'The price has to be an integer'
    if amount_sold.isalpha():
        return 'The price has to be a digit'


