import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import time

# 设置请求头（模拟浏览器访问，防止被拒绝访问）
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}

# 百度图片搜索页面 URL（根据关键词替换）
search_url = 'https://image.baidu.com/search/index?tn=baiduimage&word=cat'  # 替换为你想要的搜索页面

# 发起请求获取页面内容
response = requests.get(search_url, headers=headers)

# 解析网页内容
soup = BeautifulSoup(response.text, 'html.parser')

# 创建一个文件夹用于保存图片
folder = 'baidu_images'
if not os.path.exists(folder):
    os.makedirs(folder)

# 找到所有图片的标签（百度图片会将图像放在 <img> 标签的 "data-imgurl" 属性中）
img_tags = soup.find_all('img', {'data-imgurl': True})

# 控制爬取图片的数量
max_images = 5  # 这里设置爬取最多 5 张图片
image_count = 0

# 遍历图片标签并下载图片
for img_tag in img_tags:
    if image_count >= max_images:
        break  # 如果下载的图片达到限制数量，则退出循环
    
    # 获取图片的 URL 地址（data-imgurl 是图片的实际链接）
    img_url = img_tag.get('data-imgurl')
    if img_url:
        # 拼接绝对路径
        img_url = urljoin(search_url, img_url)
        
        # 获取图片名称
        img_name = os.path.join(folder, os.path.basename(img_url))
        
        try:
            # 下载图片
            img_data = requests.get(img_url, headers=headers).content
            with open(img_name, 'wb') as f:
                f.write(img_data)
            print(f'图片下载完成: {img_name}')
            image_count += 1
        except Exception as e:
            print(f'下载失败: {img_url}, 错误: {e}')
        
        # 适当休眠，避免过于频繁请求
        time.sleep(1)
