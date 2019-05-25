# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql
import redis


class QsbkPipeline(object):
    # 基于管道持久化存储
    # f = None
    #
    # def open_spider(self, spider):
    #     # 整个爬虫中此方法只会在爬虫开始时会被调用一次，解决文件覆盖问题
    #     print('spider start..')
    #     self.f = open('./qiushibaike_pipe.txt', 'w', encoding='utf-8')
    #
    # def process_item(self, item, spider):
    #     """
    #     该方法接收通过爬虫文件提交的item对象，并且对item中存储的数据进行持久化
    #     item表示接收到的item对象
    #     :param item:
    #     :param spider:
    #     :return:
    #     """
    #     # 1.取出item对象中存储的数据
    #     author = item['author']
    #     content = item['content']
    #
    #     # 2.持久化
    #     # with open('./qiusbaike_pipe.txt', 'w', encoding='utf-8') as f:
    #     # for循环提交的item会执行多次此方法，文件会被覆盖，导致只有最后一条记录
    #     self.f.write(author + ':' + content + '\n\n')
    #     # print('successful')
    #     return item
    #
    # def close_spider(self, spider):
    #     # 此方法只会在爬虫结束时被调用一次
    #     self.f.close()
    #
    #     print('spider close')

    # 基于数据库持久化存储Mysql
    # conn = None
    # cursor = None
    #
    # def open_spider(self, spider):
    #     print('开始爬虫')
    #     # 连接数据库
    #     self.conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123', db='spider')
    #
    # def process_item(self, item, spider):
    #     # 1.连接数据库
    #     # 2.执行sql语句
    #     sql = 'insert into qiubai VALUES("%s","%s")' % (item['author'], item['content'])
    #     self.cursor = self.conn.cursor()
    #
    #     try:
    #         self.cursor.execute(sql)
    #         self.conn.commit()
    #     except Exception as e:
    #         print(e)
    #
    #         self.conn.rollback()
    #     # 3.提交事务
    #
    #     return item
    #
    # def close_spider(self, spider):
    #     print('爬虫结束')
    #     self.cursor.close()
    #     self.conn.close()

    # 基于redis持久化
    conn = None

    def open_spider(self, spider):
        # print('start..')
        self.conn = redis.Redis(host='127.0.0.1', port=6379)

    def process_item(self, item, spider):
        dic = {
            'author': item['author'],
            'content': item['content']
        }
        self.conn.lpush('data', dic)
        print('redis...')
        return item

    def close_spider(self, spider):
        print('close')



class QsbkBymysql(object):

    def process_item(self, item, spider):
        print('mysql...')
        return item


class QsbkByfile(object):

    def process_item(self, item, spider):
        print('file...')
        return item
