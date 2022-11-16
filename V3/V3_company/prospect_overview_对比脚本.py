import csv
import datetime
import requests
import V1_get_Authorization

from V3.V3_company import prospect_overview_V3_jsonlist, prospect_overview_Prod_jsonlist

data1 = prospect_overview_Prod_jsonlist.prod

data2 = prospect_overview_V3_jsonlist.staging

while True:
    try:
        Authorization = V1_get_Authorization.get_V1Authorization()
        break
    except:
        pass


header = {'Authorization': Authorization}
proxies = {
    'http': 'http://127.0.0.1:4780',
    'https': 'http://127.0.0.1:4780'
}

def get_difference(key_):
    print(key_)
    f = open('prospect_overview_log.csv', 'a', encoding='utf-8', newline='')
    csvfile = csv.writer(f)
    for i in range(1,840):
        if type(data1[i][key_]) is str:
            if data1[i][key_] != data2[i][key_]:
                print(f'{data1[i]["companyName"]} : {key_} : {data1[i][key_]} : {data2[i][key_]}')
                csvfile.writerow([f'{data1[i]["companyName"]}',f'{data1[i]["id"]}',f'{key_}',f'{data1[i][key_]}',f'{data2[i][key_]}'])
                f.flush()
                # while True:
                #     try:
                #         print(key_ + ' : ' + str(data1[i]['companyName']))
                #         url1 = f"https://api.hitalentech.com/api/v1/company/{data1[i]['id']}?type=0"
                #         resp = requests.get(url1, headers = header, proxies=proxies)
                #         #print(resp.text)
                #         break
                #     except Exception as e:
                #         print(e)
                #         pass
                # try:
                #     if datetime.datetime.strptime(resp.json()['lastModifiedDate'], '%Y-%m-%dT%H:%M:%SZ') < datetime.datetime.strptime("2022-10-26T00:00:00Z", '%Y-%m-%dT%H:%M:%SZ'):
                #         csvfile.writerow([f'{key_}' ,str(data1[i]['companyName']), data1[i][key_], data2[i][key_]])
                #         f.flush()
                # except TypeError as e:
                #     csvfile.writerow([f'{key_}', str(data1[i]['companyName']), f'{e}'])
                # f.flush()

        elif type(data1[i][key_]) == list:
            if set(data1[i][key_]) != set(data2[i][key_]):
                print(f'{data1[i]["companyName"]} : {key_} : {data1[i][key_]} : {data2[i][key_]}')
                csvfile.writerow([f'{data1[i]["companyName"]}', f'{data2[i]["id"]}', f'{key_}', f'{data1[i][key_]}', f'{data2[i][key_]}'])
                f.flush()
                # while True:
                #     try:
                #         print(key_ + ' : ' + str(data1[i]['companyName']))
                #         url1 = f"https://api.hitalentech.com/api/v1/company/{data1[i]['id']}?type=0"
                #         resp = requests.get(url1, headers = header, proxies=proxies)
                #         #print(resp.text)
                #         break
                #     except Exception as e:
                #         print(e)
                #         pass
                # try:
                #     if datetime.datetime.strptime(resp.json()['lastModifiedDate'], '%Y-%m-%dT%H:%M:%SZ') < datetime.datetime.strptime("2022-10-26T00:00:00Z", '%Y-%m-%dT%H:%M:%SZ'):
                #         csvfile.writerow([f'{key_}' ,str(data1[i]['companyName']), data1[i][key_], data2[i][key_]])
                #         f.flush()
                # except TypeError as e:
                #     csvfile.writerow([f'{key_}', str(data1[i]['companyName']), f'{e}'])
                # f.flush()





if __name__ == '__main__':


    for k in ['companyName', 'industry', 'website', 'fortuneRank', 'businessRevenue', 'staffSizeType',
              'linkedinCompanyProfile', 'crunchbaseCompanyProfile',
              'saleLeadOwners', 'clientContact', 'estimatedDealTime', 'accountProgress',
              'serviceTypeNames', 'leadSource', 'teamMembers']:  #'am', 'bd', 'owner', 'oters_adress' , 'type','logo',
        get_difference(k)

