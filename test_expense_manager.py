import pytest
from Models.expense_manager import ExpenseManager
from Models.expense import Expense

def test_attributes():
    """
    Tests if ExpenseManager class has the correct attributes and they are set correctly
    """
    manager = ExpenseManager()

    # Checks if private attribute exists
    assert hasattr(manager, "_expenses")

    # Checks if private attribute was set correctly
    assert manager._expenses == {}


def test_add_expense():
    """
    Tests for the add_expense method
    """
    manager = ExpenseManager()
    expense1 = Expense(1, "Health", 300, "2020-05-12")
    expense2 = Expense(2, "School", 1000, "2021-04-20")
    expense3 = Expense(3, "Food", 25.6, "2021-4-30")


    # Checks if method exists
    assert hasattr(manager, "add_expense")

    # Tests that method correctly adds expenses to dictionary
    manager.add_expense(expense1)
    manager.add_expense(expense2)
    manager.add_expense(expense3)

    assert manager._expenses[1] == expense1
    assert manager._expenses[2] == expense2
    assert manager._expenses[3] == expense3
    

def test_del_expense():
    """
    Tests for the del_expense method
    """
    manager = ExpenseManager()
    expense1 = Expense(1, "Health", 300, "2020-05-12")
    expense2 = Expense(2, "School", 100.1, "2020-05-11")

    # Checks if method exists
    assert hasattr(manager, "del_expense")

    # Adds expenses 
    manager.add_expense(expense1)
    manager.add_expense(expense2)
    assert manager._expenses[1] == expense1
    assert manager._expenses[2] == expense2

    # Checks that added expenses are deleted correctly
    manager.del_expense(1) 
    manager.del_expense(2) 
    with pytest.raises(KeyError):
        assert manager._expenses[1]
        assert manager._expenses[2]



def test_upd_expense():
    """
    Tests for the upd_expense method
    """
    manager = ExpenseManager()
    expense = Expense(1, "Health", 300, "2020-05-12")
    updated_expense = Expense(1, "School", 100.1, "2020-05-11")

    # Checks if method exists
    assert hasattr(manager, "upd_expense")

    # Adds expense
    manager.add_expense(expense)
    assert manager._expenses[1] == expense

    # Checks that update expense works correctly
    manager.upd_expense(1, updated_expense)
    assert manager._expenses[1] == updated_expense





def test_get_expenses():
    """
    Tests for the get_expenses method
    """
    manager = ExpenseManager()

    # Checks if method exists
    assert hasattr(manager, "get_expenses")

    # Checks if method returns correct value
    assert manager.get_expenses() == []


def test_from_csv():
    """
    Tests for the from_csv method
    """
    manager = ExpenseManager()

    # Checks if method exists
    assert hasattr(manager, "from_csv")


def test_to_csv():
    """
    Tests for the to_csv method
    """
    manager = ExpenseManager()

    # Checks if method exists
    assert hasattr(manager, "to_csv")


def test_read_largest_id():
    """
    Tests for the read_largest_id method
    """
    manager = ExpenseManager()

    # Checks if method exists
    assert hasattr(manager, "read_largest_id")
    