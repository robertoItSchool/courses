import json
import os

class Warehouse:
  @staticmethod
  def add(product):
    try:
      # read from the file if it exists
      f = open('warehouse', 'r')
      items = f.read()
      decoded_items = json.loads(items)
      f.close()
    except:
      # if no file, the structure is empty
      decoded_items = {}

    decoded_items[product.name] = product.__dict__

    # write the new item structure to the file
    encoded_items = json.dumps(decoded_items)

    #open the file for writing
    f = open('warehouse', 'w')
    f.write(encoded_items)
    f.close()

  @staticmethod
  def show():
    if os.path.exists('warehouse'): # we check the file exists
      f = open('warehouse') # open the file for read
      encoded_items = f.read() # we read the JSON
      items = json.loads(encoded_items) #we decode the JSON
      f.close()
      return items
    return {}


class Product:
  def __init__(self, name, price, number):
    self.name = name
    self.price = price
    self.number = number

# warehouse = Warehouse()
Warehouse.add(Product('tv', 3000, 22))
Warehouse.add(Product('laptop', 2000, 10))

print(Warehouse.show())