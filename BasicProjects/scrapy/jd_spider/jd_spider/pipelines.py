# 配置 Pipeline 将数据存储到 MongoDB
from pymongo import MongoClient

class JdScraperPipeline:
    def open_spider(self, spider):
        # 连接 MongoDB
        self.client = MongoClient('localhost', 27017)
        self.db = self.client['jd_database']
        self.collection = self.db['products']

    def close_spider(self, spider):
        # 关闭 MongoDB 连接
        self.client.close()

    def process_item(self, item, spider):
        # 将 Item 存储到 MongoDB
        self.collection.insert_one(dict(item))
        return item
