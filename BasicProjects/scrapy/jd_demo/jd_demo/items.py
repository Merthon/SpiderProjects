import scrapy

class JdDemoItem(scrapy.Item):
    product_id = scrapy.Field()  # 商品ID
    description = scrapy.Field()  # 商品简介
    price = scrapy.Field()  # 商品价格
