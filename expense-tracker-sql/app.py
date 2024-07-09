from flask import Flask, request, jsonify
import sqlite3 as sql3
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    return 'Hello, World!'

# Function to add a user
@app.route('/adduser', methods=['POST'])
def add_user():
    if request.method == 'POST':
        email = request.json['addemail']
        password = request.json['addpassword']
        firstname = request.json['addfirstname']
        lastname = request.json['addlastname']

    with sql3.connect('expense_tracker.db') as conn:
        cursor = conn.cursor()
        cursor.execute(f"insert into users values {(email, password, firstname, lastname)};")
        conn.commit()
    
    return jsonify({"message": "Success"})

@app.route('/additems', methods=['POST'])
def add_items():
    if request.method == 'POST':
        email = request.json['email']
        #id = request.json['id']
        date = request.json['date']
        amount = request.json['amount']
        details = request.json['details']

    with sql3.connect('expense_tracker.db') as conn:
        cursor = conn.cursor()
        cursor.execute("insert into items_list (date, amount, details, email) values (?, ?, ?, ?);", 
                       (date, amount, details, email))
        conn.commit()
    
    return jsonify({"message": "Success"})

# Function to get all the users
@app.route('/getall', methods=['GET'])
def get_all():
    with sql3.connect('expense_tracker.db') as conn:
        cursor = conn.cursor()
        res = cursor.execute(f"select * from users;")
    return res.fetchall()

@app.route('/getallitems', methods=['GET'])
def get_all_items():
    with sql3.connect('expense_tracker.db') as conn:
        cursor = conn.cursor()
        res = cursor.execute(f"select * from items_list;")
    return res.fetchall()

# Function to Auth
@app.route('/auth', methods=['POST', 'GET'])
def auth():
    if request.method == 'POST':
        email = request.json['email']
        password = request.json['password']

    with sql3.connect('expense_tracker.db') as conn:
        cursor = conn.cursor()
        res = cursor.execute(f"select * from users;")
    
    ok = {"message": "True"}
    nok = jsonify({"message": "False"})

    for x in res:
        if email == x[0]:
            if password == x[1]:
                ok["email"] = x[0]
                ok['firstname'] = x[2]
                ok['lastname'] =  x[3]
                return jsonify(ok)
    return nok

@app.route('/getitemsbyemail', methods=['POST', 'GET'])
def get_items_email():
    if request.method == 'POST':
        email = request.json['email']

    with sql3.connect('expense_tracker.db') as conn:
        cursor = conn.cursor()
        res = cursor.execute(f"select * from items_list where email = '{email}';")
    
    resp = {"items":[]}

    for x in res.fetchall():
        resp['items'].append({"id": x[0], 
                     "date": x[1],
                       "amount": x[2], 
                       "details":x[3], 
                       "email":x[4]
                       }
                       )
    
    return jsonify(resp)

@app.route('/deleteitems', methods=['POST'])
def delete_items():
    if request.method == 'POST':
        id = request.json['delid']
    
    with sql3.connect('expense_tracker.db') as conn:
        cursor = conn.cursor()
        cursor.execute(f"delete from items_list where id = {id};")
        conn.commit()
    return jsonify("Deleted Successfully!")

@app.route('/update', methods=['POST'])
def update_items():
    if request.method == 'POST':
        id = request.json['uid']
        amount = request.json['uamount']
        details = request.json['udetails']
        
    with sql3.connect('expense_tracker.db') as conn:
        cursor = conn.cursor()
        cursor.execute("update items_list set amount = ?, details = ?  where id = ?;",(amount, details, id))
        conn.commit()
    return jsonify("Deleted Successfully!")
    


if __name__ == '__main__':
    app.run(debug=True)
