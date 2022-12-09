import requests

proxies = {
   'http': 'http://127.0.0.1:4780',
   'https': 'http://127.0.0.1:4780'
}

def get_Authorization():
    url = 'https://apiv3.hitalentech.com/user/api/v3/login'
    user = {
        # 'username' : 'private4',
        # 'password' : 'ipg@95054',
        'username': 'AMOS.TEST1',
        'password' : 'a123456',
        'timeZone': "Asia/Shanghai",
        'userAgent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"
    }

    #sission_ = requests.session()
    while True:
        try:
            resp = requests.post(url, json= user, proxies=proxies)
            break
        except Exception as e:
            print(e)
    Authorization = "Bearer " + resp.json()['credential']['access_token']
    #print(Authorization)
    return Authorization

if __name__ == '__main__':
    get_Authorization()