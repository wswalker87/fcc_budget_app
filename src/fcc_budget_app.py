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

    def transfer(self, amount, category):
        """**transfer:** Args are an amount and another budget category. Will add a withdrawl with the amount and description "Transfer to [Destination Budget Category]". 
        The method should then add a deposit to the other budget category with the amount and the description "Transfer from [Source Budget Category]". 
        If there are not enough funds, nothing should be added to either ledgers. This method should return True if the transfer took place, and False otherwise.
        """
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self, amount):
        """**check_funds:** Accepts an amount as an arg. Returns False if the amount is greater than the balance in the category, True otherwise. Should be used by withdraw and transfer.
        """
        if amount > self.balance:
            return False
        else:
            return True
        
    def __str__(self):
        """Custom string representation for the Category instance."""
        # Title line with the category name centered in a line of 30 characters, surrounded by stars
        title_line = f"{self.name:*^30}\n"
        
        # Ledger lines with each transaction
        ledger_lines = ""
        for item in self.ledger:
            description = item["description"][:23]  # First 23 characters of the description
            amount = f"{item['amount']:.2f}"       # Amount with two decimal places
            ledger_lines += f"{description:<23}{amount:>7}\n"
        
        # Total balance line
        total_line = f"Total: {self.balance:.2f}"
        
        return title_line + ledger_lines + total_line
