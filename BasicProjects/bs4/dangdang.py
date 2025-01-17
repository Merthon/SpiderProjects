from bs4 import BeautifulSoup
import requests

#爬取当当网书籍信息
def dang_book(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
    }
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text
    except requests.RequestException:
        return None
    
# 解析网页
def parse_result(html):
    soup = BeautifulSoup(html, 'lxml')
    items = soup.find('ul', class_='bang_list').find_all('li')

    for item in items:
        rank = item.find(class_='list_num').text[:-1]
        url = item.find('a')['href']
        name = item.find(class_='name').text
        price = item.find(class_='price_n').text
        publisher_total = item.find_all(class_='publisher_info')
        publisher_list = []
        for publisher in publisher_total:
            publisher_list.append(publisher.text)
        # print(rank, url, name, publisher_list[0], publisher_list[1], price)
        result = "rank:" + rank + "; " + "url:" + url + "; " + "name:" + name + "; " + "author:" + publisher_list[0] + "; " + "publisher:" + publisher_list[1] + "; " + "price:" + price
        # print(result)
        write_item_to_file(result)

# 将数据写到txt
def write_item_to_file(item):
    print('开始写入数据 ====> ' + item)
    with open('book.txt', 'a') as f:
        f.write(item + '\n')

# 主函数
def main(page):
    url = 'http://bang.dangdang.com/books/fivestars/01.00.00.00.00.00-recent30-0-0-1-' + str(page)
    html = dang_book(url)
    parse_result(html)

if __name__ == "__main__":
    for i in range(1, 26):
        main(i)