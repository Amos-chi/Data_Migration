
# 读取模板
import csv
import json

f = open('demo_CreateJob.txt', 'r', encoding='utf-8')
data = json.load(f)

def get_jobFunctionsInfo():
    ff =  open('datasource.csv', 'r', encoding= 'utf-8')
    reader = csv.reader(ff)
    next(reader)

    filedata = {}
    for l in reader:
        filedata[l[0]] = l
    return filedata

def set_data():
    jobfunctionsInfos = get_jobFunctionsInfo()
    jobfunctionid = jobfunctionsInfos.keys()

    # 循环创建json 修改参数
    i = 1
    for id_ in jobfunctionid:
        data['title'] = f'atest jobfunction{id_} - {jobfunctionsInfos[id_][2]}'
        data['jobFunctions'][0]['enumId'] = str(id_)
        i += 11

        fileName = data['title']
        #保存
        f = open(f'uploadJsonData/{fileName}.json', 'w', encoding= 'utf-8')
        f.write(json.dumps(data, indent=4, ensure_ascii= False))
        print(i)
if __name__ == '__main__':
    set_data()