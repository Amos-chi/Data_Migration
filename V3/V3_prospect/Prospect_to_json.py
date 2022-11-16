import json

import requests

from V3 import getAuthorization


def getV1Prospect():
    url = 'https://api.hitalentech.com/api/v1/companies?type=2'
    header = {
        'authorization' : 'Bearer e1be63a5-28b1-4317-8554-d67dd8cd1518'
    }

    resp = requests.get(url, headers= header)
    f = open('V1jsons.py', 'w', encoding= 'utf-8')
    f.write(json.dumps(resp.json(), indent= 4, ensure_ascii=False))

def getV3Prospect():
    Authorization = getAuthorization.get_Authorization()
    header = { 'Authorization' : Authorization }
    url = 'https://api-staging.hitalentech.com:8888/company/api/v3/company/prospects/search?mine=false&page=1&size=600'
    data = {"companyName":None,"accountManagers":None,"companyClientLevelType":None,"serviceTypes":None,"active":None,"industry":None,"countries":None}

    resp = requests.post(url, headers= header, json= data)
    print(resp.content)
    f = open('V3jsons.py', 'w', encoding= 'utf-8')
    f.write(json.dumps(resp.json(), indent= 4, ensure_ascii=False))


if __name__ == '__main__':
    getV3Prospect()