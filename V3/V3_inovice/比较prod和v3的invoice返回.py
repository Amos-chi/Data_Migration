# Time : 2022/11/3 10:01
'''

key基本相同 直接比较两个返回的dic

'''
import requests

import V1_get_Authorization
from V3 import getV3ProdAuthorization

proxies = {
    'http': 'http://127.0.0.1:4780',
    'https': 'http://127.0.0.1:4780'
}
pair = {
    0 : 'USD',
    1 : 'CNY',
    2 : 'EUR',
    3 : 'CAD',
    4 : 'GBP',
}
while True:
    try:
        V1Authorization = V1_get_Authorization.get_V1Authorization()
        V3Authorization = getV3ProdAuthorization.get_Authorization()
        V1header = {'Authorization': V1Authorization}
        V3header = {'Authorization': V3Authorization}

        break
    except Exception as e:
        print(e)


def getV1invoice(V1header):
    url = 'https://api.hitalentech.com/api/v1/invoices/?search=&page=0&size=20&sort=&sort=id,desc&status=PAID&status=UNPAID&status=OVERDUE&status=STARTUP_FEE_PAID_USED&status=STARTUP_FEE_PAID_UNUSED&status=STARTUP_FEE_UNPAID_UNUSED&status=VOID'
    resp = requests.get(url, headers= V1header, proxies= proxies)
    print(resp.status_code)

    return resp.json()

def getV3invoice(V3header):
    url = 'https://api-staging.hitalentech.com:8888/finance/api/v3/invoices/?search=&page=0&size=20&sort=&sort=id,desc&status=PAID&status=UNPAID&status=OVERDUE&status=STARTUP_FEE_PAID_USED&status=STARTUP_FEE_PAID_UNUSED&status=STARTUP_FEE_UNPAID_UNUSED'
    resp = requests.get(url, headers=V3header, proxies=proxies)
    print(resp.status_code)

    return resp.json()


if __name__ == '__main__':
    dataV1 = getV1invoice(V1header)
    dataV3 = getV3invoice(V3header)

    list1 = dataV1['elements']
    list3 = dataV3['elements']

    for l in list1:
        l['dueAmount'] = float(int(l['dueAmount']))

    for l in list3:
        l['currency'] = pair[l['currency']]


    for i in range(len(list1)):
        for key in list1[i].keys():
            if list1[i][key] == list1[i][key]:
                print(f'{i} : {key} is ok..')
            else:
                print(f'{i} : {key} ----------------------------------------  wrong')
























