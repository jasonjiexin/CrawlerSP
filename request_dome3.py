"""
@time: 2025/4/28 下午4:17
@author: Jason.Zhang
@file: request_dome3.py
@dees: UA 反爬策略
"""

import requests

# 1.指定url
url = 'http://www.cpta.com.cn/'

# UA反爬机制破解
header={
'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36'
}

# 2.发起请求
response = requests.get(url=url,headers=header)

# 3.获取响应数据
page_text = response.text
# 测试
print(page_text)

# 4.数据持久化存储
with open('source/zhongguorenshiwang.html','w') as fp:
    fp.write(page_text)