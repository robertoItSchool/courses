import unittest
from main import get_user_and_password, EmptyCredentials, Credentials


class TestPassword(unittest.TestCase):
  def test_get_user_and_password(self):
    credentials = get_user_and_password('netflix')

    expected_credentials = Credentials('roberto', 'abcdefg')
    self.assertEqual(expected_credentials.__dict__, credentials.__dict__)

  def test_get_not_configured_website(self):
    # execute - try to get info for a site not in the dictionary
    credentials = get_user_and_password('emag')

    # assertion - expect the values to be empty strings
    self.assertEqual(EmptyCredentials().__dict__, credentials.__dict__)


if __name__ == '__main__':
  unittest.main()
