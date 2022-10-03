from flask import Flask, json, jsonify, make_response

api = Flask(__name__)

@api.route('/users/<username>', methods=['GET'])
def get_userinfo(username):
	with open('./db/users.json') as f:
		users = json.load(f)['users']
	for u in users:
		if u['username'] == username:
			del u['username']
			del u['pass_sh1']
			return jsonify(u)
	return make_response(jsonify({'Error': 'Bad Request'}), 400)

if __name__ == '__main__':
	# host=0.0.0.0 Listen on all public IPs
	api.run(host="localhost", port=8500, debug=False)
