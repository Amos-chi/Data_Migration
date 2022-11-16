# Time : 2022/11/1 15:26
import csv

import requests

from V3 import getAuthorization
import V1_get_Authorization
'''
    直接运行, 不需要改参数
'''
proxies = {
    'http': 'http://127.0.0.1:4780',
    'https': 'http://127.0.0.1:4780'
}

def getV1data(V1Authorization):

    header = {'Authorization': V1Authorization}
    url = 'https://api.hitalentech.com/api/v1/companies?type=0'
    resp = requests.get(url, headers = header, proxies = proxies)


    dic_ = {}
    for j in resp.json()['clients']:
        comp = {}
        comp['companyName'] = j['name']
        comp['id'] = j['id']
        comp['openJobs'] = j['numOfOpenJobs']
        comp['contacts'] = j['numOfContacts']
        comp['level'] = j['type']
        serviceType = []
        try:
            for s in j['saleLead']:
                for ss in s['serviceTypes']:
                    serviceType.append(ss['label'])
        except:
            pass
        comp['serviceType'] = serviceType
        comp['status'] = str(j['active'])
        comp['industry'] = j['industry']
        comp['country'] = j['addresses']
        comp['createdBy'] = j['createdBy']


        dic_[j['name']] = comp

    #print(dic_)
    return dic_


def getV3data(name_,V3Authorization):
    null = None

    header = {'Authorization': V3Authorization}
    url = f'https://api-staging.hitalentech.com:8888/company/api/v3/company/clients/search?mine=false&page=0&size=25'
    payload_ = {"companyName":f"{name_}","accountManagers":null,"companyClientLevelType":null,"serviceTypes":null,"active":null,"industry":null,"countries":null}
    resp = requests.post(url, json= payload_, headers = header, proxies = proxies)



    j = resp.json()[0]
    print(j)
    comp = {}
    comp['companyName'] = j['name']
    comp['openJobs'] = j['openJobAmount']
    comp['contacts'] = j['contactAmount']
    comp['level'] = j['companyClientLevelType']
    serviceType = []
    try:
        for c in j['companyServiceTypes']:
            serviceType.append(c['label'])
    except:
        pass
    comp['serviceType'] = serviceType
    comp['status'] = str(j['active'])
    comp['industry'] = j['industry']
    comp['country'] = j['country']
    comp['createdBy'] = j['createdBy']

    #print(comp)
    return comp


if __name__ == '__main__':
    while True:
        try:
            V1Authorization = V1_get_Authorization.get_V1Authorization()
            V3Authorization = getAuthorization.get_Authorization()

            dataV1 = getV1data(V1Authorization)
            break
        except:
            pass

    f = open('client_list_log.csv', 'a', encoding='utf-8', newline='')
    csvFile = csv.writer(f)

    i = 1
    for name in dataV1.keys():
        print(f"{i} : {name}:")
        while True:
            try:
                dataV3 = getV3data(name,V3Authorization)

                if dataV1[name]['companyName'] == dataV3['companyName']:

                    if set(dataV1[name]['serviceType']) == set(dataV3['serviceType']):
                        print(f'{dataV3["companyName"]} : serviceType pass !!')
                    else:
                        msg = f'{dataV3["companyName"]} : ------------------------------------- serviceType wrong'
                        print(msg)
                        csvFile.writerow([
                            f'{dataV3["companyName"]}','serviceType',f'{dataV1[name]["serviceType"]}',f'{dataV3["serviceType"]}'])
                        f.flush()


                    klist = ['openJobs', 'contacts', 'level', 'status', 'industry', 'country']
                    #klist = ['createdBy']
                    for k in klist:
                        if dataV1[name][k] == dataV3[k]:
                            print(f'{dataV3["companyName"]} : {k} pass !!')
                        else:
                            msg = f'{dataV3["companyName"]} : ------------------------------------- {k} wrong'
                            print(msg)
                            csvFile.writerow([f'{dataV3["companyName"]}',f'{k}',f'{dataV1[name][k]}',f'{dataV3[k]}'])
                            f.flush()

                print()
                i += 1
                break
            except IndexError:
                print(f'可能没有公司: {name}')
                csvFile.writerow([f'{name}','数据缺失'])
                f.flush()
                break
            except Exception as e:
                print(e)