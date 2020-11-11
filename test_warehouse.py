import unittest
import json
import os
from warehouse import Product, Warehouse


class TestWarehouse(unittest.TestCase):
  def test_add(self):
    # setup
    os.remove('warehouse')  # remove file so we start fresh
    product1 = Product('toothbrush', 100, 50)
    product2 = Product('paper', 1, 1000)
    product3 = Product('paper2', 1, 222)

    # execution, execute what we want to test
    Warehouse.add(product1)
    Warehouse.add(product2)

    # assertion
    f = open('warehouse')
    json_list = f.read()
    f.close()
    actual_list = json.loads(json_list)  # decode the JSON from the file

    expected_list = {'blabla': product1.__dict__, product2.name: product2.__dict__}

    self.assertEqual(expected_list, actual_list)

    # cleanup
    os.remove('warehouse')
