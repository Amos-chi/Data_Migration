import csv
import json

# 中国地区
# f = open('../location_cn', 'r', encoding='utf-8')
# data = f.read()
# lines = data.replace('"','').split('\n')
# dic = {}
# for line in lines:
#     l = line.split(';')
#     dic[l[3]] = l[2]
#     dic[l[1]] = l[0]
#
# f = open('location_cn.json','w', encoding='utf-8')
# f.write(json.dumps(dic, indent=4, ensure_ascii=False))

# 外国地区
# f = open('../location_en.txt', 'r', encoding='utf-8')
# str_ = f.read()
# lines = str_.split('\n')
# dic = {}
# for line in lines:
#     l = line.strip().split('	')
#     dic[l[1]] = l[0]
#
#     f = open('location_en.json','w', encoding='utf-8')
#     f.write(json.dumps(dic, indent=4, ensure_ascii=False))

# 中国地区 按省归纳市
# f = open('../location_cn', 'r', encoding='utf-8')
# data = f.read()
# lines = data.replace('"','').split('\n')
# dic = {}
# for line in lines:
#     l = line.split(';')
#     if l[0] not in dic.keys():
#         dic[l[0]] = [[l[3],l[2]]]
#     else:
#         dic[l[0]].append([l[3],l[2]])
# f = open('location_cn.json', 'w', encoding='utf-8')
# f.write(json.dumps(dic, ensure_ascii=False))

