
# 读取模板
import csv
import json

f = open('demo_CreateTalent.txt', 'r', encoding= 'utf-8')
data = json.load(f)

def get_jobFunctionsInfo():
    f =  open('datasource.csv', 'r', encoding= 'utf-8')
    reader = csv.reader(f)

    data = {}
    for l in reader:
        #print(l)
        if l[0] == '原id':
            continue
        else:
            data[l[0]] = l
    return data

def set_data():
    jobfunctionsInfos = get_jobFunctionsInfo()
    jobfunctionid = jobfunctionsInfos.keys()

    # 循环创建json 修改参数
    i = 1
    for id_ in jobfunctionid:
        data['jobFunctions'][0]['enumId'] = id_
        data['firstName'] = f'atest jobfunction{id_} - '
        data['lastName'] = jobfunctionsInfos[id_][2]
        data['contacts'][0]['contact'] = str(17764210001 + i)
        i += 1

        fileName = data['firstName'] + data['lastName']
        #保存
        f = open(f'uploadJsonData/{fileName}.json', 'w', encoding= 'utf-8')
        f.write(json.dumps(data, indent=4))
        print(i)
if __name__ == '__main__':
    set_data()