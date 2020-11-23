import unittest
from main import get_user_and_password


class TestPassword(unittest.TestCase):
  def test_get_user_and_password(self):
    user, password = get_user_and_password('netflix')

    self.assertEqual('roberto', user)
    self.assertEqual('abcdefg', password)

  def test_get_not_configured_website(self):
    # execute - try to get info for a site not in the dictionary
    user, password = get_user_and_password('emag')

    # assertion - expect the values to be empty strings
    self.assertEqual('', user)
    self.assertEqual('', password)