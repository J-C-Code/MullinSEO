import requests
import json

url = "https://api.indexnow.org/indexnow"
payload = {
  "host": "www.getplumbing.org",
  "key": "508d95872abe40fa8ca2ccf8a5b26e2d",
  "keyLocation": "https://www.getplumbing.org/508d95872abe40fa8ca2ccf8a5b26e2d.txt",
  "urlList": [
    "https://www.getplumbing.org/",
    "https://www.getplumbing.org/residential",
    "https://www.getplumbing.org/commercial",
    "https://www.getplumbing.org/emergency"
  ]
}
headers = {"Content-Type": "application/json; charset=utf-8"}

response = requests.post(url, data=json.dumps(payload), headers=headers)

print(response.status_code)
print(response.text)
