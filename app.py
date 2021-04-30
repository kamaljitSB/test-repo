from flask import Flask, request, render_template
import csv

app = Flask(__name__)

def create_csv(name, balance):
        with open("data.csv", 'w', newline = '') as f:
            writer = csv.writer(f)
            rows = [name, balance]

            fields = ["Name", "Balance"]
            
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
    return render_template("test.html")

@app.route('/', methods=['POST'])
def my_form_post():
    name = request.form['name']
    balance = request.form['balance']
    
    try: 
        with open("data.csv", 'r') as f:
            add_to_csv(name, balance)
    except FileNotFoundError:
        create_csv(name, balance)

    return render_template("test.html")


if __name__ == "__main__":
    app.run(debug=True)