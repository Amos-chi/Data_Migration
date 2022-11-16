# Time : 2022/11/1 10:04
from V3 import V3_getActiveUser, getAuthorization

null = None

proxies = {
    'http': 'http://127.0.0.1:4780',
    'https': 'http://127.0.0.1:4780'
}

def V3():
    url = 'https://api-staging.hitalentech.com:8888/report/api/v3/report/dormant/applications'
    payload = {"teamId":[],"userId":"","status":"SUBMIT_TO_JOB"}
    Authorization = getAuthorization.get_Authorization()
    header = {'Authorization': Authorization}

    import requests
    resp = requests.post(url, json=payload, headers=header, proxies=proxies)
    print(f'resp.status_code : {resp.status_code}')
    print(f'len(resp.json()) : {len(resp.json())}\n')

    list1 = []
    activeUsers = V3_getActiveUser.getactiveUsers()
    for j in resp.json():
        if j['id'] in activeUsers.keys():
            list1.append(j['count'])

    print(list1)

    count = 0
    for i in list1:
        count += i

    print(count)

def V2():
    url = 'https://api.hitalentech.com/api/v1/report/dormant/applications?status=Submitted'

    header = {
        'authorization': 'Bearer 61847671-a0e4-4210-b7fc-eefb50c2460a'}

    import requests
    resp = requests.get(url, headers=header, proxies=proxies)
    print(f'resp.status_code : {resp.status_code}')
    print(f'len(resp.json()) : {len(resp.json())}\n')

    list1 = []
    for j in resp.json():
        list1.append(j['count'])

    print(list1)

    count = 0
    for i in list1:
        count += i

    print(count)

if __name__ == '__main__':
    V3()