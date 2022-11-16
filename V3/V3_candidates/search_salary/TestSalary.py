import json

import requests
from V3 import getAuthorization
from V3.V3_candidates.search_salary import lang
from V3.V3_candidates.search_salary.exchange_rate import Rate

url = 'https://api-staging.hitalentech.com:8888/talent/api/v3/talents/search?page=1&size=400'

f = open('demo_salary_candidate.txt', 'r', encoding='utf-8')
data = json.load(f)

Authorization = getAuthorization.get_Authorization()
header = {'Authorization' : Authorization}

def tSalary(currencys,timeUnit,min,max):

    currencyn = lang.get_numcurrencyType(currencys)
    rate = Rate()
    usdRateDic = rate.gerUSDRate(header)

    # 修改参数
    data['search'][0]['condition'][0]['value']['data']['gte'] = min
    data['search'][0]['condition'][0]['value']['data']['lte'] = max
    data['search'][0]['condition'][0]['value']['currency'] = currencyn
    data['search'][0]['condition'][0]['value']['timeUnit'] = timeUnit

    # 传参 格式化
    from toHourlyUSD import to_HourlyUSD
    r1 = to_HourlyUSD(currencys, timeUnit, min, max, usdRateDic)
    ushourlymin = r1[0]
    ushourlymax = r1[1]

    #print(json.dumps(data, indent=4 , ensure_ascii= False))
    # 发请求 获取结果列表
    resp = requests.post(url= url, headers= header, json= data)
    print(f'共有 {len(resp.json())} 个结果')

    num = 0
    for i in resp.json():
    # 判断 每个结果中的salary范围是否在请求的范围里

        # 获取 结果中的货币类型
        resultCurrency = lang.get_strcurrencyType(i['currency'])
        resultpayType = i['payType']
        resultgte = i['currentSalary']['gte']
        resultlte = i['currentSalary']['lte']
        # 用exchange_rate 换算货币

        r2 = to_HourlyUSD(resultCurrency,resultpayType,resultgte,resultlte,usdRateDic)
        resultUShourlymin = r2[0]
        resultUShourlymax = r2[1]

        if ushourlymin <= resultUShourlymax and ushourlymax >= resultUShourlymin:
            print('result right:√')
            print(f'传参: {currencys},{timeUnit}, {ushourlymin} - {ushourlymax}')
            print(f'结果: {resultCurrency}, {resultpayType}, {resultgte} - {resultlte}')
            print(f'结果转换/hour [USD]: {resultUShourlymin} - {resultUShourlymax} ')
            print()
        else:
            print('-------------------------------------result wrong!!!')
            print(f'传参: {currencys},{timeUnit}, {ushourlymin} - {ushourlymax}')
            print(f'结果: {resultCurrency}, {resultpayType}, {resultgte} - {resultlte}')
            print(f'结果转换/hour [USD]: {resultUShourlymin} - {resultUShourlymax} ')
            print()
            num += 1
    print(f'{num} wrong results. ')
if __name__ == '__main__':
    tSalary('USD',"HOUR",100, 500)