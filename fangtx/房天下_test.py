import requests,re
from lxml import etree


headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36"}
url='https://www.fang.com/SoufunFamily.htm'

res=requests.get(url,headers=headers)
html_str=res.text
response = etree.HTML(html_str)
print(response)
trs = response.xpath('//div[@class="outCont"]//tr')
province = None
for tr in trs:
    tds = tr.xpath('.//td[not(@class)]')
    province_td = tds[0]
    provice_text = province_td.xpath(".//text()")[0]
    province_text = re.sub(r'\s', '', provice_text)
    if province_text:
        province = province_text
    # 排除海外城市
    if province == '其它':
        continue

    city_td = tds[1]
    city_links = city_td.xpath(".//a")
    for city in city_links:
        city_name = city.xpath('.//text()')[0]
        city_url = city.xpath('.//@href')[0]
        print('省份：',province)
        print('城市：',city_name)
        print('城市url：',city_url)
