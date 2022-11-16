import csv
import datetime
import requests
import V1_get_Authorization


import client_overview_prod_jsonlist
data1 = client_overview_prod_jsonlist.prod
import client_overview_V3_jsonlist
data2 = client_overview_V3_jsonlist.staging

Authorization = V1_get_Authorization.get_V1Authorization()
header = {'Authorization': Authorization}
proxies = {
    'http': 'http://127.0.0.1:4780',
    'https': 'http://127.0.0.1:4780'
}

def get_difference(key_):
    print(key_)
    f = open('client_overview_log.csv', 'a', encoding='utf-8', newline='')
    csvfile = csv.writer(f)
    for i in range(1,1009):
        if data1[i][key_] != data2[i][key_]:
            while True:
                try:
                    print(key_ + ' : ' + str(data1[i]['name']))
                    url1 = f"https://api.hitalentech.com/api/v1/company/{data1[i]['id']}?type=0"
                    resp = requests.get(url1, headers = header, proxies=proxies)
                    #print(resp.text)
                    break
                except Exception as e:
                    print(e)
                    pass
            try:
                if datetime.datetime.strptime(resp.json()['lastModifiedDate'], '%Y-%m-%dT%H:%M:%SZ') < datetime.datetime.strptime("2022-10-26T00:00:00Z", '%Y-%m-%dT%H:%M:%SZ'):
                    csvfile.writerow([f'{key_}' ,str(data1[i]['name']), data1[i][key_], data2[i][key_]])
                    f.flush()
            except TypeError as e:
                csvfile.writerow([f'{key_}', str(data1[i]['name']), f'{e}'])
                f.flush()
            # except KeyError as e:
            #     csvfile.writerow([f'{key_}', str(data1[i]['name']), '异常数据'])
            #     f.flush()
            # except:
            #     continue




if __name__ == '__main__':


    for k in ['logo', 'name', 'industry', 'website', 'fortuneRank', 'sourceLink', 'businessRevenue', 'staffSizeType',
              'linkedinCompanyProfile', 'crunchbaseCompanyProfile', 'companyClientLevelType', 'active', 'tenantId', 'description',
              's3_link', 'organizationName', 'companyAddresses_primary']:  #'am', 'bd', 'owner', 'oters_adress' , 'type'
        get_difference(k)

