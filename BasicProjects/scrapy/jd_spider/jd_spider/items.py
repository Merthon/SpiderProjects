# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

# 定义 Item 数据结构
class JdSpiderItem(scrapy.Item):
    product_id = scrapy.Field() #商品id
    description = scrapy.Field() # 商品描述
    price = scrapy.Field() # 商品价格
