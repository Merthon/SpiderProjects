import scrapy
from scrapy_splash import SplashRequest
from jd_demo.items import JdDemoItem

class ProductSpider(scrapy.Spider):
    name = 'product'
    allowed_domains = ['jd.com']
    start_urls = ['https://www.jd.com/']

    # Lua 脚本来模拟页面滚动
    scroll_script = """
    function main(splash)
        splash:go(splash.args.url)
        splash:wait(2)
        -- 模拟下拉滚动
        for i = 1, 5 do
            splash:runjs("window.scrollTo(0, document.body.scrollHeight);")
            splash:wait(2)
        end
        return splash:html()
    end
    """

    def start_requests(self):
        # 使用 SplashRequest 来处理 JavaScript 渲染和滚动
        yield SplashRequest(self.start_urls[0], self.parse, args={'lua_source': self.scroll_script})

    def parse(self, response):
        # 提取商品项
        products = response.xpath('//body/div[2]/div/div/div/div[3]/div/ul/li')

        for product in products:
            item = JdDemoItem()

            # 提取商品 ID
            item['product_id'] = product.xpath('.//a/@href').re_first(r'item\.jd\.com/(\d+)\.html')

            # 提取商品描述（名称）
            item['description'] = product.xpath('.//div[2]/p/text()').get().strip()

            # 提取商品主价格
            item['price'] = product.xpath('.//div[2]/div[2]/div/span/text()').get().strip()

            # 提取商品价格的后半部分
            item['price_suffix'] = product.xpath('.//div[2]/div[2]/div/span/span/text()').get().strip()

            # 输出抓取的每个商品数据
            self.logger.info(f"Extracted item: {item}")

            # 返回商品数据
            yield item
