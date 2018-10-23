from flask import Flask, Blueprint, jsonify, make_response
from flask_restplus import Api,Resource,reqparse
from ..model.product_models import Item
from ..common import validator

app = Flask(__name__)

product_print = Blueprint("products", __name__)
api = Api(product_print, prefix="/api/v1")

carts=[]

parser = reqparse.RequestParser()
parser.add_argument('name', type=str, required=True, help="Name cannot be blank!")
parser.add_argument('price', type=int, required=True, help="price can only be an integer")
parser.add_argument('quantity', type=int, required=True, help="quantity can only be an integer")
parser.add_argument('description',type=str, required=True, help="Description cannot be blank")

class get_page(Resource):
    def get(self):
        return {"Message":"Welcome to my store-manager"}, 200

class get_all(Resource):

    """"
    This class gets all questions and posts a question
    """

    def get(self):
        """This handles getting all products in a cart"""
        return {'Shopping cart':carts}, 200

    def post(self):
        """This handles posting a product"""
        data = parser.parse_args()
        verify_product = validator.check_empty(data['name'])

        if verify_product:
            return {"message": verify_product}, 409

        verify_prod = validator.check_empty(data['description'])

        if verify_prod:
            return {"message": verify_prod}, 400

        id_count = 1
        for cart in carts:
            id_count += 1

        new_item = Item(data['name'], data['price'], data['quantity'], data['description'])
        new_item_dict = new_item.make_dict(id_count)

        carts.append(new_item_dict)
        return {'message': 'Your item has been added successfully'}, 201 

class get_id(Resource):
    """This class gets the item by its id"""
    @classmethod
    def get(cls, productid):
        check_id = validator.check_using_id(carts,int(productid))
        if check_id:
            return check_id, 200
        return {'message':'no such question'}

api.add_resource(get_page, "/")
api.add_resource(get_all, "/products")
api.add_resource(get_id, "/products/<productid>")