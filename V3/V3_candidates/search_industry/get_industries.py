import json

import requests

from V3 import getAuthorization

Authorization = getAuthorization.get_Authorization()
header = {'Authorization' : Authorization}
url = 'https://api-staging.hitalentech.com:8888/job/api/v3/dict/industries?type=EN'
resp = requests.get(url, headers= header)

resulets = resp.json()
dict = {}
id_cn = {}
for r in resulets:
    if r.get('children'):
        list_ = []
        list_.append(r['id'])
        id_cn[r['id']] = [r['label'],r['labelCn']]
        for i in r.get('children'):
            id_cn[i['id']] = [i['label'],i['labelCn']]
            list_.append(i['id'])
            dict[i['id']] = [i['id']]
        dict[list_[0]] = list_

    else:
        id_cn[r['id']] = [r['label'],r['labelCn']]
        dict[r["id"]] = [r["id"]]
ids_ = json.dumps(dict, indent=4)
id_cns = json.dumps(id_cn, indent=4, ensure_ascii= False)
f = open('industy_ids.json', 'w', encoding='utf-8')
f.write(ids_)
f = open('industy_id_cn.json', 'w', encoding='utf-8')
f.write(id_cns)