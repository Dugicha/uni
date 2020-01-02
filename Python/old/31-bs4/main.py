from bs4 import BeautifulSoup
import requests
import sqlite3

origin_url = "https://code.i-harness.com" # for concatenating question link
base_page = "https://code.i-harness.com/en/tagged/python?page="
current_page_num = 1
current_page = base_page + str(current_page_num)

questions = []

conn = sqlite3.connect('rosterdb.sqlite')
cur = conn.cursor()

# Do some setup
cur.executescript('''
DROP TABLE IF EXISTS Questions;
CREATE TABLE Questions (
    id    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    text    TEXT UNIQUE,
    link    TEXT UNIQUE
)''')

r = requests.get(current_page)
while r.status_code == 200:
    soup = BeautifulSoup(r.content, "html5lib")
    ordered_lists = soup.find_all("ol")
    if len(ordered_lists[0].find_all("a")) == 0:
        break;
    for ordered_list in ordered_lists:
        for a in ordered_list.find_all("a"):
            text = a.string.strip()
            link = origin_url + str(a.get("href"))
            cur.execute('''INSERT OR REPLACE INTO Questions
              (text, link) VALUES (?, ?)''', 
              (text, link))
            print(text)
    current_page_num += 1
    current_page = base_page + str(current_page_num)
    r = requests.get(current_page)

conn.commit()
cur.execute("SELECT * FROM Questions")
data = cur.fetchall()
print(data)