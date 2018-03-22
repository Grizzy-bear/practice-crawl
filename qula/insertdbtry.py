import sqlite3

conn = sqlite3.connect("F:\\Python-craw\\xiaoshuo\\booksName.db")

conn.execute('''
    create table if not exists woshizhizun(
        id integer primary key autoincrement,
        
        chapter TEXT,
        url TEXT
    )
    ''')
con = conn.cursor()

class insertdb():
    # def __init__(self, chapter, url):
    #     self.chapter = chapter
    #     self.url = url
    
    def insertdbto(self,chapter,url,):
        con.execute('SELECT * FROM woshizhizun WHERE (url=?)',[self.url])
        res = con.fetchall()
        if len(res) > 0:
            return 'error'
        else:
            con.execute("INSERT INTO woshizhizun(chapter,url)VALUES(?,?)", [self.chapter, self.url])
            conn.commit()
            print("succc")