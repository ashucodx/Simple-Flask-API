from flask import Flask, jsonify

app = Flask(__name__)

# Sample data
users = [
    {"id": 1, "name": "Raju", "email": "raju@example.com"},
    {"id": 2, "name": "Ram", "email": "ram@example.com"}
]

# Home route
@app.route('/')
def home():
    return "Welcome to the Simple API made by Ashu!"

# Users route
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

# Add user route
@app.route('/users', methods=['POST'])
def add_user():
    new_user = request.get_json()
    users.append(new_user)
    return jsonify(new_user), 201

if __name__ == '__main__':
    app.run(debug=True)
