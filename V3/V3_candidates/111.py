import csv
import pandas as pd

# pf = pd.read_csv('talent.csv')
# for index,row in pf.iterrows():
#     pf.loc[index,'detail'] = row['detail'].replace(': ',',').replace('"','')
#     #print(row['detail'].replace(': ',','))
#     print(type(row['detail']))
#     print(type(row['detail'].replace(': ',',')))
#
# pf.to_csv('new.csv', encoding='utf-8', index=0)

def operateCSV():
    f = open('talent.csv', 'r', encoding='utf-8')
    data = csv.reader(f)
    #data = f.readlines()
    for row in data:
        #print(row)
        if ':' in row[4]:
            row[4].replace(': ',',')
            #print(row[4])
    for roww in data:
        print(roww)


if __name__ == '__main__':
    operateCSV()