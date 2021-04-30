from datetime import date


TODAY = date.today()

# print("Today's date:", TODAY)
# print(TODAY.month)

class Expense:
    """ A class to represent an expense """


    @staticmethod
    def create_from_dict(dict_):
        """Create a new Expense object from dict_

        :param dict_: dictionary with "Category" and "Amount"
        :type dict_: dict
        :return: Expense object
        :rtype: Expense
        """
        return Expense(ID=dict_["ID"], Category=dict_["Category"], Amount=float(dict_["Amount"]), Date=dict_["Date"])
        

    @staticmethod
    def get_serializable_field_names():
        """Get field names from Expense object

        :return: list of field names of Expense object
        :rtype: list
        """
        return ["Category", "Amount"]
    

    def __init__(self, ID, Category, Amount, Date=TODAY):       
        """ Initializes private attributes

        Args:
            ID (int): ID of the expense
            Category (str): Category of the expense (cannot be empty)
            Amount (float): Amount spent (cannot be negative)
            Date: Date of the expense (default is today)
        Raises:
            ValueError: 
                ID is not int
                Category is not str or is empty
                Amount is not float or negative
        """
        # Validation #
        if type(ID) is not int:
            raise ValueError("Invalid ID")
        if type(Category) is not str or not Category:
            raise ValueError("Invalid Category")
        if type(Amount) is not float or Amount < 0:
            raise ValueError("Invalid Amount")

        self._ID = ID
        self._Category = Category
        self._Amount = Amount
        self._Date = Date
    

    @property
    def ID(self):
        return self._ID


    @property
    def Category(self):
        return self._Category


    @property
    def Amount(self):
        return self._Amount


    @property
    def Date(self):
        return self._Date


    @property
    def __dict__(self):
        """Convert Expense object into dictionary

        :return: Dictionary representation of Expense
        :rtype: dict
        """
        expense_dict = {}
        expense_dict["ID"] = self.ID
        expense_dict["Category"] = self.Category
        expense_dict["Amount"] = self.Amount
        expense_dict["Date"] = self.Date

        return expense_dict


    def to_dict(self):
        """Convert Expense object into dictionary

        :return: Dictionary representation of Expense
        :rtype: dict
        """
        return self.__dict__




############################################
if __name__ == "__main__":
    Expense1 = Expense(1, "Food", 123.4, "2021-05-06")
    Expense2 = Expense(2, "Clothes", 599.99, "2021-05-08")

    
    