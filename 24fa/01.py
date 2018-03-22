# encoding: utf-8
"""
@version:3.6
@author:lamplight
@file:01.py
@time:2018/1/90:28
"""
import os
import requests
from bs4 import BeautifulSoup

url_s = 'https://www.24fa.com/MeiNv/2017-06/26254.html'
BASE_DIR = 'E:/Pictures'
headers = {
            # 'Host': "bj.lianjia.com",
            'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            'Accept-Encoding': "gzip, deflate, br",
            'Accept-Language': "zh-CN,zh;q=0.9",
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.87 Safari/537.36",
            'Connection': "keep-alive",
            'cookie':"__cfduid=def525640d6c38c8c279d2146801422091515260134; mpc=1"
        }


def get_html_text(url, timeout=5):
    'get the htnl content'
    try:
        r= requests.get(url)
        r.encoding='utf-8'
        # r.raise_for_status()
        # r.encoding = r.apparent_encoding
        # print(r.text)
        return r.text

    except:
        print('error1')
        return 'error'


def get_html_text_with_post(url, timeout=5):
    '''post, get the content'''
    try:
        r= requests.post(url, headers)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print('error2')
        return 'error'

def parse_url_list(url):
    '''
    返回所有超链接
    :param url:
    :return:
    '''
    # pass

    url_list = []
    try:
        html = get_html_text(url)
        if html != 'error':
            soup = BeautifulSoup(html, 'lxml')
            urls = soup.select("#middle > div.conR > div.lframe > ul")
            # m = []
            for url in urls:
                a = url.find_all('a')
                for i in a:
                    print(i['title'])
                    n = i['href'].split('../')[-1]
                    url_list.append('https://www.24fa.com/' + n)
                    print('https://www.24fa.com/' + n)
                    # print(url.prettify())
            # print(b)
            urls1 = soup.select("#middle > div.conR > div.lframe > div.wrapper > div > ul")
            # print(type(urls1))
            for url1 in urls1:
                a1 = url1.find_all('a')
                for i in a1:
                    print(i['title'])
                    n = i['href'].split('../')[-1]
                    url_list.append('https://www.24fa.com/' + n)
                    print('https://www.24fa.com/' + n)

            urls2 = soup.select("#middle > div.conR > ul")
            # print(type(urls1))
            for url2 in urls2:
                a2 = url2.find_all('a')
                for i in a2:
                    print(i['title'])
                    n = i['href'].split('../')[-1]
                    url_list.append('https://www.24fa.com/' + n)
                    print('https://www.24fa.com/' + n)

            urls3 = soup.select("#middle > div.conR > div.conR > div > div.wrapper > div > ul")
            for url3 in urls3:
                a3 = url3.find_all('a')
                for i in a3:
                    print(i['title'])
                    n = i['href'].split('../')[-1]
                    url_list.append('https://www.24fa.com/' + n)
                    print('https://www.24fa.com/' + n)
        return url_list
    except:
        print("eoor3")
        return -1

def cached_url(url):
    """get url content"""
    # pass
    folder = 'cached_url'
    filename = url.split('/')[4] + '.html'
    path = os.path.join(folder, filename)
    #如果缓存过了，读取文件返回
    if os.path.exists(path):
        with open(path, 'rb') as f:
            s = f.read()
            return s
    else:
        if not os.path.exists(folder):
            os.mkdir(folder)
        html = get_html_text(url)
        if html != -1:
            with open(path, 'wb') as f:
                f.write(html)
                return html
        else:
            print('{}下载失败'.format(filename))
            print('eoor4')
            return -1

def parse_img(url):

    img_list = []
    html = get_html_text(url)
    if html != -1:
        soup = BeautifulSoup(html, 'lxml')
        urls1_name = soup.select("#printBody > div:nth-of-type(1) > h1")
        name = urls1_name[0].text[0:3]
        urls1 = soup.select("#content > div > div:nth-of-type(1)")
        print(type(urls1))
        # m = []
        for url1 in urls1:
            a1 = url1.find_all('img')
            for i in a1:
                # print(i['src'])
                n = i['src'].split('../')[-1]
                # print(n)
                img_list.append('https://www.24fa.com/' + n)
                print('https://www.24fa.com/' + n)
                    # name = i.split('/')[4].split('.jpg')
                    # del name[1]
                    # for nam in name:
                    #     nam1 = nam
        print('图:{}解析完毕'.format(name))
        return dict(urls_all=img_list, name=name)
    else:
        print("出错5")
        return 'error'

def img_downloader(pac):
    '''
    下载图片
    :param pac:
    :return:
    '''
    dirname = BASE_DIR + '/imgs/' + pac['name']
    #创建文件夹
    if not os.path.exists(dirname):
        os.makedirs(dirname)
        for url in pac['urls_all']:
            filename = url.split('/')[-1]
            open(dirname + '/' + filename, 'wb').write(requests.get(url).content)
            print('{}正在下载'.format(pac['name']))
    else:
        print('已经下载过了')



if __name__ == '__main__':
    dict_imgs = []
    url_list = parse_url_list(url_s)
    for url in url_list:
        dict_img = parse_img(url)
        if dict_img != 'error':
            dict_imgs.append(dict_img)

    #多线程下载
    from multiprocessing import Pool
    # 建立进程池
    pool = Pool()
    pool.map(img_downloader, dict_imgs)
    pool.close()
    pool.join()






