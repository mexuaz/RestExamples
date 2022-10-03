import requests, json

if __name__ == '__main__':
	res = requests.get('http://localhost:8500/users')
	if res.status_code != 200:
		raise RuntimeError(f"Error: {res.status_code}")
	users = res.json()['users']
	headers = ['Name','Lastname','Balance']
	print (f" {headers[0]:<10}| {headers[1]:<15}| {headers[2]:<10}")
	print ("="*40)
	for u in users:
		print (f" {u['firstname']:<10}| {u['lastname']:<15}| {u['balance']:<10,}")
