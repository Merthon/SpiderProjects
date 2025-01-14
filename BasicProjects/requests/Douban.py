import requests

# 导入requests库用于发送HTTP请求

# 设置目标URL - 豆瓣电影Top250页面
url = 'https://movie.douban.com/top250'

# 设置请求头,模拟浏览器访问
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
}

# 发起GET请求获取页面内容
response = requests.get(url, headers=headers)

# 检查响应状态
if response.status_code == 200:
    # 获取页面HTML内容
    html_content = response.text
    # 将HTML内容保存到本地文件
    with open('BasicProjects/data_page/douban.html', 'w', encoding='utf-8') as fp:
        fp.write(html_content)
    print('HTML content saved successfully.')
else:
    # 请求失败时打印错误信息
    print(f"Failed to fetch the page. Status code: {response.status_code}")
