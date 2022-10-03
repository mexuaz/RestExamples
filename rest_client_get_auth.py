import requests, json
from requests.auth import HTTPBasicAuth
from getpass import getpass


if __name__ == '__main__':
	username = input("Enter username: ")
	password = getpass("Enter password: ")
	res = requests.get('http://localhost:8500/mybalance', auth = HTTPBasicAuth(username, password))
	if res.status_code != 200:
		raise RuntimeError(f"Error: {res.status_code}")
	print(f"Your balance is: {res.json()['balance']:,}$.")

