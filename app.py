from flask import Flask, request, render_template
import csv
from Models.expense import Expense
from Models.expense_manager import ExpenseManager


app = Flask(__name__)


def create_csv(name, balance):
        with open("data.csv", 'w', newline = '') as f:
            writer = csv.writer(f)
            rows = [name, balance]

            fields = ["Balance", "Budget"]
            
            # Writes fields and rows to csv
            writer.writerow(fields)
            writer.writerow(rows)


def add_to_csv(name, balance):
        # Appends to data.csv instead of writing, which would replace existing entries
        with open("data.csv", 'a', newline = '') as f:
            writer = csv.writer(f)
            rows = [name, balance]
            writer.writerow(rows)


@app.route('/')
def index():
    return render_template("main.html")


@app.route('/', methods=['POST'])
def expense():
    expense_id = int(request.form['expense_id'])
    category = request.form['category']
    amount = int(request.form['amount'])
    date = "nov1"
    EM = ExpenseManager()
    expense = Expense(expense_id, category, amount)
    EM.add_expense(expense)

    EM.to_csv("expenses.csv")

    balance = request.form['balance']
    budget = request.form['budget']

    try: 
        with open("data.csv", 'r') as f:
            add_to_csv(balance, budget)
    except FileNotFoundError:
        create_csv(balance, budget)


    return render_template("main.html")





if __name__ == "__main__":
    app.run(debug=True)