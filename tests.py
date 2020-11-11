# first we need to import the library
import unittest

# we need to create a class and extend TestCase
class TestUser(unittest.TestCase):
  def test_true(self):
    self.assertEqual(True, True)

  def test_false(self):
    # we can add a message in case of failure
    self.assertEqual(True, False, 'error, True is not equal to False')

  def test_new(self):
    self.assertTrue(False)

  def sum(self, x, y):
    return x + y

  def test_sum(self):
    self.assertEqual(5, self.sum(2, 3))
    self.assertEqual(5, self.sum(1, 4))