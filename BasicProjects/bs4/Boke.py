import requests
from bs4 import BeautifulSoup
import json

url = "https://www.cnblogs.com/"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
    }
# 获取页面内容
response = requests.get(url, headers=headers)

# 输出页面内容进行调试
print(response.text[:1000])  # 打印前 1000 个字符查看网页结构

# 如果请求成功
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # 用来保存所有文章数据
    articles = []
    
    # 查找所有的文章项
    for item in soup.find_all('div', class_='post-item'):
        article = {}
        
        # 获取文章标题
        title_tag = item.find('a', class_='title')
        if title_tag:
            article['title'] = title_tag.text.strip()
            article['url'] = title_tag['href']
        
        # 获取文章作者
        author_tag = item.find('a', class_='lightblue')
        if author_tag:
            article['author'] = author_tag.text.strip()

        # 获取文章发布时间（可能会找不到）
        time_tag = item.find('span', class_='time')
        if time_tag:
            article['time'] = time_tag.text.strip()

        # 将抓取的文章数据添加到列表中
        articles.append(article)
    
    # 保存数据为 JSON 文件
    with open('BasicProjects/data_page/blog_articles.json', 'w', encoding='utf-8') as f:
        json.dump(articles, f, ensure_ascii=False, indent=2)
    
    print("博客园博客文章数据已成功保存。")
else:
    print(f"请求失败，状态码：{response.status_code}")