from time import sleep

import requests

from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from V3 import getV3ProdAuthorization

'''
    在cmd 命令行窗口运行: (端口号可以设置任意闲置端口)
    chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\Chromedriver\chromeprofile"
'''

Authorization = getV3ProdAuthorization.get_Authorization()
header = {'Authorization': Authorization}



def get_companyIDs():
    url = 'https://api-staging.hitalentech.com:8888/company/api/v3/company/clients/list?type=0'
    resp = requests.get(url, headers = header)
    IDS = []
    for j in resp.json():
        IDS.append(j['id'])
    print(len(IDS))
    return IDS

def openUrls():
    chrome_options = Options()
    chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

    driver = webdriver.Chrome(options=chrome_options)
    ids = get_companyIDs()
    for i in ids:
        url = f'https://apn-v3-staging.hitalentech.com/companies/detail/{i}/0'
        print(f'opening {i}..')
        driver.get(url)
        # 设置显示等待 以20秒为最大等待时间, 以0.5秒一次的频率更新页面, 直到找到元素 否则报错
        try:
            WebDriverWait(driver, 20, 0.5).until(lambda el: driver.find_element('xpath','//*[text()="Page not found."]'))
            WebDriverWait(driver, 20, 0.5).until(lambda el: driver.find_element('xpath','//*[text()="Company Name"]'))
            print(f'{i} is ok..')
        except Exception as e:
            print(e)
            f = open('log.txt', 'a', encoding= 'utf-8')
            f.write(str(i) + '\n')

if __name__ == '__main__':
    openUrls()