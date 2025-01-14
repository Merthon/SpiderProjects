import requests
from bs4 import BeautifulSoup

# 定义请求头（避免反爬虫机制）
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

# 目标URL
url = "https://www.shicimingju.com/book/sanguoyanyi.html"

# 获取页面内容
response = requests.get(url, headers=headers)

# 检查请求是否成功
if response.status_code != 200:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
else:
    # 使用BeautifulSoup解析HTML
    soup = BeautifulSoup(response.content, 'html.parser')

    # 打印HTML，检查结构
    print(soup.prettify()[:1000])  # 打印前1000个字符

    # 找到所有章节链接
    chapter_links = soup.find_all('a', class_='chapter')

    if not chapter_links:
        print("没有找到章节链接。")
    else:
        print(f"找到了 {len(chapter_links)} 个章节链接。")

    # 打开文件保存章节内容
    with open("BasicProjects/data_page/三国演义.txt", "w", encoding="utf-8") as file:
        # 遍历每个章节链接
        for link in chapter_links:
            chapter_url = "https://www.shicimingju.com" + link.get('href')
            chapter_title = link.text.strip()

            print(f"开始抓取章节: {chapter_title}")

            # 获取章节内容
            chapter_response = requests.get(chapter_url, headers=headers)

            if chapter_response.status_code == 200:
                chapter_soup = BeautifulSoup(chapter_response.content, 'html.parser')
                content = chapter_soup.find('div', class_='chapter_content')
                if content:
                    content_text = content.get_text(strip=True)
                    # 写入文件
                    file.write(f"章节标题: {chapter_title}\n")
                    file.write(f"章节内容:\n{content_text}\n\n")
                    print(f"已保存章节: {chapter_title}")
                else:
                    print(f"未找到章节内容: {chapter_title}")
            else:
                print(f"无法获取章节内容 {chapter_title}")

    print("所有章节内容已保存到 '三国演义.txt' 文件中。")
