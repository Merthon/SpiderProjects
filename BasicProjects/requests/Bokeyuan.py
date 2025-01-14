import requests

url = "https://www.cnblogs.com/"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
}
response = requests.get(url, headers=headers)

with open('BasicProjects/data_page/blog_articles.html', 'w', encoding='utf-8') as f:
        f.write(response.text)
print('successful!')