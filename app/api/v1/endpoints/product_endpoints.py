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
        data = self.parser.parse_args()

        verify_product = validator.verify_product_information(data['name'], data['price'], data['quantity'], data['description'])

        if verify_product:
            return {"message": verify_product}, 409

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


api.add_resource(get_all, "/products")
api.add_resource(get_id, "/products/<productid>")