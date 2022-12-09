from V3 import getV3ProdAuthorization
from V3.V3_candidates.search_salary.exchange_rate import Rate

rate = Rate()

def to_HourlyUSD(currencys,timeUnit,min,max,header):

    # 获取 传参中的货币类型
    if timeUnit in ['DAY', 'DAILY']:
        hourlymin = min /8
        hourlymax = max /8
        if currencys == 'USD':
            ushourlymin = hourlymin
            ushourlymax = hourlymax
        else:
            r = rate.getUSD(currencys,hourlymin,hourlymax,header)
            ushourlymin = r[0]
            ushourlymax = r[1]

    elif timeUnit in ['WEEK', 'WEEKLY'] :
        hourlymin = min /40
        hourlymax = max /40
        if currencys == 'USD':
            ushourlymin = hourlymin
            ushourlymax = hourlymax
        else:
            r = rate.getUSD(currencys,hourlymin,hourlymax,header)
            ushourlymin = r[0]
            ushourlymax = r[1]

    elif timeUnit in ['MONTH', 'MONTHLY']:
        hourlymin = min*12 /2080
        hourlymax = max*12 /2080
        if currencys == 'USD':
            ushourlymin = hourlymin
            ushourlymax = hourlymax
        else:
            r = rate.getUSD(currencys,hourlymin,hourlymax,header)
            ushourlymin = r[0]
            ushourlymax = r[1]

    elif timeUnit in ['YEAR', 'YEARLY']:
        hourlymin = min /2080
        hourlymax = max /2080
        if currencys == 'USD':
            ushourlymin = hourlymin
            ushourlymax = hourlymax
        else:
            r = rate.getUSD(currencys,hourlymin,hourlymax,header)
            ushourlymin = r[0]
            ushourlymax = r[1]

    else:
        hourlymin = min
        hourlymax = max
        if currencys == 'USD':
            ushourlymin = hourlymin
            ushourlymax = hourlymax
        else:
            r = rate.getUSD(currencys,hourlymin,hourlymax,header)
            ushourlymin = r[0]
            ushourlymax = r[1]

    #print(ushourlymin,ushourlymax)
    return (ushourlymin,ushourlymax)

if __name__ == '__main__':
    Authorization = getV3ProdAuthorization.get_Authorization()
    header = {'Authorization': Authorization}
    to_HourlyUSD('CAD', 'HOUR', 100, 1000, header)