import os
import csv
import sqlite3
import logging

logger = logging.getLogger('import_data')

db_path = '/tmp/db'
db_file = 'netflix.db'
data_file = 'netflix_titles.csv'

if not os.path.exists(db_path):
  os.makedirs(db_path)
db_conn = sqlite3.connect(os.path.join(db_path, db_file))
cur = db_conn.cursor()
cur.execute("DROP TABLE IF EXISTS titles")
cur.execute(
  "CREATE TABLE IF NOT EXISTS titles( \
    show_id char(6) PRIMARY KEY, type char(8), title char(50), \
    director char(50), cast char(200), country char(20), \
    date_added char(20), release_year char(5), rating char(5), \
    duration char(10), listed_in char(100), description char(200) \
  )"
)

with open(data_file, 'r', encoding='Latin1') as d_file:
  dr = csv.DictReader(d_file)
  data_to_db = []
  for i, row in enumerate(dr):
    try:
      data_to_db.append((
        row['show_id'],
        row['type'],
        row['title'],
        row['director'],
        row['cast'],
        row['country'],
        row['date_added'],
        row['release_year'],
        row['rating'],
        row['duration'],
        row['listed_in'],
        row['description']
      ))
    except UnicodeDecodeError:
      logger.info('Decoding error at row:', i)

cur.executemany("INSERT INTO titles VALUES(?,?,?,?,?,?,?,?,?,?,?,?)", data_to_db)
db_conn.commit()

cur.execute("SELECT * FROM titles LIMIT 3")
for row in cur.fetchall():
  print(row)

db_conn.close()

