from flask import Flask, Blueprint, jsonify, make_response
from flask_restplus import Api,Resource,reqparse
from ..model.product_models import Item
from ..common import validator

app = Flask(__name__)

product_print = Blueprint("products", __name__)
api = Api(product_print, prefix="/api/v1")

carts=[]

class get_all(Resource):

    """"
    This class gets all questions and posts a question
    """
    parser = reqparse.RequestParser()
    parser.add_argument("name")
    parser.add_argument("price")
    parser.add_argument("quantity")
    parser.add_argument("description")


    def get(self):
        return {'cart':carts}, 200

    def post(self):
        id_count = 1
        for cart in carts:
            id_count += 1

        data = self.parser.parse_args()
        new_item = Item(data['name'], data['price'], data['quantity'], data['description'])
        new_item_dict = new_item.make_dict(id_count)

        carts.append(new_item_dict)
        return {'message': 'Your item has been added successfully'}, 201 

    

    
api.add_resource(get_all, "/products")