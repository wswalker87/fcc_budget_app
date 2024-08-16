# Complete unit tests for the fcc_budget_app.py file.

# **NOTE THAT I HAD TO NAME THE FILE test_budget_app.py IN ORDER TO RUN THE TESTS.**

import unittest
from fcc_budget_app import *

# Define a class to crease the suite of tests

class TestBudget(unittest.TestCase):

    def test_deposit(self):
        category = Category("Food")
        
        # Test deposit with a description
        category.deposit(100, "Initial deposit")
        print(category.ledger)
        assert category.ledger == [{"amount": 100, "description": "Initial deposit"}]
        print(category.balance)
        assert category.balance == 100
        
        # Test deposit without a description
        category.deposit(50)
        assert category.ledger == [
            {"amount": 100, "description": "Initial deposit"},
            {"amount": 50, "description": ""}
        ]
        assert category.balance == 150
        print(category.balance)
        
        print("All deposit tests passed.")

    def test_withdraw(self):
        category = Category("Food")
        
        # Test withdraw with enough money
        category.balance = 100
        print(category.balance)
        category.withdraw(100, "Initial withdrawl")
        print(category.ledger)
        assert category.ledger == [{"amount": -100, "description": "Initial withdrawl"}]
        print(category.balance)
        assert category.balance == 0 # add assertion statement here. 
        
        # Test withdraw without enough money
        category.balance = 50
        category.withdraw(100)
        assert category.ledger == [
            {"amount": -100, "description": "Initial withdrawl"}]
        assert category.balance == 50
        
        print("All withdraw tests passed.")

    def test_get_balance(self):
        category = Category("Food")
        category_balance = 0
        print(category.ledger)
        # Test balance adding to the ledger
        category.deposit(2000)
        category.deposit(50)    
        category.withdraw(1500)
        print(category.ledger)

        # Get the current balance amount
        current_balance = category.get_balance()

        #Verify that the get_balance method returns the correct balance.
        assert category.balance == 550, f"Balance expected to be 550. Actual balance is {current_balance}"
        
        print("All balance request tests passed.")

    def test_check_funds(self):
        category = Category("Food")
        category_balance = 0
        print(category.ledger)
        category.deposit(2000)
        category.withdraw(1000)
        print(category.ledger)
        
        # Get the current balance
        current_balance = category.get_balance()
        
        # Verify that check_funds allows the transaction to continue
        assert category.balance == 1000, f"Balance is expected to be 1000. Actual balance is {current_balance}"

        # Verify that if the balance is insufficient, the transaction is declined. 
        category = Category("Food")
        category_balance = 0
        print(category.ledger)
        category.deposit(2000)
        category.withdraw(3000)
        print(category.ledger)
        
        # Get the current balance
        current_balance = category.get_balance()
        
        # Verify that check_funds allows the transaction to continue
        assert category.balance == 2000, f"Balance is expected to be 2000. Actual balance is {current_balance}"

        print("All check_funds test passed.")

    def test_transfer(self):
        food = Category("Food")
        clothing = Category("Clothing")

        # Make initial deposits
        food.deposit(1000, "Initial deposit")
        clothing.deposit(500, "Initial deposit")

        # Print initial balances
        print(f"Initial balance of Food category: {food.get_balance()}")
        print(f"Initial balance of Clothing category: {clothing.get_balance()}")

        # Transfer 100 from food to clothing
        food.transfer(100, clothing)

        # Food should be 900 and clothing should be 600
        assert food.get_balance() == 900, f"Expected balance: 900, but got {food.get_balance()}"
        assert clothing.get_balance() == 600, f"Expected balance: 600, but got {clothing.get_balance()}"

        # Print balances after transfer
        print(f"Balance of Food category after transfer: {food.get_balance()}")
        print(f"Balance of Clothing category after transfer: {clothing.get_balance()}")   

        # Now verify the ledger entries for each category
        print(food.ledger)
        assert food.ledger == [
            {'amount': 1000, 'description': 'Initial deposit'},
            {'amount': -100, 'description': 'Transfer to Clothing'}
        ], f'Food ledger mismatch: {food.ledger}'
        
        assert clothing.ledger == [
            {'amount': 500, 'description': 'Initial deposit'},
            {'amount': 100, 'description': 'Transfer from Food'}
        ], f'Clothing ledger mismatch: {clothing.ledger}'

        # Test transfer with insufficient funds
        result = food.transfer(1000, clothing)
        assert result is False, "Transfer should not occur due to insufficient funds"
        assert food.get_balance() == 900, "Balance should remain the same after failed transfer"
        assert clothing.get_balance() == 600, "Balance should remain the same after failed transfer"
        
        print("All transfer tests passed.")

if __name__ == "__main__":
    unittest.main()