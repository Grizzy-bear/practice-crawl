import requests
from lxml import html
from bs4 import BeautifulSoup
import sqlite3
# ID INT PRIMARY KEY NOT NULL,
conn = sqlite3.connect("F:\\Python-craw\\MMIMG\\mmimg.db")
print("create suceessfully")
conn.execute('''
    create table if not exists mmimgsA(
        id integer primary key autoincrement,
        
        name TEXT,
        url TEXT
    )
    ''')
conn.execute('''
    create table if not exists mm_urlsA(
        id integer primary key autoincrement,
        
        page INT,
        url TEXT
    )
    ''')
print("表创建成功")
con = conn.cursor()

# insert to db


def record_urls(page, url):
    # sql_cmd = ''' select * from mm_urls where url LIKE '/s' ''' % url
    # con.execute(sql_cmd)
    # con.execute("select * from mm_urls where url LIKE '/s' ",[url])
    # con.execute("SELECT * FROM mm_urls WHERE url=%s;", (url, ))
    con.execute('SELECT * FROM mm_urlsA WHERE (url=?)',[url])
    # sql_cmd = "SELECT * FROM mm_urls WHERE url LIKE %s;"
    # args = [url,]
    # con.execute(sql_cmd,args)
    res = con.fetchall()
    if len(res) > 0:
        return 'error'
    else:

        # sql = '''inset into mm_urls(page,url)values('%d','%s')''' % (page, url)
        # con.execute(sql)
        con.execute("INSERT INTO mm_urlsA(page,url)VALUES(?,?)", [page, url])
        conn.commit()
        return 'suceess'


def insert_db(name, url):
    # sql_cmd = '''select * from mmimgs where name = '/s' ''' % name
    # con.execute(sql_cmd)
    # con.execute("select * from mmimgs where name LIKE '/s'",[name])
    con.execute('SELECT * FROM mmimgsA WHERE (name=?)',[name])
    res = con.fetchall()
    if len(res) > 0:
        return 'error'
    else:
        # sql = '''insert into mmimgs(name,url)values('%s','%s')''' % (name, url)
        # con.execute(sql)
        con.execute("INSERT INTO mmimgsA(name,url)VALUES(?,?)", [name, url])
        print("oj")
        conn.commit()


HEADERS = {
    # 'Host': "bj.lianjia.com",
    'Accept':
    "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    'Accept-Encoding':
    "gzip, deflate, br",
    'Accept-Language':
    "zh-CN,zh;q=0.9",
    'User-Agent':
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.87 Safari/537.36",
    'Connection':
    "keep-alive",
    'cookie':
    "__cfduid=def525640d6c38c8c279d2146801422091515260134; mpc=1"
}
BaseDir = 'F://Python-craw'
url = 'http://www.mmjpg.com/'
urls = 'http://www.mmjpg.com/home/{}'


def get_html_text(url, timeout=5):
    # get the content
    try:
        # urlA = url[0] 
        # print(urlA)
        # print(url)
        r = requests.get(url)
        r.encoding = 'utf-8'
        return r.text
    except:
        print("erroraaa")
        return 'error'
        # pass


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
                Judge = insert_db(name, urlImage)
                if Judge == 'error':
                    print("cunguo")
                    # continue
                    return 'errora'

    # except:
    #     print("erro2")
    #     return 'error'


# get_urls(url)
# result = []
# record all urls from pages[1:30]
for i in range(2, 41):
    mmimgUrl = urls.format(i)
    judge = record_urls(i, mmimgUrl)
    if judge == 'error3':
        continue

#获得sqlite，mm_urls内容
lis = con.execute('SELECT url FROM mm_urlsA')
# print(type(lis))
reslut = []

for j in lis:
    reslut.append(j[0])
# print(reslut)
for row in reslut:
    # print(row)
    # print(row)
    # rowA = row[0]
    print(row)

    resul = get_urls(row)
    # # print(resul)
    if resul == 'errora':
    #     print("hao")
        continue

    # print(rowA)
    # get_urls('http://www.mmjpg.com/home/2')
    
