# -*- coding: utf-8 -*-
import scrapy
from qsbk.items import QsbkItem


class QiushibaikeSpider(scrapy.Spider):
    name = 'qiushibaike'
    # 获取图片时可能会出现图片的url不在指定域名，注释此行代码
    # allowed_domains = ['www.qiushibaike.com/text']
    start_urls = ['https://www.qiushibaike.com/text/']

    def parse(self, response):
        # 建议使用xpath进行指定内容解析（scrapy集成了xpath解析接口）
        div_list = response.xpath("//div[@id='content-left']/div")

        #     # content_list = []
        #     for div in div_list:
        #         # xpath解析的内容被存储到了Selector对象中，使用extract()将selector对象中的数据拿到
        #         # author = div.xpath("./div/a[2]/h2/text()").extract()[0]
        #         # extract_first() = extract()[0]
        #
        #         author = div.xpath("./div/a[2]/h2/text()").extract_first()
        #         # print(author)  # [<Selector xpath='./div/a[2]/h2/text()' data='\n非法无罪\n'>]
        #         content = div.xpath('.//div[@class="content"]/span/text()').extract_first()
        # # 基于管道持久化
        #         # 1.将解析到的author和content存储到items对象
        #         items = QsbkItem()
        #         items['author'] = author
        #         items['content'] = content
        #
        #         #用yield关键字提交给管道
        #         yield items

        # print(content)
        # 终端持久化
        # dic = {'author': author,
        # 'content': content}
        # content_list.append(dic)
        # return content_list  # 返回一个可迭代对象

        # 数据库持久化
        for div in div_list:
            author = div.xpath("./div/a[2]/h2/text()").extract_first()
            content = div.xpath('.//div[@class="content"]/span/text()').extract_first()

            # 1.将解析到的author和content存储到items对象
            item = QsbkItem()
            item['author'] = author
            item['content'] = content

            # 用yield关键字提交给管道
            yield item
