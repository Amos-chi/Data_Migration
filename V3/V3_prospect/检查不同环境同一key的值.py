import datetime
import json

import requests
from V3 import getV3ProdAuthorization

import V1jsons

data1 = V1jsons.json_

data2 = V1jsons.json_

#Authorization = getAuthorization.get_Authorization()
header = {'Authorization': 'Bearer e1be63a5-28b1-4317-8554-d67dd8cd1518',
          'Cookie': 'JSESSIONID=e8800732-d6b2-4d35-9d6d-414b4b0d60a1; JSESSIONID=e8800732-d6b2-4d35-9d6d-414b4b0d60a1'
          }
payload={}
def get_difference(key_):
    for i in range(1,2000):
        print(i)
        if data1[i][key_] != data2[i][key_]:
            while True:
                try:
                    print(key_ + ' : ' + str(data1[i]['id']))
                    url1 = f"https://api.hitalentech.com/api/v1/company/{data1[i]['id']}?type=0"
                    resp = requests.get(url1, headers = header, data = payload)
                    #print(resp.text)
                    break
                except:
                    continue
            try:
                if datetime.datetime.strptime(resp.json()['lastModifiedDate'], '%Y-%m-%dT%H:%M:%SZ') < datetime.datetime.strptime("2022-09-20T00:00:00Z", '%Y-%m-%dT%H:%M:%SZ'):
                    print(str(data1[i]['id']))
                    f = open('log_1.txt', 'a', encoding= 'utf-8')
                    f.write(key_ + ' : ' + str(data1[i]['id']) + '\n')
            except TypeError as e:
                f = open('log_1.txt', 'a', encoding='utf-8')
                f.write(key_ + ' : ' + str(data1[i]['id']) + '异常数据' + '\n')
            except KeyError as e:
                f = open('log_1.txt', 'a', encoding='utf-8')
                f.write(key_ + ' : ' + str(data1[i]['id']) + '异常数据' + '\n')
            except:
                continue




if __name__ == '__main__':
    # for k in ['logo', 'name', 'industry', 'website', 'fortuneRank', 'sourceLink', 'businessRevenue', 'staffSizeType',
    #           'linkedinCompanyProfile', 'crunchbaseCompanyProfile', 'type', 'companyClientLevelType', 'active', 'tenantId', 'description',
    #           's3_link', 'organizationName', 'am', 'bd', 'owner', 'companyAddresses_primary', 'oters_adress']:
    #     get_difference(k)
    #get_difference('oters_adress')
    print(data2)
