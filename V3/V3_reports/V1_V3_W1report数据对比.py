# Time : 2022/11/14 13:42
import requests

import V1_get_Authorization
from V3 import getV3ProdAuthorization

proxies = {
    'http': 'http://127.0.0.1:4780',
    'https': 'http://127.0.0.1:4780'
}

def getV1data():
    url = 'https://api.hitalentech.com/api/v2/report/p1-pipeline-analytics-by-users?fromDate=2022-09-30T16:00:00.000Z&toDate=2022-10-26T15' \
          ':59:59.999Z&jobCountry=&teamId=&divisionId=&userRole=RECRUITER&jobTypes=CONTRACT&jobTypes=FULL_TIME&jobTypes=PAY_ROLL'
    Authorization = V1_get_Authorization.get_V1Authorization()

    header = {'Authorization': Authorization}

    resp = requests.get(url, headers=header, proxies=proxies)
    j = resp.json()
    data = {}
    for i in j:
        data[i['userName']] = i['appliedCount'] + i['submittedCount'] + i['pipelineUpdateSubmittedCount'] + i[
            'interviewCount'] + i['offeredCount'] + i['offerAcceptedCount'] + i['startedCount']

    return data

def getV3data():
    url = 'https://api-staging.hitalentech.com:8888/report/api/v3/report/p1-pipeline-analytics-by-users'
    payload = {"userRole":"AM","userId":"","jobTypes":["CONTRACT","FULL_TIME","PAY_ROLL"],"fromDate":"2022-09-30T16:00:00.000Z",
               "toDate":"2022-10-26T15:59:59.999Z","teamIds":[],"divisionId":""}
    Authorization = getV3ProdAuthorization.get_Authorization()
    header = {'Authorization': Authorization}
    resp = requests.post(url, headers=header, proxies=proxies, json= payload)
    #print(resp.status_code)
    j = resp.json()
    data = {}
    for i in j:
        data[i['userName']] = i['appliedCount'] + i['submittedCount'] + i['pipelineUpdateSubmittedCount'] + i[
            'interviewCount'] + i['offeredCount'] + i['offerAcceptedCount'] + i['startedCount']

    sum_ = sum([i['interviewCount'] for i in j])
    print(sum_)



    return data



if __name__ == '__main__':
    # v1data = getV1data()
    # print(len(v1data))
    v3data = getV3data()
    #(len(v3data))

    # for k in v1data.keys():
    #     if k not in v3data.keys():
    #         print(k)
    #
    # print('------------------------')
    #
    # for kk in v3data.keys():
    #     if kk not in v1data.keys():
    #         print(kk)

