BOT_NAME = 'jd_scraper'

SPIDER_MODULES = ['jd_scraper.spiders']
NEWSPIDER_MODULE = 'jd_scraper.spiders'

# 禁止遵守 robots.txt
ROBOTSTXT_OBEY = False

# 下载延迟设置，避免被封
DOWNLOAD_DELAY = 2  # 两秒延迟

# 启用管道
ITEM_PIPELINES = {
    'jd_scraper.pipelines.JdScraperPipeline': 300,
}

# 启用随机 User-Agent 中间件
DOWNLOADER_MIDDLEWARES = {
    'jd_scraper.middlewares.RandomUserAgentMiddleware': 400,
}
