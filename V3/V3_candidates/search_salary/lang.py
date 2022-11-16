currency = {
    0 : ['USD','usd'],
    1 : ['CNY','cny','rmb'],
    2 : ['EUR','cny'],
    3 : ['CAD','cad'],
    4 : ['GBP','gbp']
}

def get_numcurrencyType(str_):
    for i in currency.keys():
        if str_ in currency[i]:
            return i

def get_strcurrencyType(num_):

    return currency[num_][0]

if __name__ == '__main__':
    print(get_numcurrencyType('rmb'))