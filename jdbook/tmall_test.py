import requests,re
from lxml import etree

# github https://github.com/shengqiangzhang/examples-of-web-crawlers

headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36",
           'cookie':'_med=dw:1920&dh:1080&pw:1920&ph:1080&ist:0; cna=o4/6FCNwKV4CAdpcKcJ8KL2b; enc=E1h7nTFszrFiLk6M6OvC1ZRcS2e%2Fsh9n%2BmDSMI0CHEUQg1XUM3FzKDZMyqYkevoAHu0XS4eWFN%2FgQgFEkM%2BhYA%3D%3D; lid=%E5%BC%93%E9%95%BF%E5%AE%9D1585531; hng=CN%7Czh-CN%7CCNY%7C156; _uab_collina=155176451870994656709724; dnk=%5Cu5F13%5Cu957F%5Cu5B9D1585531; uc1=cookie16=VT5L2FSpNgq6fDudInPRgavC%2BQ%3D%3D&cookie21=URm48syIYB3rzvI4Dim4&cookie15=U%2BGCWk%2F75gdr5Q%3D%3D&existShop=false&pas=0&cookie14=UoTZ4SWFLIWnww%3D%3D&cart_m=0&tag=8&lng=zh_CN; uc3=vt3=F8dByEiWo4C86otaI9A%3D&id2=UonfP6dUbX4lLw%3D%3D&nk2=2iKXu7tddRZHujTRVg%3D%3D&lg2=V32FPkk%2Fw0dUvg%3D%3D; tracknick=%5Cu5F13%5Cu957F%5Cu5B9D1585531; lgc=%5Cu5F13%5Cu957F%5Cu5B9D1585531; cookie2=14a7b48e0e7d255e461312ad613ad27c; t=c5aa073e79ad7849e9cf23e4e1bb0aac; csg=8ed738db; _tb_token_=e3e1318bbf5e7; cq=ccp%3D1; _m_h5_tk=491662762196c452fec4e16a817965e8_1555146486461; _m_h5_tk_enc=491c8951fc7f0d82f41c6dccc631fdfb; res=scroll%3A1903*5999-client%3A1903*430-offset%3A1903*5999-screen%3A1920*1080; x5sec=7b22746d616c6c7365617263683b32223a223931396437633631303936636233386232343130336238363939626437626534434a366478755546454d5879725a574d397075354f426f4d4d5467304f4451324e546b324f547378227d; isg=BNbWfRt-lhASk6JxcxQZqOkoJ4wY3xm2Irg-TUA_wrlUA3adqAdqwTzxm99KsBLJ; l=bBxQSCKuv1ED19nyBOCanurza77OSIRYYuPzaNbMi_5I76T6aRbOlZgnPF96Vj5R_ILB4q0AiPv9-etkZ; pnm_cku822=098%23E1hvVpvUvbpvUvCkvvvvvjiPRL5h6jrEn2zv1jrCPmPwzjiRnLsp0jEjP2d9ljYW2QhvCvvvMMGCvpvVvmvvvhCvKphv8vvvvvCvpvvvvvm2phCvCbIvvUnvphvpgvvv96CvpCCvvvm2phCvhhmivpvUvvmvnxcvmruEvpvVmvvC9jXPmphvLCClrpvj7SoBSO0Trkxb670xfXkKjL7xfwClDCODN%2B1lYE7re1lVQj7QiXT4a6VQ0f0DW3CQog0HsXZpVcIUDajxALwp8Boxfa1l51Qtvpvhvvvvv8wCvvpvvUmm',

           }


def shop(url):
    response = requests.get(url=url, headers=headers)
    response = response.text
    print(response)
    return response


def detail(response):
    html = etree.HTML(response)
    lists = html.xpath('//*[@id="J_ItemList"]/div')
    for list in lists:
        item={}
        item['title'] = list.xpath('.//*[@class="productTitle"]/a/text()')[0].strip()
        item['price'] = list.xpath('.//*[@class="productPrice"]/em/@title')[0]
        #item['url']='https://read.douban.com/'+list.xpath('./a/@href')[0]

        print(item)


def main():
    url='https://list.tmall.com/search_product.htm?type=pc&q=%C3%AB%C4%D8%CD%E2%CC%D7%C5%AE&totalPage=80&sort=s&style=g&jumpto=4'
    url2='https://list.tmall.com/search_product.htm?q=%C3%AB%C4%D8%CD%E2%CC%D7%C5%AE&type=p&cat=all'
    content=shop(url2)
    book_url=detail(content)


if __name__ == '__main__':
    main()




