import scrapy
from jd_spider.items import JdSpiderItem

class JdSpider(scrapy.Spider):
    name = 'jd_spider'
    allowed_domains = ['jd.com']
    start_urls = ['https://www.jd.com/']

    def parse(self, response):
        # 定位商品列表区域
        products = response.xpath('//body/div[2]/div/div/div/div[3]/div/ul/li')

        for product in products:
            # 创建 Item
            item = JdSpiderItem()

            # 商品ID
            item['product_id'] = product.xpath('.//a[@class="more2_lk"]/@href').re_first(r'item\.jd\.com/(\d+)\.html')

            # 商品简介
            item['description'] = product.xpath('.//p[@class="more2_info_name"]/text()').get()

            # 商品价格
            item['price'] = product.xpath('.//div[@class="mod_price"]/span[@class="more2_info_price_txt"]/text()').get()

            yield item

        # 分页处理（如果有下一页链接）
        next_page = response.xpath('//a[@class="pn-next"]/@href').get()
        if next_page:
            yield response.follow(next_page, self.parse)
