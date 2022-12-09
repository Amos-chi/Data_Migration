import json
import os
from V3 import getV3ProdAuthorization
import requests

'''
    发送请求 创建jobfunction对应的职位
'''

file_dir = r'E:\Program Files (x86)\PyCharm\Amos-chi\data migration\JobFunction_Migration\V3_job\uploadJsonData'
req_url = 'https://api-staging.hitalentech.com:8888/job/api/v3/jobs'

Authorization = getV3ProdAuthorization.get_Authorization()
header = {
    'Authorization':  Authorization,
    'Content-Type': 'application/json'
          }
print(header)
#读取文件列表
files = os.listdir(file_dir)

#循环 获取payload data
for file in files:
    if file.endswith('json'):
        f = open(os.path.join(file_dir,file), 'r', encoding= 'utf-8')
        data = json.load(f)
        #print(data)
        #发送请求
        while True:
            try:
                resp = requests.post(req_url, json= data, headers= header)
                print(resp.content)
                break
            except Exception as e:
                print(e)
                continue