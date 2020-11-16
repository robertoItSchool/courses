import requests
import json
import unittest
from unittest.mock import patch

def get_iss():
  parameters = {"lat": 40.71, "lon": -74}
  response = requests.get("http://api.open-notify.org/iss-pass.json", params=parameters)

  print(response)
  return response['status_code']

  encoded_json = response.json()
  print(encoded_json)
  print(encoded_json['response'])
  # json.loads(encoded_json)

class TestIss(unittest.TestCase):
  # def test_error(self):
  #   with self.assertRaises(TypeError):
  #     get_iss()

  @patch('requests.get', return_value={'status_code': 400})
  def test_iss(self, iss_call):
    response_code = get_iss()

    self.assertEqual(400, response_code)


