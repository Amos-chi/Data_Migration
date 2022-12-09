import json
import os
from V3 import getV3ProdAuthorization
import requests

'''
    发送请求 创建jobfunction对应的候选人
'''

file_dir = r'E:\Program Files (x86)\PyCharm\Amos-chi\data migration\JobFunction_Migration\V3_talent\uploadJsonData'
duplication_url = r'https://api-staging.hitalentech.com:8888/talent/api/v3/talents/search-by-contacts-and-similarity'
req_url = r'https://api-staging.hitalentech.com:8888/talent/api/v3/talents'

Authorization = getV3ProdAuthorization.get_Authorization()
header = { 'Authorization' : Authorization }

#读取文件列表
files = os.listdir(file_dir)

#循环 获取payload data
for file in files:
    if file.endswith('json'):
        f = open(os.path.join(file_dir,file), 'r', encoding= 'utf-8')
        data = json.load(f)
        #发送请求
        while True:
            try:
                resp = requests.post(req_url, json= data, headers= header)
                print(resp.text)
                break
            except Exception as e:
                print(e)
                continue