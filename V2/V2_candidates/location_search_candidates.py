import json

import requests

import V2getAuthorization



Authorization = V2getAuthorization.get_Authorization()
url = 'https://api-staging.hitalentech.com/api/v2/talents/search'

header = {
  'Authorization': Authorization,
  'Content-Type': 'application/json',
  'Cookie': 'JSESSIONID=3fa46120-f0f5-4589-b1cc-53480edb3f73; JSESSIONID=3fa46120-f0f5-4589-b1cc-53480edb3f73'
}

# 传参模板
# f = open('demo_talent.txt', 'r', encoding= 'utf-8')
# data = json.loads(f.read())

# 城市中英文名, 省市对应关系
ff = open('location_cn.json', 'r', encoding='utf-8')
locations = json.load(ff)

# 遍历文件中的省, 和每个省下所有的城市
for province in locations.keys():
    # 城市的中英文名为一组, 查询完后比对结果
    for locationPair in locations[province]:
        result = []
        for l in locationPair:
            # 将传参中的location 换成要查询的城市中/英文名
            f = open('demo_talent.txt', 'r', encoding='utf-8')
            data = json.loads(f.read())
            data['condition'] = data['condition'].replace('wuahn', l)
            print(f'------------------------------------------------------------{l}')
            print(data)
            # 避免网络原因造成的报错造成程序中断
            while True:
                try:
                    resp = requests.post(url, data = json.dumps(data), headers = header)
                    print(resp.content)
                    break
                #print(json.dumps(resp.json(), indent=4, ensure_ascii=False))
                except Exception as e:
                    print(e)
                    continue

            result.append(resp.json())

        # 存放英文名查询到的talentid
        try:
            list1 = []
            for j in result[0]:
                list1.append(j['_id'])

            # 存放中文名查询到的talentid
            list2 = []
            for j in result[1]:
                list2.append(j['_id'])

        except TypeError:
            log = open('log.txt', 'a', encoding='utf-8')
            log.write(f'{locationPair} : {resp.status_code}\n')
            log.close()
            continue

        # 存放有问题的talentid
        problem1_ = []
        for l1 in list1:
            if l1 not in list2:
                print(f'{locationPair[0]}" 的 {l1} 不在 "{locationPair[1]}" 的返回列表里')
                problem1_.append(l1)

        # 如果长度不为0 就写入log/表格
        if len(problem1_) > 0 :
            # log = open('log.txt', 'a', encoding='utf-8')
            # log.write(f'"{locationPair[0]}"有 "{locationPair[1]}"没有的结果: {problem1_}\n')
            # log.close()

            newlist = [str(x) for x in problem1_]
            liststr = "，".join(newlist)
            csv_ = open('talent.csv', 'a', encoding='utf-8', newline='')
            csv_.write(f'{locationPair[0]},{len(list1)},{locationPair[1]},{len(list2)},location中文名能搜到 英文名搜索不到,{liststr},{locationPair[0]} 有 {locationPair[1]} 没有的结果\n')
            csv_.close()



        problem2_ = []
        for l2 in list2:
            if l2 not in list1:
                print(f'{locationPair[1]}" 的  {l2} 不在 "{locationPair[0]}"的返回列表里')
                problem2_.append(l2)

        if len(problem2_) > 0:
            # log = open('log.txt', 'a', encoding='utf-8')
            # log.write(f'"{locationPair[1]}"有 "{locationPair[0]}"没有的结果: {problem2_}\n')
            # log.close()

            newlist = [str(x) for x in problem2_]
            liststr = "，".join(newlist)
            csv_ = open('talent.csv', 'a', encoding='utf-8', newline='')
            csv_.write(f'{locationPair[0]},{len(list1)},{locationPair[1]},{len(list2)},location英文名能搜到 中文名搜索不到,{liststr},{locationPair[1]} 有 {locationPair[0]} 没有的结果\n')
            csv_.close()