# encoding: utf-8
"""
@version:3.6
@author:lamplight
@file:02.py
@time:2018/1/2223:35
"""
import requests
from bs4 import BeautifulSoup
from lxml import etree
import json
headers1={
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36',
}
headers2 = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit 537.36 (KHTML, like Gecko) Chrome'

}

# start_urls = ['http://www.ximalaya.com/dq/comic-%E5%8D%95%E7%94%B0%E8%8A%B3/{}/'.format(num) for num in range(1,5)]
# for start_url in start_urls:
#     html = requests.get(start_url, headers = headers1).text
#     soup = BeautifulSoup(html, 'lxml')
#     for  item in soup.find_all(class_="albumfaceOutter"):
#         content = {
#             'href' : item.a['href'],
#             'title': item.img['alt'],
#             'img_url': item.img['src']
#         }
        # print(content)

url = 'http://www.ximalaya.com/1000265/album/3820/'
# html = requests.get(url ,headers = headers1).text
# print(html)
# numlist = etree.HTML(html).xpath('//div[@class="personal_body"]/@sound_ids')[0].split(',')
# for i in numlist:
#     murl = 'http://www.ximalaya.com/tracks/{}.json'.format(i)
#     html = requests.get(murl, headers=headers2).text
#     dic = json.load(html)

html = requests.get(url, headers = headers1).text
ifanother = etree.HTML(html).xpath('//div[@class="pagingBar_wrapper"]/a[last()-1]/@data-page')
if len(ifanother):
    num = ifanother[0]
    print('资源有{}个页面'.format(num))
    for n in  range(1, int(num)+1):
        print('正解析{}个中的第{}个页面'.format(num, n))
        url2 = url+'?page={}'.format(n)
        print(url2)

