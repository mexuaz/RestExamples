import requests, json

if __name__ == '__main__':
	username = input("Enter your username:")
	res = requests.get(f"http://localhost:8500/users/{username}")
	if res.status_code != 200:
		raise RuntimeError(f"Error: {res.status_code}")
	info = res.json()
	for k, v in info.items():
		print(f"{k}: {v}")

