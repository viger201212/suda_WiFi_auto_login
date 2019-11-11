# 苏大WiFi自动登录脚本
 使用python写的而简单脚本, 方便苏州大学学生快速登录苏大WiFi. 会在后台运行直到登录成功为止, 需要手动关闭. 有什么好的解决方案欢迎提交issu
  ***
#### 依赖:
* [Python3](https://www.python.org/downloads/)
* requests

  `pip install requests`
  
  或者
  
  `pip3 install requests`
 ***
#### 使用说明
  * 下载suda_WIFI_auto_login.py. 对于Linux,可能需要赋予权限`chmod a+x ./suda_WIFI_auto_login.py`
  * 首次运行, 编辑suda_WIFI_auto_login.py文件, 在 username 和 password 处填入你想登录的苏大WiFi账号. 对于移动宽带账户, 请填入宽带账号密码并修改 method 为 2 或 3.
  * 使用Python解释器运行suda_WIFI_auto_login.py. 在终端或脚本中执行
  
  `python ./suda_WIFI_auto_login.py`
  
  或
  
  `python3 ./suda_WIFI_auto_login.py`

#### 自启动
***
* **Windows**:
移动suda_WIFI_auto_login到C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp

* **Linux**:
编辑~/.bashrc, 在文件末尾添加`/usr/bin/python3 */suda_WIFI_auto_login.py` 将路劲修改为你存脚本的绝对路径即可

## todo
 [x] 优化循环判断
 [ ] Android 兼容
 [x] 移动宽带登录支持