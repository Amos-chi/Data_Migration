from enum import Enum

import requests

from V3 import getAuthorization


class Rate():

    def gerUSDRate(self,header):

        url = 'https://api-staging.hitalentech.com:8888/job/api/v3/dict/currency/all'
        resp = requests.get(url,headers = header)
        #print(resp.json())
        dic = {}
        for i in resp.json():
            dic[i['name']] = i['fromUsdRate']
        #print(dic)
        return dic

    def getUSD(self,rtype, min, max, usdRateDic):

        type_ = usdRateDic[rtype]
        nmin = min * type_
        nmax = max * type_
        #print(f'转换结果: {nmin}, {nmax}')
        return nmin, nmax


if __name__ == '__main__':
    rate = Rate()
    rate.gerUSDRate()
    #rate.getUSD('CNY',20000,35000)