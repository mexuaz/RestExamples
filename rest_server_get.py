from flask import Flask, json

api = Flask(__name__)

@api.route('/users', methods=['GET'])
def get_users():
	with open('./db/users.json') as f:
		users = json.load(f)
	return json.dumps(users)

if __name__ == '__main__':
	# host=0.0.0.0 Listen on all public IPs
	api.run(host="localhost", port=8500, debug=False)
