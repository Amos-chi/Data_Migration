import requests
import json

url = "https://api-staging.hitalentech.com/api/v2/talents/search"

payload = json.dumps({
  "condition": "{\"and\":[{\"or\":[{\"location\":\"Wuhan\"}]}]}",
  "pageSize": 600,
  "pageNumber": 1,
  "module": "CANDIDATE",
  "timezone": "Asia/Shanghai",
  "initialSearch": False
})
headers = {
  'Authorization': 'Bearer 297831fa-cec5-41de-8087-10b9f3d6a00b',
  'Content-Type': 'application/json',
  'Cookie': 'JSESSIONID=3fa46120-f0f5-4589-b1cc-53480edb3f73; JSESSIONID=3fa46120-f0f5-4589-b1cc-53480edb3f73'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)