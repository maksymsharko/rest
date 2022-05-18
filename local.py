import requests

res = requests.put("http://127.0.0.1:3001/api/courses/2", {"name": "Igor", "age": 14})
print(res.json())
