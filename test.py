import requests

# Test Website:
r = requests.get('http://localhost:5000')
print(r.text)
r = requests.post('http://localhost:5000')
print(r.text)

# Test API:
r = requests.get('http://localhost:5000/api')
print(r.text)
