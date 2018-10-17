import os
import unittest
from flask import json
import json
import sys
sys.path.append("..")

from ..app import create_app

class StoreManager(unittest.TestCase):
    """This class represents Questions and Answers posted."""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app("testing")
        self.client = self.app.test_client()
        self.cart_items = {'name': 'What ', "price":"122", "quantity":"12", "description":"veryuu"}
        
        
    def test_post_item(self):
        """Testing posting an item."""
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
        response = self.client.get(
            '/api/v1/products/1', data=json.dumps(self.cart_items), content_type='application/json'
        )  
        self.assertEqual(response.status_code, 200)   

    

if __name__=='__main__':
    unittest.main()