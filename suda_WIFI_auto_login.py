import base64
import logging
import time

import requests

logging.basicConfig(level=logging.DEBUG)
# baseurl = "1d.suda.edu.cn"
password = b"xxxxxx"  # 填入你的密码
username = "xxxxxxxx"  # 填入你的学号如18123456
headers = {'Host': '1d.suda.edu.cn',
           'Proxy-Connection': 'keep-alive',
           'Content-Length': '73',
           'Accept': 'application/json, text/javascript, */*; q=0.01',
           'Origin': 'http://1d.suda.edu.cn',
           'X-Requested-With': 'XMLHttpRequest',
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3956.0 Safari/537.36 Edg/80.0.328.0',
           'DNT': '1',
           'Content-Type': 'application/x-www-form-urlencoded',
           'Referer': 'http://1d.suda.edu.cn/',
           'Accept-Encoding': 'gzip, deflate',
           'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
           'Cookie': 'sunriseUsername=; sunriseDomain=campus; think_language=zh-CN; PHPSESSID='}
data = {'username': username,
        'domain': '',
        'password': base64.b64encode(password),
        'enablemacauth': '0'}
r = requests.request("post", "http://1d.suda.edu.cn/index.php/index/login", headers=headers, data=data)
while r.status_code != 200:
    time.sleep(10000)
    logging.debug("login failed, retrying")
    r = requests.request("post", "http://1d.suda.edu.cn/index.php/index/login", headers=headers, data=data)
print(r.json()["info"])
