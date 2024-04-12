from flask import Flask, request, jsonify
import main
import inform
import login

app = Flask(__name__)

valid_users = {
    "7": "pass",
    "11": "pass"
}

user_updates = {}
user_queries = {}

@app.route('/start', methods=['POST'])
def start_route():
    data = request.get_json()
    user_id = data.get('user_id')
    password = data.get('password')

    if user_id in valid_users and valid_users[user_id] == password:

        updates = login.main(user_id)
        if updates != "not":
            return updates, 200
        else:
            jsonify({"error": "no updates"}), 401
    else:
        return jsonify({"error": "Invalid credentials"}), 401


@app.route('/query', methods=['POST'])
def query():
    data = request.get_json()
    user_id = data.get('user_id')
    query = data.get('query')

    if user_id in valid_users:
        response = {
            "message": "Query results for user {}".format(user_id),
            "query": query,
            "results": user_queries.get(user_id, {}).get(query, "No results found")
        }
        return jsonify(response), 200
    else:
        return jsonify({"error": "User not found"}), 404


if __name__ == '__main__':
    app.run(debug=True)
