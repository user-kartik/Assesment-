from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

# Database connection
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="yourpassword",  # Replace with your MySQL password
    database="yourdatabase"   # Replace with your database name
)
cursor = connection.cursor(dictionary=True)

# Create (Insert data)
@app.route('/register', methods=['POST'])
def create_registration():
    data = request.json
    try:
        query = "INSERT INTO Registration (Name, Email, DateOfBirth, PhoneNumber, Address) VALUES (%s, %s, %s, %s, %s)"
        values = (data['Name'], data['Email'], data['DateOfBirth'], data.get('PhoneNumber'), data.get('Address'))
        cursor.execute(query, values)
        connection.commit()
        return jsonify({"message": "Registration successful!", "ID": cursor.lastrowid}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Read (Fetch data)
@app.route('/registrations', methods=['GET'])
def read_registrations():
    try:
        cursor.execute("SELECT * FROM Registration")
        result = cursor.fetchall()
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Update (Modify data)
@app.route('/register/<int:id>', methods=['PUT'])
def update_registration(id):
    data = request.json
    try:
        query = "UPDATE Registration SET Name=%s, Email=%s, DateOfBirth=%s, PhoneNumber=%s, Address=%s WHERE ID=%s"
        values = (data['Name'], data['Email'], data['DateOfBirth'], data.get('PhoneNumber'), data.get('Address'), id)
        cursor.execute(query, values)
        connection.commit()
        return jsonify({"message": "Registration updated successfully!"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Delete (Remove data)
@app.route('/register/<int:id>', methods=['DELETE'])
def delete_registration(id):
    try:
        cursor.execute("DELETE FROM Registration WHERE ID = %s", (id,))
        connection.commit()
        return jsonify({"message": "Registration deleted successfully!"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
