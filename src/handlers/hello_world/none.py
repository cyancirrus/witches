import json
import requests

# url = "http://127.0.0.1:3000/goddess/helloworld"
# url = " https://mikqk5fn4m.execute-api.us-east-1.amazonaws.com/Prod/goddess/helloworld"

url = "https://mikqk5fn4m.execute-api.us-east-1.amazonaws.com/Prod/demo/helloworld"
 
r = requests.get(url,
    headers = {
        'Accept' : 'text/json'
    }
)

print(r.text)
print(r.status_code)

