import scrapy


class Bi05Spider(scrapy.Spider):
    name = 'bi05'
    allowed_domains = ['bi05.cc']
    start_urls = ['http://bi05.cc/html/179106/'] #小说目录页

    def parse(self, response):
        chapter_links = response.xpath()
