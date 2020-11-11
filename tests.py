# first we need to import the library
import unittest

class TestUser(unittest.TestCase):
  def test_true(self):
    self.assertEqual(True, True)

  def test_false(self):
    self.assertEqual(True, False, 'error, True is not equal to False')

  def test_new(self):
    self.assertTrue(False)

  def sum(self, x, y):
    return x + y

  def test_sum(self):
    self.assertEqual(5, self.sum(2, 3))
    self.assertEqual(5, self.sum(1, 4))