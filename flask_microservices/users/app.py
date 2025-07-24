from flask import Flask, jsonify

app = Flask(__name__)

USERS = [
    {"id": 1, "username": "alice"},
    {"id": 2, "username": "bob"},
]

@app.route('/users', methods=['GET'])
def list_users():
    return jsonify(USERS)

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = next((u for u in USERS if u['id'] == user_id), None)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
