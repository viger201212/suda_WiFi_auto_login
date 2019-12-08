import base64
import logging
import time
from typing import Dict

import requests

logging.basicConfig(level=logging.DEBUG)

# config area
# baseurl = "1d.suda.edu.cn"
password = b"xxxxxx"  # 填入你的密码
username = "xxxxxxxx"  # 填入你的学号如18123456
method = "1"  # 填入登录的方式. 1 为校园网; 2 为中国移动; 3 为中国移动测试

domain: Dict[str, str] = {"1": "", "2": "cmcc-suzhou", "3": "CMCC"}
headers = {'Host': '1d.suda.edu.cn',
           'Proxy-Connection': 'keep-alive',
           'Content-Length': '73',
           'Accept': 'application/json, text/javascript, */*; q=0.01',
           'Origin': 'http://1d.suda.edu.cn',
           'Connection': 'keep-alive',
           'X-Requested-With': 'XMLHttpRequest',
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/80.0.3956.0 Safari/537.36 Edg/80.0.328.0',
           'DNT': '1',
           'Content-Type': 'application/x-www-form-urlencoded',
           'Referer': 'http://1d.suda.edu.cn/',
           'Accept-Encoding': 'gzip, deflate',
           'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
           'Cookie': 'sunriseUsername=; sunriseDomain=campus; think_language=zh-CN; PHPSESSID='}
data = {'username': username,
        'domain': domain,
        'password': base64.b64encode(password),
        'enablemacauth': '0'}
r = requests.request("post", "http://1d.suda.edu.cn/index.php/index/login", headers=headers, data=data)
while True:
    if r.status_code == 200:
        print(r.json()["info"])
        break
        # 当访问网关成功时, 输出登录情况, 退出程序
    else:
        time.sleep(1)
        r = requests.request("post", "http://1d.suda.edu.cn/index.php/index/login", headers=headers, data=data)
        logging.debug("请连接到suda_WiFi, 一秒后自动重试")
        # 访问网关失败时, 等待一秒后重试
        # TODO: 优化循环判断
input("Press enter to exit ;)")
