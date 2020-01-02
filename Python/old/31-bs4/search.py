import sqlite3
from pprint import pprint

conn = sqlite3.connect("rosterdb.sqlite")
cur = conn.cursor()

search_string = str(input("Question: ")).strip()

cur.execute('''SELECT text, link FROM Questions 
    WHERE LOWER(text) LIKE LOWER('%{}%');'''.format(search_string))

data = cur.fetchall()
for q, l in data:
    print(f"{q} - {l}")
print("="*20)
print(f"{len(data)} results")