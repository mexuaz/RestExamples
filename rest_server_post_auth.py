from flask import Flask, json, jsonify, make_response, request
from flask_httpauth import HTTPBasicAuth
from hashlib import sha1

database = './db/users.json'
api = Flask(__name__)
auth = HTTPBasicAuth()
user_info = None
users = None

@auth.verify_password
def verify_password(username, password):
	global users
	global user_info
	with open(database) as f:
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
	return make_response(jsonify({'Error': 'Not Found'}), 404)


@api.route('/fund', methods=['POST'])
@auth.login_required
def add_fund():
	global users
	global user_info
	# Use get_data if post information is comming in data mode
	# request.get_data())
	if not request.is_json or not 'amount' in request.json:
		return make_response(jsonify({'Error': 'Bad Request'}), 400)
	for u in users:
		if user_info['username'] == u['username']:
			u['balance'] = u['balance'] + float(request.get_json()['amount'])
			with open(database, 'w', encoding='utf-8') as outfile:
				json.dump({"users": users}, outfile, ensure_ascii=False, sort_keys=True, indent='\t')
			user_info = u
			return make_response(jsonify({'Fund': 'Processed'}), 200)
	return make_response(jsonify({'Error': 'Internal Server Error'}), 500)


@api.route('/mybalance', methods=['GET'])
@auth.login_required
def get_maybalance():
	return jsonify({'balance': user_info['balance']})

if __name__ == '__main__':
	# host=0.0.0.0 Listen on all public IPs
	api.run(host="localhost", port=8500, debug=False)


