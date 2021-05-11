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

    # Checks if method exists
    assert hasattr(manager, "add_expense")


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
    

def test_by_month_expense():
    manager = ExpenseManager()
    Expense1 = Expense(1, "Food", 50, "2020-04-29")
    Expense2 = Expense(2, "School", 20, "2021-04-30")
    Expense3 = Expense(3, "Food", 36.6, "2021-05-01")
    Expense4 = Expense(4, "Family", 100, "2021-05-02")
    Expense5 = Expense(5, "Family", 88.8, "2021-01-02")
    Expense6 = Expense(6, "Health", 62, "2021-01-31")

    # Add to the manager
    manager.add_expense(Expense1)
    manager.add_expense(Expense2)
    manager.add_expense(Expense3)
    manager.add_expense(Expense4)
    manager.add_expense(Expense5)
    manager.add_expense(Expense6)

    assert manager.by_month_expense()["Apr"] == 20
    assert manager.by_month_expense()["May"] == 136.6
    assert manager.by_month_expense()["Jan"] == 150.8
