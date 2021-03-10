import json
import requests

url = "http://127.0.0.1:3000/goddess/helloworld"

 
r = requests.get(url,
    headers = {
        'Accept' : 'text/json'
    },
    json = {
        "hello":"is this still good"
    }
)

print(r.text)
print(r.status_code)

