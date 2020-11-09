# Create a mini application which mimics a shopping website (Amazon, Emag)
# Commands we can give the program:
# we can add a user with a specified username: python3 app.py user add <username>, error if the username already exists
# we can delete a user specifying its username: python3 app.py user remove <username>, error if the username does not exist
# we can edit a user's username: python3 app.py user edit <old_username> <new_username>, error if the old_username does not exist, error if the new_username already exists
# we can add a product and specify how much of it we have in stock: python3 app.py product add <product_name> <price> <stock_number>, error if product_name already exists, error if price is not int or float, error if stock_number is not int
# we can delete a product: python3 app.py product delete <product_name>, error if the product name does not exist
# we can add more items of a product, it will increase the stock number: python3 app.py product add stock <product_name> <new_number_of_items>, error if product_name does not exist, error if new_number is not int
# we can remove items from stock, it will decrease the stock number: python3 app.py product remove stock <product_name> <number_of_items_to_be_removed>, error if product_name does not exist, error if number is not int, error if we have less numbers in stock than the number of items to be removed
# we can change the price of a product: python3 app.py product edit <product_name> <new_price>, error if product does not exist, error if new_price is not int or float
# a user can add a product to wishlist: python3 app.py user wishlist add <username> <product_name>, error if the username does not exist, error if the product name does not exist
# a user can delete a product from wishlist: python3 app.py user wishlist remove <username> <product_name>, error if the username does not exist, error if the product_name does not exist
# a user can order an item: python3 app.py user order <username> <product_name> <number_of_items>, delete <product_name> from wishlist (if exists, if not do not print/raise error), decrease number from product stocks, error if there are not enough in stock, error if the username does not exist, error if the product_name does not exist
import sys
import os
# we import the class User from file user.py
from user import User

arguments = sys.argv[1:] # definim o variabila ce contine argumentele date de sistem, incepand de la 1 (eliminam pozitia 0 ce contine numele fisierului app.py)
# print(arguments)

if arguments[0] == 'user' and arguments[1] == 'add': # sa verificam argumentele date de user
  new_user = User(arguments[2]) # we create an object user
  new_user.save() # we save it on the system


if arguments[0] == 'user' and arguments[1] == 'remove':
  user = User(arguments[2])
  user.remove()

if arguments[0] == 'user' and arguments[1] == 'edit':
  user = User(arguments[2])
  user.rename(arguments[3])
