# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy_redis.spiders import RedisCrawlSpider


class AmazonSpider(RedisCrawlSpider):
    name = 'amazon'
    allowed_domains = ['amazon.cn']
    #start_urls = ['https://www.amazon.cn/%E5%9B%BE%E4%B9%A6/b/ref=sa_menu_top_books_l1?ie=UTF8&node=658390051']
    redis_key = 'amazon'

    rules = (Rule(LinkExtractor(restrict_xpaths=('//ul[@class="a-unordered-list a-nostyle a-vertical s-ref-indent-one"]/div/li')), follow=True),
             Rule(LinkExtractor(restrict_xpaths=('//div[@class="left_nav browseBox"]/ul/li')),follow=True),
             # 匹配图书的url地址
             Rule(LinkExtractor(restrict_xpaths=("//div[@id='mainResults']/ul/li//h2/..")),callback="parse_book_detail"),
             #翻页
             Rule(LinkExtractor(restrict_xpaths=('//div[@id="pagn"]')), follow=True)
             )


    def parse_book_detail(self, response):
        item= {}
        item['title'] = response.xpath('//span[@id="productTitle"]/text()').extract_first()
        item['book_publish_date'] = response.xpath('//h1[@id="title"]/span[3]/text()').extract_first()
        item['book_author'] = response.xpath('//div[@id="bylineInfo"]/span/a/text()').extract()
        #item['book_img'] = response.xpath('//div[@id="img-canvas"]/img/@src').extract_first()
        item['book_price'] = response.xpath('//div[@id="soldByThirdParty"]/span[2]/text()').extract_first()
        item['book_press'] = response.xpath('//b[text()="出版社:"]/../text()').extract_first()
        print(item)
