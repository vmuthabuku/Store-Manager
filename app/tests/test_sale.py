import os
import unittest
from flask import json
import json


from app import create_app

class SaleRecord(unittest.TestCase):
    """This class represents Sales Records Test class."""

    def setUp(self):
        """Define test variables and initialize app."""

        self.app = create_app("testing")
        self.client = self.app.test_client()
        self.sale_items = {'item': 'What ', "price":"122", "amount_sold":"12"}
        self.sample_data = {'item': '', "price":"122", "amount_sold":"12"}
        self.sample_data1 = {'item': 'What ', "price":"", "amount_sold":"12"}
        self.sample_data2 = {'item': 'What ', "price":"122", "amount_sold":"wws"}


    def test_post_sale(self):
        """Testing posting a sale record."""

        response = self.client.post(
            '/api/v1/sales', data=json.dumps(self.sale_items), content_type='application/json')
        self.assertEqual(response.status_code, 201)

    def test_get_all(self):
        """Testing to get all sale records"""
        response = self.client.get(
            '/api/v1/sales', data=json.dumps(self.sale_items), content_type='application/json')
        self.assertEqual(response.status_code, 200)
    
    def test_by_id(self):
        """Testing to get a specific sale id by its id"""
        response = self.client.get(
        '/api/v1/sales/1', data=json.dumps(self.sale_items), content_type='application/json'
        )  
        self.assertEqual(response.status_code, 200) 

    def test_empty_item(self):
        """Testing if user cannot post an empty item"""
        response = self.client.post(
        '/api/v1/sales', data=json.dumps(self.sample_data), content_type='application/json'
        ) 
        result = json.loads(response.data.decode())
        self.assertEqual(
            result['message'],  'You cannot post an empty item name, Please add a name')
        self.assertEqual(response.status_code, 409) 

    def test_price_type(self):
        """Testing if user cannot post a wrong price type"""
        response = self.client.post(
        '/api/v1/sales', data=json.dumps(self.sample_data1), content_type='application/json'
        ) 
        result = json.loads(response.data.decode())
        self.assertEqual(
            result['message'],  'You cannot post an empty price, Please add a price')
        self.assertEqual(response.status_code, 409) 

    def test_amount_item(self):
        """Testing if user cannot post wrong amount sold type"""
        response = self.client.post(
        '/api/v1/sales', data=json.dumps(self.sample_data2), content_type='application/json'
        ) 
        result = json.loads(response.data.decode())
        self.assertEqual(
            result['message'],  'The price has to be a digit')
        self.assertEqual(response.status_code, 409) 
        

    

if __name__=='__main__':
    unittest.main()

    