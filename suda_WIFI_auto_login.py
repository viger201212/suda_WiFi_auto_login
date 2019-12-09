import base64
import json
import logging
import time
from typing import Dict

import requests

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)

    # config area
    # baseurl = "1d.suda.edu.cn"
    with open('config.json') as fp:
        config = json.load(fp=fp)
    password = bytes(config["password"], encoding="utf-8")
    username = config["username"]
    method = config["method"]

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
            'domain': domain[method],
            'password': base64.b64encode(password),
            'enablemacauth': '0'}
    while True:
        r = requests.request("post", "http://1d.suda.edu.cn/index.php/index/login", headers=headers, data=data)
        if r.status_code == 200:
            print(r.json()["info"])
            break
            # 当访问网关成功时, 输出登录情况, 退出程序
        else:
            time.sleep(1)
            logging.debug("请连接到suda_WiFi, 一秒后自动重试")
            # 访问网关失败时, 等待一秒后重试
    input("Press enter to exit ;)")
