import unittest
from flask import json
import json

from .. import create_app

class StoreManager(unittest.TestCase):
    """This class represents storemanger products posted test class"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app("testing")
        self.client = self.app.test_client()
        self.cart_items = {'name': 'What ', "price":"122", "quantity":"12", "description":"veryuu"}
        self.sample_data1 = {'name': '', "price":"122", "quantity":"12", "description":"veryuu"}
        self.sample_data2 = {'name': 'What ', "price":"ww", "quantity":"12", "description":"veryuu"}
        self.sample_data3 = {'name': 'What ', "price":"ww", "quantity":"12", "description":""}
        self.sample_data4 = {'name': 'What ', "price":"ww", "quantity":"", "description":"veryuu"}


    def test_post_item(self):
        """Testing posting product description."""

        response = self.client.post(
            '/api/v1/products', data=json.dumps(self.cart_items), content_type='application/json')
        res = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 201)

    def test_get_all(self):
        """Testing to get all items"""

        response = self.client.get(
            '/api/v1/products', data=json.dumps(self.cart_items), content_type='application/json')
        self.assertEqual(response.status_code, 200)
    
    def test_by_id(self):
        """Testing if a product can be accessed using its id"""
        response = self.client.get(
            '/api/v1/products/1', data=json.dumps(self.cart_items), content_type='application/json'
        )  
        self.assertEqual(response.status_code, 200)   
    
    def test_product_no_name(self):
        """Testing if a user cannot post a product with no name"""

        response = self.client.post(
            'api/v1/products', data=json.dumps(self.sample_data1), content_type='application/json'
        )
        result = json.loads(response.data.decode())
        self.assertTrue(
            result['message'], 'You cannot post an empty name, Please add a name')
        self.assertEqual(response.status_code, 409)
    
    def test_product_price_type(self):
        """Testing if a user cannot post a wrong product price type """

        response = self.client.post(
            'api/v1/products', data=json.dumps(self.sample_data2), content_type='application/json'
        )
        result = json.loads(response.data.decode())
        self.assertTrue(
            result['message'], 'The price has to be an integer')
        self.assertEqual(response.status_code, 409)
    
    def test_product_no_description(self):
        """ Testing if a user cannot post a product with no description """

        response = self.client.post(
            'api/v1/products', data=json.dumps(self.sample_data3), content_type='application/json'
        )
        result = json.loads(response.data.decode())
        self.assertTrue(
            result['message'], 'You cannot post an empty description')
        self.assertEqual(response.status_code, 409)

    def test_product_quantity_type(self):
        """Testing if a user cannot post a wrong product quantity type """

        response = self.client.post(
            'api/v1/products', data=json.dumps(self.sample_data4), content_type='application/json'
        )
        result = json.loads(response.data.decode())
        self.assertTrue(
            result['message'], 'The price has to be a digit')
        self.assertEqual(response.status_code, 409)

    

if __name__=='__main__':
    unittest.main()