import requests,re
from lxml import etree

headers ={"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36"}

# pc端有反爬
def get_one_page(url):
        html = requests.get(url, headers=headers)
        html_return =html.text
        #print(html_return)
        html=etree.HTML(html_return)
        house_list = html.xpath("//ul[@class='sellListContent']/li")
        print(house_list)
        for house in house_list:
            item={}
            item['name'] = house.xpath("./div/div/a/text()")[0]
            item['href'] = house.xpath('./div/div/a/@href')[0]
            # huxing = house.xpath("./div[2]/p[2]/text()")[0]
            # zongjia = house.xpath("string(./div[2]/p[3])")

            print(item)
            #sel = download(href)


def main():
    for i in range(1,2):
        url = 'https://bj.lianjia.com/ershoufang/pg{}/'.format(i)
        get_one_page(url)


if __name__ == '__main__':
    pass
    #main()




# mobile

headers ={"User-Agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1"}

for i in range(376,1920):
    url='https://m.lianjia.com/bj/ershoufang/pg{}/?_t=1'.format(i)
    print(url)
    html = requests.get(url, headers=headers)
    html_return =html.text
    #print(html_return)
    html = etree.HTML(html_return)
    house_list = html.xpath("//*[@class='mod_cont lazyload_ulog']/ul/li")
    for house in house_list[1:-1]:
        item = {}
        item['name'] = house.xpath('.//div[@class="media_main"]/img/@alt')[0]
        item['href'] = house.xpath('./a/@href')[0]

        print(item)


