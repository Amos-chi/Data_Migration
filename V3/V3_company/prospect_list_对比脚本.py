# Time : 2022/11/1 15:26
import csv
from datetime import datetime

import requests

from V3 import getV3ProdAuthorization
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
    url = 'https://api.hitalentech.com/api/v1/companies?type=2'
    resp = requests.get(url, headers = header, proxies = proxies)


    dic_ = {}
    for j in resp.json()['clients']:
        comp = {}
        comp['companyName'] = j['name']
        comp['id'] = j['id']
        comp['industry'] = j['industry']
        saleLeadOwner = []
        estimatedDealTime = []
        accountProgress = []
        serviceTypes = []
        try:
            for s in j['saleLead']:
                for slo in s['saleLeadOwner']:
                    saleLeadOwner.append(slo['firstName'] + ' ' + slo['lastName'])
                estimatedDealTime.append(datetime.strptime(s['estimatedDealTime'],'%Y-%m-%dT%H:%M:%SZ'))
                accountProgress.append(s['accountProgress'])
                for stp in s['serviceTypes']:
                    serviceTypes.append(stp['label'])
        except:
            pass
        comp['saleLeadOwner'] = saleLeadOwner
        comp['estimatedDealTime'] = estimatedDealTime
        comp['accountProgress'] = accountProgress
        comp['serviceTypes'] = serviceTypes
        comp['country'] = j['addresses']
        comp['createdDate'] = datetime.strptime(j['createdDate'],'%Y-%m-%dT%H:%M:%SZ')
        comp['createdBy'] = j['createdBy']


        dic_[j['name']] = comp

    #print(dic_)
    return dic_


def getV3data(name_,V3Authorization):
    null = None

    header = {'Authorization': V3Authorization}
    url = f'https://api-staging.hitalentech.com:8888/company/api/v3/company/prospects/search?mine=false&page=0&size=25'
    payload_ = {"companyName": name_,"serviceTypes":null,"industry":null,"countries":null,"owners":null,"accountProgress":null,"createdBy":null}
    resp = requests.post(url, json= payload_, headers = header, proxies = proxies)



    j = resp.json()[0]
    print(j)
    comp = {}
    comp['companyName'] = j['name']
    comp['id'] = j['id']
    comp['industry'] = j['industry']
    saleLeadOwner = []
    estimatedDealTime = []
    accountProgress = []
    serviceTypes = []
    try:
        for slo in j['salesLeadOwners']:
            saleLeadOwner.append(slo['fullName'])

        for sl in j['salesLeads']:
            estimatedDealTime.append(datetime.strptime(sl['estimatedDealTime'],'%Y-%m-%dT%H:%M:%SZ'))
            accountProgress.append(sl['accountProgress'])
            for stp in sl['companyServiceTypes']:
                serviceTypes.append(stp['label'])
    except Exception as e:
        print(e)
        pass
    comp['saleLeadOwner'] = saleLeadOwner
    comp['estimatedDealTime'] = estimatedDealTime
    comp['accountProgress'] = accountProgress
    comp['serviceTypes'] = serviceTypes

    comp['country'] = j['country']
    comp['createdDate'] = datetime.strptime(j['createdDate'], '%Y-%m-%dT%H:%M:%SZ')
    comp['createdBy'] = j['createdBy']

    #print(comp)
    return comp


if __name__ == '__main__':
    while True:         # 防止启动时因为网络原因中断
        try:
            V1Authorization = V1_get_Authorization.get_V1Authorization()
            V3Authorization = getV3ProdAuthorization.get_Authorization()

            dataV1 = getV1data(V1Authorization)
            #print(dataV1)
            break
        except:
            pass

    f = open('prospect_list_log.csv', 'a', encoding='utf-8', newline='')
    csvFile = csv.writer(f)
    i = 1
    for name in dataV1.keys():
        print(f"{i} : {name}:")
        while True:
            try:
                dataV3 = getV3data(name,V3Authorization)

                if dataV1[name]['companyName'] == dataV3['companyName']:

                    llist = ['saleLeadOwner', 'estimatedDealTime', 'accountProgress', 'serviceTypes']
                    for l in llist:
                        if set(dataV1[name][l]) == set(dataV3[l]):
                            print(f'{dataV3["companyName"]} : {l} pass !!')
                        else:
                            msg = f'{dataV3["companyName"]} : ------------------------------------- {l} wrong'
                            print(msg)
                            csvFile.writerow([
                                f'{dataV3["companyName"]}',f'{l}',f'{dataV1[name][l]}',f'{dataV3[l]}'])
                            f.flush()


                    klist = ['industry', 'country', 'createdBy'] #  'createdDate'不比较, 前端在后端返回的基础上加了8 UI上是正确的
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
