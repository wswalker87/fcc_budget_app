class Category:
    
    def __init__(self, name):
        """This is a class to sort items into a budgeting app.
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
    global balance, description, name


    def deposit(self, amount, description=""):
        """**deposit:**: Accepts an amount and description. If no description, defaults to empty string. Method will append an object to the ledger list
        in the form of {"amount": amount, "description": description}.
        """
        self.ledger.append({"amount": amount, "description": description})
        balance = balance =+ amount

    def withdraw(self, amount):
        """**withdraw:** Similar to deposit, but the amount passed in should be stored in the ledger as a negative number. 
            If there are not enough funds, nothing should be added to the ledger. This method should return True if the withdrawal took place, and False otherwise.
        """
        if balance > 0:
            self.ledger.append({"amount": -abs(amount), "description": description}) # How do I make this amount negative?
            return True
            balance =+ amount
        else:
            return False
            
        
    def get_balance(self):
        """**get_balance:** Return the current balance of the category, based off deposits and withdrawls.  
        """
        current_balance = balance

    def transfer(self, amount, description=""):
        """**transfer:** Args are an amount and another budget category. Will add a withdrawl with the amount and description "Transfer to [Destination Budget Category]". 
    The method should then add a deposit to the other budget category with the amount and the description "Transfer from [Source Budget Category]". 
    If there are not enough funds, nothing should be added to either ledgers. This method should return True if the transfer took place, and False otherwise.
        """
        pass

    def check_funds(self, amount):
        """**check_funds:** Accepts an amount as an arg. Returns False if the amount is greater than the balance in the category, True otherwise. Should be used by withdraw and transfer.
        """
        pass
