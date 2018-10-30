def check_using_id(list_name, other_id):
    """use the relevant id to find item in a product carts list"""

    my_item = next((item for item in list_name if item[
                   'item_id'] == other_id), None)

    if my_item:
        return my_item
    return False

def check_empty(s):
    if s == '':
        return "cannot be blank"

def check_name(l_name,name):
    for item in l_name:
        if item["name"] == name:
            return "Product already in inventory"

def check_item_name(lis_name, item):
    for item in lis_name:
        if item["name"] != item:
            return{"message":"item not in inventory"}

def check_item_price(lis, price):
    for item in lis:
        if item["price"] != price:
            return{"message":"price has to be the same"}


def reduce_item(list_nme,amount_sold):
    for item in list_nme:
        if item["quantity"] >= amount_sold:
            item["quantity"] -= amount_sold
            return{"message":"product updated"}
        return{"message":"sold cant exceed quantity"}

