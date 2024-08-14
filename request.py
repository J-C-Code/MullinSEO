import requests
import json

url = "https://api.indexnow.org/indexnow"
payload = {
  "host": "getplumbing.org",
  "key": "508d95872abe40fa8ca2ccf8a5b26e2d",
  "keyLocation": "https://getplumbing.org/508d95872abe40fa8ca2ccf8a5b26e2d.txt",
  "urlList": [
    "https://getplumbing.org/",
    "https://getplumbing.org/residential",
    "https://getplumbing.org/commercial",
    "https://getplumbing.org/emergency"
  ]
}
headers = {"Content-Type": "application/json; charset=utf-8"}

response = requests.post(url, data=json.dumps(payload), headers=headers)

print(response.status_code)
print(response.text)
