import requests

url = "http://localhost:5000/users"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)

# ToDo - sa facem o functie cupytest sa rulam testul respectiv
