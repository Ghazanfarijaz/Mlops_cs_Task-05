from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient("mongodb://mongo:27017/")  # Connecting to MongoDB container

db = client["mydatabase"]  # Database name
collection = db["users"]  # Collection name


@app.route('/store', methods=['POST'])
def store_data():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    if name and email:
        user_data = {'name': name, 'email': email}
        collection.insert_one(user_data)
        return jsonify({'message': 'Data stored successfully'}), 201
    else:
        return jsonify({'error': 'Name and Email are required'}), 400


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
