from flask import Flask, json

with open('./users.json') as f:
  users = json.load(f)

api = Flask(__name__)

@api.route('/users', methods=['GET'])
def get_companies():
  return json.dumps(users)

if __name__ == '__main__':
    api.run()
