# Time : 2022/11/15 17:03

proxies = {
    'http': 'http://127.0.0.1:4780',
    'https': 'http://127.0.0.1:4780'
}
f = open('prospect_list_log.csv','r', encoding='utf-8')
import pandas as pd
csv_ = pd.read_csv(f)
print(type(csv_))

csv_.to_csv('pppppp.csv',mode='w', encoding='utf-8', columns= ['Intellipro Group Inc.'] )