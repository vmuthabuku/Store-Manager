from flask import Flask, Blueprint, jsonify, make_response
from flask_restplus import Api,Resource,reqparse
from ..model.sale_model import Sale
from .product_endpoints import carts, get_all
from ..common import validator

app = Flask(__name__)
sale_manager = Blueprint('sales', __name__)
api = Api(sale_manager,prefix='/api/v1')

sale_record=[]


class Get_all(Resource):
    """ This class helps us get all the sales record """
    
    parser = reqparse.RequestParser()
    parser.add_argument("item",type=str,required=True,help="cannot be blank")
    parser.add_argument("price",type=int, required=True, help="price can only be an integer")
    parser.add_argument("amount_sold",type=int, required=True, help="amount can only be an integer")

    def get(self):
        """This handles getting all sale records"""
        return {'sale record':sale_record}
    

    def post(self):
        """This handles posting a sale record"""
        data = Get_all.parser.parse_args()
        valid = validator.check_empty(data["item"])
        if valid:
            return {"message": valid}, 409

        vali = validator.check_item_name(carts, data["item"])
        if vali:
            return {"message": vali}, 409

        reduce_prod = validator.reduce_item(carts,data["amount_sold"])
        if reduce_prod:
            return {"message":reduce_prod}, 409

        price_const = validator.check_item_price(carts,data["price"])
        if price_const:
            return {"message":price_const}, 409

        id_count = 1
        for sale in sale_record:
            id_count += 1

        

        new_item = Sale(data['item'], data['price'], data['amount_sold'])        
        new_item_dict = new_item.make_dict(id_count)
        sale_record.append(new_item_dict)
        return {'message': 'Sale record created',}, 201

class get_id(Resource):
    """This class gets the sale by its id"""
    @classmethod
    def get(cls,saleid):
        check_id = validator.check_using_id(sale_record,int(saleid))
        if check_id:
            return check_id, 200
        return {'message':'no such id'}
               

api.add_resource(Get_all, "/sales")
api.add_resource(get_id,"/sales/<saleid>")