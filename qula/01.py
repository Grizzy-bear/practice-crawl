import requests
from bs4 import BeautifulSoup
import sqlite3

url = "https://www.qu.la/"

headers = {
     # 'Host': "bj.lianjia.com",
    'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    'Accept-Encoding': "gzip, deflate, br",
    'Accept-Language': "zh-CN,zh;q=0.9",
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.87 Safari/537.36",
    'Connection': "keep-alive",
    'cookie':"__cfduid=def525640d6c38c8c279d2146801422091515260134; mpc=1"
}

novel_name_urls=[]

def get_html_text(url,timeout = 5):
    r = requests.get(url)
    r.encoding = 'utf-8'
    return r.text

# print(get_html_text(url))
num = []
nun = []
def get_name_author(url):
    html = get_html_text(url)
    soup = BeautifulSoup(html, 'lxml')
    urls = soup.select("#hotcontent > div.l")
    # print(type(urls))
    for url in urls:
        # print(url.find_one('a'))
        # print(url.find_all('a'))
        # a = url.find_all('a')
        # print(a['href'])
        # a = url.xpath(../div[1]/div[1]/a/@href)
        a = url.find_all('a')
        b = url.find_all('img')
        # print(a)

        for i in a:
            if i['href'] not in num:
                num.append(i['href'])
                print(i['href'])
            # print(i['alt'])
        for j in b:
            nun.append(j['alt'])
            print(j['alt'])
    return (nun,num)
    
# get_name_author(url)

conn = sqlite3.connect("F:\\Python-craw\\xiaoshuo\\booksName.db")

conn.execute('''
    create table if not exists books(
        id integer primary key autoincrement,
        
        book TEXT,
        url TEXT
    )
    ''')
con = conn.cursor()
def insert_db(book, url):
    con.execute('SELECT * FROM books WHERE (url=?)',[url])
    res = con.fetchall()
    if len(res) > 0:
        return 'error'
    else:
        con.execute("INSERT INTO books(book,url)VALUES(?,?)", [book, url])
        conn.commit()
        print("succc")

(book,name_url) = get_name_author(url)

total = []
for i in name_url:
    l = list(i)
    del(l[0])
    m = ''.join(l)
    mk = url + m
    total.append(mk)

diction = dict(zip(book,total))
for boo, ur in diction.items():
    insert_db(boo,ur)

# print(num)
# print(nun)
