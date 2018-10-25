from flask import Flask, Blueprint, jsonify, make_response
from flask_restplus import Api,Resource,reqparse
from ..model.sale_model import Sale
from ..common import validator

app = Flask(__name__)
sale_manager = Blueprint('sales', __name__)
api = Api(sale_manager,prefix='/api/v1')

sale_record=[]

class get_all(Resource):
    """ This class helps us get all the sales record """
    
    parser = reqparse.RequestParser()
    parser.add_argument("item")
    parser.add_argument("price")
    parser.add_argument("amount_sold")

    def get(self):
        # return {'sale-record':sale_record}
        return sale_record
    

    def post(self):
        id_count = 1
        for sale in sale_record:
            id_count += 1

        data = get_all.parser.parse_args()
        new_item = Sale(data['item'], data['price'], data['amount_sold'])        
        new_item_dict = new_item.make_dict(id_count)
        sale_record.append(new_item_dict)
        return {'message': 'Sale record created',}, 201

api.add_resource(get_all, "/sales")