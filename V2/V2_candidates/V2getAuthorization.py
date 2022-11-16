import requests

def get_Authorization():
    url = 'https://api-staging.hitalentech.com/api/v1/login'
    user = {
        'username' : 'amos.chi',
        'password' : '123456'
    }

    sission_ = requests.session()
    resp = sission_.post(url, json= user)
    print(resp.json())
    Authorization = "Bearer " + resp.json()['credential']['access_token']
    print(Authorization)
    return Authorization

if __name__ == '__main__':
    get_Authorization()