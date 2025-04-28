"""
@time: 2025/4/28 下午2:16
@author: Jason.Zhang
@file: request_dome2.py
@desc:加参数的request-get 使用
"""

import requests

# 1.指定url，该url是在网站中搜索后自动形成的url，将参数部分去掉，只保留原链接主体
# https://game.51.com/search/action/game/?q=%E8%8B%B1%E9%9B%84 中的 ?q=%E8%8B%B1%E9%9B%84为参数部分
url = 'https://game.51.com/search/action/game/'
game_title = input('enter a game name:')  # 查询条件不能写死，如果只有一个参数可以直接写在原链接中,为了程序的可扩展性还是将其分开描述
# 参数用字典来描述
params = {
    'q': game_title
}

# 2.发起请求,get是基于指定的url和携带固定请求参数进行请求发送
response = requests.get(url=url, params=params)

# 3.获取响应数据
page_text = response.text  # text 表示获取字符串形式的响应数据
# 测试
#print(page_text)

# 4.持久化数据存储
#文件起名
fileName = game_title + '.html'
with open('source/'+fileName, 'w')as fp:
    fp.write(page_text)
