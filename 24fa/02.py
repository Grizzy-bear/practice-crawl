# encoding: utf-8
"""
@version:3.6
@author:lamplight
@file:02.py
@time:2018/1/919:23
"""
# url
# img_list = []
# url = '../../upload/2017-06/17060705015645.jpg'
# filename = url.split('/')[2:4]
# # filename = url.split('/')[4].split('.jpg')
# # del filename[1]
# # del filename[0]
# # filename = str(filename).replace(' ', '')
# # for i in filename:
#
#     # img_list.append('https://www.24fa.com/' + i)
# print(filename)
# # print(img_list)

url = 'https://www.24fa.com/MeiNv/2017-06/26254.html'
import requests
from bs4 import BeautifulSoup

a = requests.get(url)
a.encoding='utf-8'
c = a.text
soup = BeautifulSoup(c, 'lxml')
# b = soup.find_all('h1').
# print(type(soup))
# urls = soup.select("#middle > div.conR > div.lframe > ul")
# m = []
# for url in urls:
#     a = url.find_all('a')
#     for i in a:
#         print(i['title'])
#         n= i['href'].split('../')[-1]
#         m.append('https://www.24fa.com/' + n)
#         print('https://www.24fa.com/' + n)
#     # print(url.prettify())
# # print(b)
# urls1 = soup.select("#middle > div.conR > div.lframe > div.wrapper > div > ul")
# # print(type(urls1))
# for url1 in urls1:
#     a1 = url1.find_all('a')
#     for i in a1:
#         print(i['title'])
#         n= i['href'].split('../')[-1]
#         m.append('https://www.24fa.com/' + n)
#         print('https://www.24fa.com/' + n)
#
# urls2 = soup.select("#middle > div.conR > ul")
# # print(type(urls1))
# for url2 in urls2:
#     a2 = url2.find_all('a')
#     for i in a2:
#         print(i['title'])
#         n= i['href'].split('../')[-1]
#         m.append('https://www.24fa.com/' + n)
#         print('https://www.24fa.com/' + n)
#
# urls3 = soup.select("#middle > div.conR > div.conR > div > div.wrapper > div > ul")
# for url3 in urls3:
#     a3 = url3.find_all('a')
#     for i in a3:
#         print(i['title'])
#         n= i['href'].split('../')[-1]
#         m.append('https://www.24fa.com/' + n)
#         print('https://www.24fa.com/' + n)
# print(len(m))
# urls1 = soup.select("#content > div > div:nth-of-type(1)")
# print(type(urls1))
# m = []
# for url1 in urls1:
#     a1 = url1.find_all('img')
#     for i in a1:
#         # print(i['src'])
#         n= i['src'].split('../')[-1]
#         # print(n)
#         m.append('https://www.24fa.com/' + n)
#         print('https://www.24fa.com/' + n)
# urls1 = soup.select("#printBody > div:nth-of-type(1) > h1")
# print(urls1[0].text[0:3])
# m = []
# for url1 in urls1:
#     a1 = url1.find_all('img')
#     for i in a1:
#         # print(i['src'])
#         n= i['src'].split('../')[-1]
#         # print(n)
#         m.append('https://www.24fa.com/' + n)
#         print('https://www.24fa.com/' + n)

import os
BASE_DIR = 'E:/Pictures'
pac ={
    'urls_all':'https://www.24fa.com/MeiNv/2017-06/26254.html',
    'name' : 'sha'
}
dirname = BASE_DIR + '/imgd/' + pac['name']
print(dirname)
# 创建文件夹
if not os.path.exists(dirname):
    os.makedirs(dirname)
    # for url in pac['urls_all']:
    #     filename = url.split('/')[-1]
    #     open(dirname + '/' + filename, 'wb').write(requests.get(url).content)
    #     print('{}正在下载'.format(pac['name']))
else:
    print('已经下载过了')

