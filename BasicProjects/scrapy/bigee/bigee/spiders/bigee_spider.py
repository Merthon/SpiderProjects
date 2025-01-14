import scrapy

class BigeeSpider(scrapy.Spider):
    name = 'bigee_spider'
    allowed_domains = ['bigee.cc']
    start_urls = ['https://www.bigee.cc/book/1/']

    def parse(self, response):
        # 提取当前页面的小说标题和简介
        title = response.css('div.bookname h1::text').get()
        intro = response.css('div#intro p::text').get()

        yield {
            'title': title,
            'intro': intro
        }

        # 遍历后续页面的URL，提取下一本书的内容
        for i in range(2, 1000):
            next_url = f'https://www.bigee.cc/book/{i}/'
            yield scrapy.Request(next_url, callback=self.parse)
