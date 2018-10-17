import os
import unittest
from flask import json
import json


from ..app import create_app

class SaleRecord(unittest.TestCase):
    """This class represents Questions and Answers posted."""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app("testing")
        self.client = self.app.test_client()
        self.sale_items = {'item': 'What ', "price":"122", "amount_sold":"12"}

    def test_post_sale(self):
        response = self.client.post(
            '/api/v1/sales', data=json.dumps(self.sale_items), content_type='application/json')
        self.assertEqual(response.status_code, 201)

    def test_get_all(self):
        """Testing to get all items"""
        response = self.client.get(
            '/api/v1/sales', data=json.dumps(self.sale_items), content_type='application/json')
        self.assertEqual(response.status_code, 200)
    
    def test_by_id(self):

        response = self.client.get(
        '/api/v1/sales/1', data=json.dumps(self.sale_items), content_type='application/json'
        )  
        self.assertEqual(response.status_code, 200)  

if __name__=='__main__':
    unittest.main()

    