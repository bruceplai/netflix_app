import os
import sqlite3
import logging
import pandas as pd

logger = logging.getLogger('import_data')

db_path = '/tmp/db'
db_file = 'netflix.db'
data_file = 'netflix_titles.csv'

if not os.path.exists(db_path):
  os.makedirs(db_path)
db_conn = sqlite3.connect(os.path.join(db_path, db_file))
cur = db_conn.cursor()
cur.execute("DROP TABLE IF EXISTS titles")

colNames = [
  'show_id',
  'type',
  'title',
  'director',
  'cast',
  'country',
  'date_added',
  'release_year',
  'rating',
  'duration',
  'listed_in',
  'description'
]
df = pd.read_csv(data_file, usecols=colNames)
df = df.rename(columns={'show_id':'id', 'date_added': 'dateAdded', 'release_year': 'releaseYear', 'listed_in': 'genre'})
df.to_sql('titles', db_conn)

# cur.execute("SELECT releaseYear, COUNT(releaseYear) FROM titles WHERE director LIKE '%good%' GROUP BY releaseYear")
# for row in cur.fetchall():
#   print(row)

cur.execute("SELECT * FROM titles WHERE title LIKE %good%")
for row in cur.fetchall():
  print(row)

db_conn.close()

