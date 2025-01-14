import requests

url = 'https://www.thepaper.cn/channel_122908'
response = requests.get(url=url)
# 获取相应数据
page = response.text
# print(page)检查是否成功
# 存储页面
with open('BasicProjects/data_page/news.html','w',encoding='utf-8') as fp:
    fp.write(page)
print("It's over")