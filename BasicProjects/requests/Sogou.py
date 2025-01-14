import requests

# 增加请求头，达到伪装的效果
# URL = https://www.sogou.com/web?
# headers ：Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36
headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
}
url = 'https://www.sogou.com/web?'
# 增加一个搜索关键字，url 参数
word = input('please enter a word :')
param = {
    'query' : word
}
response = requests.get(url=url, params=param, headers=headers)
pagedata = response.text
# 储存网页
with open('BasicProjects/data_page//sogou.html', 'w', encoding='utf-8')as fp:
    fp.write(pagedata)
print('successful!')