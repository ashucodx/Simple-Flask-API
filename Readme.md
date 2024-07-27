# Simple Flask API

This is a simple Flask API that demonstrates how to handle GET and POST requests. The API allows you to retrieve a list of users and add a new user to the list.

## Getting Started

### Prerequisites

- Python installed on your system. You can download it from [python.org](https://www.python.org/).
- `pip` (Python package installer) installed. It usually comes with Python.

### Installation

1. Clone the repository to your local machine:

    ```sh
    git clone https://github.com/ashucodx/simple-flask-api.git
    ```

2. Navigate to the project directory:

    ```sh
    cd simple-flask-api
    ```

3. Install the required packages:

    ```sh
    pip install flask
    ```

### Running the API

1. Open your terminal or command prompt.
2. Navigate to the project directory if you haven't already.
3. Run the following command:

    ```sh
    python app.py
    ```

4. You should see output indicating that the server is running:

    ```sh
     * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
     * Restarting with stat
     * Debugger is active!
    ```

### Using the API

You can use tools like [POSTMAN](https://www.postman.com/) to test the API.

#### GET Request

1. Open POSTMAN.
2. Create a new GET request with the following URL:

    ```
    http://127.0.0.1:5000/users
    ```

3. Send the request. You should receive a list of users in the response.

#### POST Request

1. Open POSTMAN.
2. Create a new POST request with the following URL:

    ```
    http://127.0.0.1:5000/users
    ```

3. Go to the **Body** tab and select **raw** and **JSON**.
4. Add the following JSON data to the body:

    ```json
    {
      "id": 3,
      "name": "abcnew",
      "email": "abcnew@example.com"
    }
    ```

5. Send the request. You should receive the new user data in the response.

### Project Structure

simple-flask-api/
│
├── app.py
└── README.md


### app.py

This file contains the main code for the API:

```python
from flask import Flask, jsonify, request

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

# GET request 
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

# POST request 
@app.route('/users', methods=['POST'])
def add_user():
    new_user = request.get_json()  
    users.append(new_user) 
    return jsonify(new_user), 201  

if __name__ == '__main__':
    app.run(debug=True)

### Contributing
If you would like to contribute to this project, please fork the repository and submit a pull request.