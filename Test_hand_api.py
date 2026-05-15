



import requests


URL = "http://localhost:8001/api/v1/contents"

payload = {"username" : "WetsGrow"}
response = requests.get(URL, payload)
print("Заголовки", response.headers)
response.raise_for_status()
#print(response.headers)
print(response.json())
print(response.content)