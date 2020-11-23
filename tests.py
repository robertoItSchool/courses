import unittest
from main import get_user_and_password


class TestPassword(unittest.TestCase):
  def test_get_user_and_password(self):
    user, password = get_user_and_password('netflix')

    self.assertEqual('roberto', user)
    self.assertEqual('abcdefg', password)

