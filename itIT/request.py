import requests

url = 'http://localhost:5000/api'

r = requests.post(url, json={'y_target':1,})
print(r.json())