from bs4 import BeautifulSoup
import requests

res = requests.get('http://media.daum.net/economic/')

import sqlite3
if res.status_code == 200:
    soup = BeautifulSoup(res.content, 'html.parser')
    links = soup.select('a.link_txt')
    # with sqlite3.connect('./db.sqlite3') as conn
    connect = sqlite3.connect('../db.sqlite3')
    cursor = connect.cursor()

    for link in links:
        title = str.strip(link.get_text())
        href = str.strip(link.get('href'))
        try:
            cursor.execute(
                "insert into polls_economics(create_date, href, title) values(datetime('now'), ?, ?)", (href,title))
            print(title, ' : ', href)
        except:
            pass

    connect.commit()



