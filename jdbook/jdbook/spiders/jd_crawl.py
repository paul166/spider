# -*- coding: utf-8 -*-
import scrapy,re
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class JdCrawlSpider(CrawlSpider):
    name = 'jd_crawl'
    allowed_domains = ['jd.com']
    start_urls = ['http://jd.com/']

    rules = (
        Rule(LinkExtractor(allow=''), callback='parse_item', follow=True),  # 爬取所有链接，均不加限制
    )

    def parse_item(self, response):
        i = {}
        # i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        # i['name'] = response.xpath('//div[@id="name"]').extract()
        # i['description'] = response.xpath('//div[@id="description"]').extract()

        thisurl = response.url  # 获取当前所在的地址，下一步判断是否是商品地址
        pat = 'item.jd.com/(.*?).html'
        url = re.search(pat, thisurl)
        if (url):  # 如果url是商品页
            # product_id = re.findall(pat, thisurl)[0]
            # price_link = 'http://p.3.cn/prices/mgets?callback=jQuery6325563&type=1&area=1_72_2799_0&pdtk=&pduid=1509845912914927705768&pdpin=&pin=null&pdbp=0&skuIds=J_' + str(product_id) + '&ext=11000000&source=item-pc'  # 当前商品价格链接地址
            # pat_price = 'p":"(.*?)"'  # 获取价格的正则
            #
            # price_str = urllib.request.urlopen(price_link).read().decode('utf-8', 'ignore')  # 价格所在url
            # i['price'] = re.compile(pat_price).findall(price_str)[0]  # 获取价格
            # goodRate_link = 'http://sclub.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98vv244&productId=' + str(product_id) + '&score=0&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1'  # 当前商品好评率链接地址
            # pat_goodrate = '{"goodRateShow":(.*?),'  # 正则表达式匹配价格
            # goodRate_str = urllib.request.urlopen(goodRate_link).read().decode('utf-8', 'ignore')  # 好评地址
            # i['goodRate'] = re.compile(pat_goodrate).findall(goodRate_str)[0]  # 好评率
            i['title'] = response.xpath('//title/text()').extract()  # 商品标题
            i['store'] = response.xpath('//div[@class="name"]/a/text()').extract()  # 店铺名字
            i['link'] = response.xpath('//link[@rel="canonical"]/@href').extract()  # 商品链接
            print(i)
        else:  # 不是商品叶
            pass
            # print("不是商品")
        return i
