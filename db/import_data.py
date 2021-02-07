"""
Import Netflix CSV data into netflix.db titles table

titles table columns: 
  'id',
  'type',
  'title',
  'director',
  'cast',
  'country',
  'dateAdded',
  'releaseYear',
  'rating',
  'duration',
  'genre',
  'description'
"""

import os
import sqlite3
import logging
import pandas as pd

from sqlite3 import OperationalError

logger = logging.getLogger('import_data')
working_path = os.path.abspath(__file__)
working_dir = os.path.dirname(working_path)
os.chdir(working_dir)

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
df = df.rename(columns={
  'show_id':'id',
  'date_added': 'dateAdded',
  'release_year': 'releaseYear',
  'listed_in': 'genre',
  'cast': 'castList'
})
df.to_sql('titles', db_conn)

# try:
#   cur.execute("SELECT releaseYear, COUNT(releaseYear) FROM titles WHERE castList LIKE '%john%' GROUP BY releaseYear LIMIT 3")
#   for row in cur.fetchall():
#     print(row)
# except OperationalError as oe:
#   logger.error(oe)

db_conn.close()

