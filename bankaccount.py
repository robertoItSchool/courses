# Write 2 asserts for withdraw
# Write 2 asserts for deposit
# Add a 1ron tax for withdraw and update the test
# Return False if we try to withdraw more than what we have
# Write an assert if we try to withdraw more than what we have
import unittest

class BankAccount:
  def __init__(self, balance):
    self.balance = balance

  def withdraw(self, amount):
    if amount > self.balance:
      return False
    self.balance -= amount + 1

  def deposit(self, amount):
    self.balance += amount

class TestBankAccount(unittest.TestCase):
  def test_withdraw(self):
    account = BankAccount(100)
    account.withdraw(40)
    self.assertEqual(59, account.balance)

    account.withdraw(20)
    self.assertEqual(38, account.balance)

  def test_withdraw_more_than_we_have(self):
    account = BankAccount(5000)
    response = account.withdraw(6000)

    self.assertEquals(False, response)
    self.assertEqual(5000, account.balance)