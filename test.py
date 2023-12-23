import unittest
from datetime import datetime, timezone
from expenses import Expense, ExpenseDatabase  # Replace 'your_expense_module' with the actual name of your module

class TestExpenseDatabase(unittest.TestCase):
    def setUp(self):
        # Create an instance of ExpenseDatabase for testing
        self.expensedb = ExpenseDatabase()

    def test_add_expense(self):
        expense = Expense("Test Expense", 500)
        self.expensedb.add_expense(expense)
        self.assertIn(expense, self.expensedb.expenses)

    def test_remove_expense(self):
        expense = Expense("Test Expense", 500)
        self.expensedb.add_expense(expense)
        expense_id = expense.expense_id
        self.expensedb.remove_expense(expense_id)
        self.assertNotIn(expense, self.expensedb.expenses)

    def test_get_expenses_by_id(self):
        expense = Expense("Test Expense", 500)
        self.expensedb.add_expense(expense)
        retrieved_expense = self.expensedb.get_expenses_by_id(expense.expense_id)
        self.assertEqual(retrieved_expense, expense)

    def test_get_expenses_by_title(self):
        expense = Expense("Test Expense", 500)
        self.expensedb.add_expense(expense)
        retrieved_expense = self.expensedb.get_expenses_by_title("Test Expense")
        self.assertEqual(retrieved_expense, expense)

    def test_to_dict(self):
        expense = Expense("Test Expense", 500)
        self.expensedb.add_expense(expense)
        expected_dict = [expense.to_dict()]
        self.assertEqual(self.expensedb.to_dict(), expected_dict)

    def test_update_expense(self):
        expense = Expense("Test Expense", 500)
        self.expensedb.add_expense(expense)

        updated_title = "Updated Test Expense"
        updated_amount = 700

        expense.update(title=updated_title, amount=updated_amount)
        self.expensedb.add_expense(expense)

        retrieved_expense = self.expensedb.get_expenses_by_id(expense.expense_id)
        self.assertEqual(retrieved_expense.expense_title, updated_title)
        self.assertEqual(retrieved_expense.amount, updated_amount)

if __name__ == '__main__':
    unittest.main()
