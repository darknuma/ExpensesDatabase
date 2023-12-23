import uuid
from datetime import datetime, timezone

# creating an Expenses class: Represents an individual financial expense.
class Expense:
    # attributes 
    def __init__(self, title, amount):
        self.expense_id = str(uuid.uuid4())
        self.expense_title = title  
        self.amount = amount
        self.created_at = datetime.now(timezone.utc) 
        self.updated_at = datetime.now(timezone.utc)  
        
    # methods
    def update(self, title=None, amount=None):
        if title is not None:
            self.expense_title = title
        if amount is not None:
            self.amount = amount
        self.updated_at = datetime.now(timezone.utc)
    
    def to_dict(self):
        return {
            'id': self.expense_id,
            'expense_title': self.expense_title,
            'amount': self.amount,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }

# create a class for the expensesdb for a collection of expense objects
class ExpenseDatabase:

    def __init__(self):
        # initialize an empty database
        self.expenses = []
    
    # this method adds an expense to the database
    def add_expense(self, expense):
        self.expenses.append(expense)

    # this method removes expenses_id from the database
    def remove_expense(self, expense_id):
        self.expenses = [expense for expense in self.expenses if expense.expense_id!= expense_id]

    # this method gets the expenses by id
    def get_expenses_by_id(self, expense_id):
        for expense in self.expenses:
           if expense.expense_id == expense_id:
               return expense
        return None

    # this method gets an expenses by title  
    def get_expenses_by_title(self, expense_title):
        for expense in self.expenses:
            if expense.expense_title == expense_title:
                return expense
        return None
    
    def to_dict(self):
        return [expense.to_dict() for expense in self.expenses]
        
 


 
if  __name__ == "__main__":
    # Create instances
    expensedb = ExpenseDatabase()

    # Test 1: Add an expense
    expense = Expense("Rent", 1000)
    expensedb.add_expense(expense)
    assert len(expensedb.expenses) == 1, "Test 1 failed: One expense should be added to the database."

    # Test 2: Update the expense
    expense.update(title="Updated Rent", amount=1200)
    assert expense.expense_title == "Updated Rent", "Test 2 failed: Expense title should be 'Updated Rent'."
    assert expense.amount == 1200, "Test 2 failed: Expense amount should be 1200."

    # Test 3: Add new expenses
    expense1 = Expense("School Fees", 2000)
    expense2 = Expense("Car", 1500)

    expensedb.add_expense(expense1)
    expensedb.add_expense(expense2)

    assert len(expensedb.expenses) == 3, "Test 3 failed: Three expenses should be in the database."

    # Test 4: Verify updating another expense
    expense1.update(title="Updated School Fees", amount=2500)
    assert expense1.expense_title == "Updated School Fees", "Test 4 failed: Expense title should be 'Updated School Fees'."
    assert expense1.amount == 2500, "Test 4 failed: Expense amount should be 2500."

    # Test 5: Verify the update for the first expense
    updated_expense = expensedb.get_expenses_by_id(expense.expense_id)
    assert updated_expense.to_dict() == expense.to_dict(), "Test 5 failed: Updated expense details should match."

    # Test 6: Remove an expense
    expensedb.remove_expense(expense2.expense_id)
    assert len(expensedb.expenses) == 2, "Test 6 failed: One expense should be removed from the database."

    print("All tests passed.")


