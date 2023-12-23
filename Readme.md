# Expense Database 
## Project Description
With the use of Python (OOP) to create a project based on individual expenses, which involves implementing two classes Expenses and ExpenseDatabse to model and manage financial expenses. 

The project contains the:

expenses.py: this contains the expenses model
test.py: this contains a unittest for the expenses module

# Clone the project
To copy this project, use this repo link: https://github.com/darknuma/ExpensesDatabase.git 

and on your terminal navigate to your workind directory with cd [current working directory], and use the code below

```bash
git clone https://github.com/darknuma/ExpensesDatabase.git 
```

Once cloned you would have the copy of the repo on your local computer

## Requirements
1. Installed Git on your local computer
2. Have a github account
3. Ensure you have python3.7 and above installed on your local computer.

# How to run the code
To run expenses.py on your terminal press the command
```bash
python3 expenses.py
```
This would execute the expenses.py and run the test on the for the various operations done by the Expenses Class
Expense representation
Updating the Expenses

an example below of the code:
```python
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
```
Also on the Expense Database, it would:
Instatiate the expenses database, 
Add expenses: add_expenses,
Remove Expenses: remove_expense
Get functionalites:  get_expenses_by_id, get_expenses_by_id, and Convert the database to a dictionary: to_dict

To run the test.py on yout terminal to test all the functionalites of the expenses module
```bash
python3 test.py
```



