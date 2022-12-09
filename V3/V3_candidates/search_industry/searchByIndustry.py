import json

import requests

from V3 import getV3ProdAuthorization

Authorization = getV3ProdAuthorization.get_Authorization()
header = {'Authorization' : Authorization,
          'Content-Type': 'application/json',
          'Cookie': 'JSESSIONID=3fa46120-f0f5-4589-b1cc-53480edb3f73'}
url = 'https://api-staging.hitalentech.com:8888/talent/api/v3/talents/search?page=1&size=500'

# 数据模板
f = open('demo_industy.txt', 'r', encoding='utf-8')
data = json.load(f)

ff = open('industy_id_cn.json', 'r', encoding='utf-8')
id_cnPair = json.load(ff)

def searchIndustry(ids_):
    data['search'][0]['condition'][0]['value']['data'] = ids_

    resp = requests.post(url, headers= header, json= data)
    results = resp.json()
    for r in results:
        status = 0
        cns = []
        for i in ids_:
            cns.append(id_cnPair[i])
            for ii in id_cnPair[i]:
                if ii in r['industries']:
                    status = 1
        if status == 0:

            log = open('log.txt', 'a', encoding='utf-8')
            log.write(f'{r["_id"]} not match {cns}\n')

if __name__ == '__main__':
    jsonfile = open('industy_ids.json', 'r', encoding='utf-8')
    dic_ = json.load(jsonfile)
    for k in dic_.keys():
        print(dic_[k])
        while True:
            try:
                searchIndustry(dic_[k])
                break
            except:
                continue