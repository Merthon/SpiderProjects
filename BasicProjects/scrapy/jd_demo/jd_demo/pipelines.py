import pymongo

class JdDemoPipeline:
    def open_spider(self, spider):
        self.client = pymongo.MongoClient('localhost', 27017)  # 连接 MongoDB
        self.db = self.client['jd_database']  # 选择数据库
        self.collection = self.db['products']  # 选择集合
        self.logger.info("MongoDB connected!")

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        # 将 item 保存到 MongoDB
        self.collection.insert_one(dict(item))
        self.logger.info(f"Saved item: {item}")
        return item
