import requests
from lxml import etree
from bs4 import BeautifulSoup

url = 'http://www.mmjpg.com/home/2'
# r = requests.get(url)
# r.encoding = 'utf-8'
# # print(r.text)
# content = r.text
# # print(content)
# soup = BeautifulSoup(content,'lxml')
# # # urls = soup.find_all("/html/body/div[2]/div[1]/ul/li")
# urls = soup.select("body > div.main > div.pic > ul > li")
# # print(urls)
# for i in urls:
#     # print(i)
#     imgs = i.find_all('img')
#     # print(name)
#     for i in imgs:
#         # print(i)
#         name = i['alt'][:5]
#         urla = i['src']
#         print(name,urla)


# res = []
# for i in range(2,4):
#     print(i)
#     r = requests.get(url.format(i))
#     r.encoding = 'utf-8'
#     etree.HTML(r.text)
#     print("ok")
    # print(r.text)

# a = ('http://www.mmjpg.com/home/36',)
# print(a[0])
def get_html_text(url, timeout=5):
    # get the content
    try:
        # urlA = url[0] 
        # print(urlA)
        # print(url)
        r = requests.get(url)
        r.encoding = 'utf-8'
        return r.text
        # print(r.text)
    except:
        print("erroraaa")
        return 'error'
        # pass
# get_html_text(url)
def get_urls(url):
    ''' 
    get all urls of imgs
    '''
    # temp_imgUrls = {}
    # try:
        # print(url)
    html = get_html_text(url)
    # print(html)
    if html != 'error':
        print("okaaa")
        soup = BeautifulSoup(html, 'lxml')
        urls = soup.select("body > div.main > div.pic > ul > li ")
        print("ok")
        for urla in urls:
            # print("ok")
            # print("\n")
            # print(url.find_all('img'))
            # print(url[span])
            imgs = urla.find_all('img')
            for img in imgs:
                # print(img['alt'][:5])
                # temp_imgUrls.append(img['href'])
                name = img['alt'][:5]
                urlImage = img['src']
                print(name, urlImage)
                # temp_img = {'name':'href'}
                # temp_imgUrls.update(temp_img)
                # Judge = insert_db(name, urlImage)
                # if Judge == 'error':
                    # continue

    # except:
        # print("erro2")
        # return 'error'
get_urls(url)