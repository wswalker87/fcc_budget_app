class Category:
    
    def __init__(self, name):
        """
        This is a class to sort items into a budgeting app.
        When objects are created, they are passed in the name of the category. 
        The class should have an instance variable called ledger that is a list. The class should also contain the following methods:
        deposit, withdraw, get_balance, transfer, check_funds
        
        When the budget object is printed it should display:

        A title line of 30 characters where the name of the category is centered in a line of * characters.
        A list of the items in the ledger. Each line should show the description and amount. 
        The first 23 characters of the description should be displayed, then the amount. 
        The amount should be right aligned, contain two decimal places, and display a maximum of 7 characters.
        A line displaying the category total.
        """
        self.name = name
        self.ledger = []
        self.balance = 0

    def deposit(self, amount, description=""):
        """**deposit:**: Accepts an amount and description. If no description, defaults to empty string. Method will append an object to the ledger list
        in the form of {"amount": amount, "description": description}.
        """
        self.ledger.append({"amount": amount, "description": description})
        self.balance += amount

    def withdraw(self, amount, description=""):
        """**withdraw:** Similar to deposit, but the amount passed in should be stored in the ledger as a negative number. 
            If there are not enough funds, nothing should be added to the ledger. This method should return True if the withdrawal took place, and False otherwise.
        """
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            self.balance -= amount
            return True
        else:
            return False
            
        
    def get_balance(self):
         """**get_balance:** Return the current balance of the category, based off deposits and withdrawls."""
         return self.balance

    def transfer(self, amount, description=""):
        """**transfer:** Args are an amount and another budget category. Will add a withdrawl with the amount and description "Transfer to [Destination Budget Category]". 
        The method should then add a deposit to the other budget category with the amount and the description "Transfer from [Source Budget Category]". 
        If there are not enough funds, nothing should be added to either ledgers. This method should return True if the transfer took place, and False otherwise.
        """
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from{category.name}")
            return True
        return False

    def check_funds(self, amount):
        """**check_funds:** Accepts an amount as an arg. Returns False if the amount is greater than the balance in the category, True otherwise. Should be used by withdraw and transfer.
        """
        if amount > self.balance:
            return False
        else:
            return True
        
        

# Example of unit tests
def test_deposit():
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

def test_withdraw():
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

def test_get_balance():
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

def test_check_funds():
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

                                                                                    
          

test_deposit()
test_withdraw()
test_get_balance()
test_check_funds()