import sqlite3
import requests
from bs4 import BeautifulSoup
# from qula.insertdbtry import insertdb
# from insertdbtry import insertdb

conn = sqlite3.connect("F:\\Python-craw\\xiaoshuo\\booksName.db")
conn.execute('''
    create table if not exists bookAll(
        id integer primary key autoincrement,
        
        chapter TEXT,
        url TEXT
    )
    ''')
con = conn.cursor()

# urls = con.execute('SELECT url FROM books')
book = con.execute('SELECT * FROM books')

def insertd(chapter, url):
    con.execute('SELECT * FROM woshizhizun WHERE (url=?)',[url])
    res = con.fetchall()
    if len(res) > 0:
        return 'error'
    else:
        con.execute("INSERT INTO woshizhizun(chapter,url)VALUES(?,?)", [chapter, url])
        conn.commit()
        print("succc")

reslut = []
reslut_name = []
reslut_urls=[]

# inser = insertdb()

# for j in urls:
#     reslut.append(j[0])
# # print(reslut)
# print(type(reslut_name))

# for j in book:

    # print(j[2])
    # reslut_name.append(j[1])
    # reslut.append(j[2])

def get_html_content(url):
    r = requests.get(url)
    r.encoding = 'utf-8'
    return r.text

def parse_html(url):
    html = get_html_content(url)
    soup = BeautifulSoup(html, 'lxml')
    # urls = soup.select("#list > dl")
    # for url in urls:
    #     print(url)
    urls = soup.find_all('dd')
    for urs in urls:
        # print(url)
        mm = urs.find('a')
        # print(mm['href'][0])
        if mm['href'][0] != '/':
            continue
        else:
            urlss = mm['href'].split('/')[3:]
            # print(urlss)
            for j in urlss:
            #     print(type(j))

                usl_total = url + j
                # # reslut_urls.append(usl_total)
                word = mm.get_text().strip()
                # inser(usl_total,word)
                # insertdb.insertdbto(word,usl_total)
                # print(usl_total)
                # print(word)
                insertd(word, usl_total)

# print(type(book))
# parse_html(book[2][0])
for j in book:
    print(parse_html(j[2]))
    break
# print(reslut)
# print(reslut_name)
# for k in book:
#     reslut_name.append(k)
# print(reslut_name)