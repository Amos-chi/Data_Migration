# Time : 2022/11/2 15:15
import requests

from V3 import getV3ProdAuthorization

proxies = {
    'http': 'http://127.0.0.1:4780',
    'https': 'http://127.0.0.1:4780'
}
url = 'https://api-staging.hitalentech.com:8888/user/api/v3/users/all-brief'
Authorization = getV3ProdAuthorization.get_Authorization()
header = {'Authorization' : Authorization}
def getactiveUsers():
    while True:
        try:
            resp = requests.get(url, headers=header, proxies=proxies)
            print(resp.status_code)
            break
        except Exception as e:
            print(e)
    activeUsers = {}
    for j in resp.json():
        if j['activated'] == True:
            activeUsers[j['id']] = j['fullName']

    print(len(activeUsers))
    return activeUsers

if __name__ == '__main__':
    getactiveUsers()