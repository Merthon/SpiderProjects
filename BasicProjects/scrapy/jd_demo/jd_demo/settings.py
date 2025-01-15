# settings.py
SPLASH_URL = 'http://localhost:8050'  # Splash 服务的地址

DOWNLOADER_MIDDLEWARES = {
    'scrapy_splash.SplashMiddleware': 725,  # 启用 Splash 中间件
    'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 810,
}

SPIDER_MIDDLEWARES = {
    'scrapy_splash.SplashSpiderMiddleware': 725,
}

SPIDER_MODULES = ['jd_demo.spiders']

# 设置下载延迟
DOWNLOAD_DELAY = 2

# 启用 JSON-LD 数据
FEED_FORMAT = 'jsonlines'
FEED_URI = 'output.json'
