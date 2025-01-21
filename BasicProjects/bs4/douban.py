import requests
from bs4 import BeautifulSoup
import json

base_url = "https://movie.douban.com/top250"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36\
                        (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
    }

movies = []

# 遍历所有 10 页
for i in range(10):
    url = f"{base_url}?start={i * 25}"
    
    # 获取页面内容
    response = requests.get(url, headers=headers)
    
    # 如果请求成功
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # 查找所有的电影项
        for item in soup.find_all('div', class_='item'):
            movie = {}
            
            # 获取电影标题
            title_tag = item.find('span', class_='title')
            if title_tag:
                movie['title'] = title_tag.text
            
            # 获取评分
            rating_tag = item.find('span', class_='rating_num')
            if rating_tag:
                movie['rating'] = rating_tag.text
            
            # 获取电影的引用语句
            quote_tag = item.find('span', class_='inq')
            if quote_tag:
                movie['quote'] = quote_tag.text
            else:
                movie['quote'] = "No quote"
            
            movies.append(movie)
        
        print(f"已抓取第 {i+1} 页数据")
    else:
        print(f"请求失败，状态码：{response.status_code}")
        break

# 保存数据为 JSON 文件
with open('BasicProjects/data_page/douban_movies.json', 'w', encoding='utf-8') as f:
    json.dump(movies, f, ensure_ascii=False, indent=2)

print("豆瓣电影榜单所有数据已成功保存。")

