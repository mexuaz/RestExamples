from flask import Flask, json, jsonify, make_response, request
from flask_httpauth import HTTPBasicAuth
from hashlib import sha1


api = Flask(__name__)
auth = HTTPBasicAuth()
user_info = None

@auth.verify_password
def verify_password(username, password):
	global user_info
	with open('./db/users.json') as f:
		users = json.load(f)['users']
	for u in users:
		if username == u['username']:
			if sha1(password.encode('utf-8')).hexdigest() == u['pass_sh1']:
				user_info = u
				return True
			else:
				return False
	return False



@auth.error_handler
def unauthorized():
	return make_response(jsonify({'Error': 'Unauthorized Access'}), 401)

@api.errorhandler(404)
def not_found(error):
	return make_response(jsonify({'Error': 'Not found'}), 404)


@api.route('/mybalance', methods=['GET'])
@auth.login_required
def get_maybalance():
	return jsonify({'balance': user_info['balance']})

if __name__ == '__main__':
	# host=0.0.0.0 Listen on all public IPs
	api.run(host="localhost", port=8500, debug=False)


