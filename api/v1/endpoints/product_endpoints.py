from flask import Flask, Blueprint, jsonify, make_response
from flask_restplus import Api,Resource,reqparse
from ..model.product_models import Item
from ..common import validator

app = Flask(__name__)

product_print = Blueprint("api", __name__)
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

    
api.add_resource(get_all, "/products")