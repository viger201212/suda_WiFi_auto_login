import base64
import json
import logging
import time
from typing import Dict
import socket
pcname = socket.getfqdn(socket.gethostname( ))
pcip = socket.gethostbyname(pcname)
pcip = socket.gethostbyname_ex(pcname)[2][1]

print(pcip)

import requests

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)

    # config area
    # baseurl = "http://10.9.1.3:801/eportal/?c=Portal&a=login&callback=dr1004&login_method=1&user_account=%2C0%2C1827406006&user_password=llhw201212&wlan_user_ip=10.70.87.222&wlan_user_ipv6=&wlan_user_mac=000000000000&wlan_ac_ip=221.178.234.23&wlan_ac_name=&jsVersion=3.3.3&v=6050"
    with open('config.json') as fp:
        config = json.load(fp=fp)
    password = config["password"]
    username = config["username"]
    method = config["method"]

    domain: Dict[str, str] = {"1": "1", "2": "cmcc-suzhou", "3": "CMCC"}
    headers = {}
    if method == "3":
        username = username + "@zgyd"

    while True:
        r = requests.request("get", "http://10.9.1.3:801/eportal/?c=Portal&a=login&callback=dr1003&login_method=1&user_account={1}&user_password={2}&wlan_user_ip={3}&wlan_user_ipv6=&wlan_user_mac=000000000000&wlan_ac_ip=&wlan_ac_name=&jsVersion=3.3.3&v=7546".format(method, username, password, "000.000.000.000"), headers=headers)
        if r.status_code == 200:
            try:
                response = r.content.decode("utf-8")
                response = response.replace("dr1003(", "")
                response = response.replace(")", "")
                # print(response)
                r = json.loads(response)
                if r["result"] != "1":
                    print(r["msg"])
                    print(r["ret_code"])
                    break
                print(r["msg"])
                break
            except Exception as e:
                print(e)
                time.sleep(1)
                logging.debug("请连接到suda_WiFi, 一秒后自动重试")
                continue

            # 当访问网关成功时, 输出登录情况, 退出程序
        else:
            time.sleep(1)
            logging.debug("请连接到suda_WiFi, 一秒后自动重试")
            # 访问网关失败时, 等待一秒后重试
    input("Press enter to exit ;)")
