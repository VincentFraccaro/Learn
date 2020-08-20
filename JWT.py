import json
import requests
# edit bearer to what you get from requests.get
auth_token = {'Accept':'application/json', 'Authorization':'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImFkbWluIiwiaWF0IjoxNTk3ODMxMjAzLCJleHAiOjE1OTc5MTc2MDN9.1xPbqhiYl6iXly4jE0_LSwMsQm5mJBv_xjJ-XC2VUgg'}
host = input("What is Host IP: ")
port = input("What is Host Port: ")
url = "http://" + host + ":" + port
# edit for your own creds
r = requests.post(url + "/login", json={'username':'admin', 'password':'Zk6heYCyv6ZE9Xcg'})
print(json.dumps(r.json(), indent=4))
r = requests.get(url + "/users", headers=auth_token)
my_json = r.json()
dictionary = json.dumps(my_json, indent=4)
print(dictionary)
# edit to loop through for paremeter you want to lookup
for i in my_json:
	name = i['name']
	nameLogs = requests.get("http://10.10.10.137:3000/users/" + name, headers=auth_token)
	print(nameLogs.json())
	
