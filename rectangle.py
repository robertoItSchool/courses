import unittest


class Rectangle:
  def __init__(self, x, y):
    self.x = x
    self.y = y

  # implement the method to compute the perimeter, the sum of the vertices
  # write tests for it
  def perimeter(self):
    return 2 * self.x + 2 * self.y

  # implement method to compute the area
  # write tests for it
  def area(self):
    return self.x * self.y


class TestRectangle(unittest.TestCase):
  def test_perimeter(self):
    # set up
    rectangle1 = Rectangle(3, 5)
    rectangle2 = Rectangle(6, 12)

    # execution
    per1 = rectangle1.perimeter()
    per2 = rectangle2.perimeter()

    # assertions
    self.assertEqual(16, per1)
    self.assertEqual(36, per2)


# Create a subclass of Rectangle, square
class Square(Rectangle):
  def __init__(self, x):
    self.x = x
    self.y = x


class TestSquare(unittest.TestCase):
  def test_area(self):
    # set up
    square = Square(10)
    # execution
    area = square.area()
    # assertion
    self.assertEqual(100, area)

# write tests for perimeter & area
