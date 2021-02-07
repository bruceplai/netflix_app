import sqlite3

from typing import List
from title import Title
from data_point import DataPoint

class Model:
  """
  Application model that queries data stored in SQLite netflix.db titles table

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
  def __init__(self) -> None:
    self.db_file = '/tmp/db/netflix.db'
  
  def get_title(self, id: str) -> Title:
    """
    Get title data by id, which is matched to id in the titles table
    """
    db_conn = sqlite3.connect(self.db_file)
    with db_conn:
      cursor = db_conn.cursor()
      query = cursor.execute("SELECT * FROM titles WHERE id = ?", [id])
      colnames = [des[0] for des in query.description]
      result = cursor.fetchone()
      if not result:
        return None
      title = {}
      for i in range(len(colnames)):
        title[colnames[i]] = result[i] or ""
    return Title(**title)

  def get_titles(self, title: str, director: str) -> List[Title]:
    """
    Get data for multiple titles by searching by partial title and/or director matches.
    """
    results = []
    query_addon = []
    if title:
      query_addon.append(f"title LIKE '%{title}%'")
    if director:
      query_addon.append(f"director LIKE '%{director}%'")
    if query_addon:
      query_addon = " AND ".join(query_addon)
    db_conn = sqlite3.connect(self.db_file)
    with db_conn:
      cur = db_conn.cursor()
      if query_addon:
        query = cur.execute("SELECT * FROM titles WHERE " + query_addon)
      else:
        query = cur.execute("SELECT * FROM titles")
      colnames = [des[0] for des in query.description]
      for row in cur.fetchall():
        title = {}
        for i in range(len(colnames)):
          title[colnames[i]] = row[i] or ""
        results.append(Title(**title))
    return results

  def __query_by_group(self, col: str, **kwargs) -> List[DataPoint]:
    """
    Query that returns counts grouped by input column.
    Optional filter args can be passed in.
    """
    results = []
    query_addon = []
    for key, val in kwargs.items():
      if val:
        query_addon.append(f"{key} LIKE '%{val}%'")
    if query_addon:
      query_addon = " AND " + " AND ".join(query_addon)
    else:
      query_addon = ""
    db_conn = sqlite3.connect(self.db_file)
    with db_conn:
      cur = db_conn.cursor()
      query_str = f"SELECT {col} AS name, COUNT({col}) AS value \
        FROM titles \
        WHERE {col} IS NOT NULL {query_addon} \
        GROUP BY {col}"
      cur.execute(query_str)
      for row in cur.fetchall():
        results.append(DataPoint(**{ 'name': str(row[0]), 'value': row[1] }))
    return results

  def __query_and_post_process(self, col: str, **kwargs) -> List[DataPoint]:
    """
    Query that returns counts grouped by comma separated values in input column.
    Post processing is required for columns that have comma separated lists
    rather than single string values.
    Optional filter args can be passed in.
    """
    results = []
    query_addon = []
    for key, val in kwargs.items():
      if val:
        query_addon.append(f"{key} LIKE '%{val}%'")
    if query_addon:
      query_addon = " AND " + " AND ".join(query_addon)
    else:
      query_addon = ""
    db_conn = sqlite3.connect(self.db_file)
    with db_conn:
      cur = db_conn.cursor()
      query_str = f"SELECT {col} FROM titles WHERE {col} IS NOT NULL {query_addon}"
      cur.execute(query_str)
      result_dict = {}
      for row in cur.fetchall():
        row_vals = row[0].split(',')
        for val in row_vals:
          val = val.strip()
          if val not in result_dict:
            result_dict[val] = 1
          else:
            result_dict[val] += 1
    for item in result_dict.items():
      results.append({ 'name': str(item[0]), 'value': item[1] })
    return results

  def get_years(self, title: str, director: str):
    """
    Get release year data for partial title and/or director matches.
    """
    return self.__query_by_group('releaseYear', title=title, director=director)

  def get_ratings(self, title, director):
    """
    Get rating data for partial title and/or director matches.
    """
    return self.__query_by_group('rating', title=title, director=director)

  def get_countries(self, title: str, director: str):
    """
    Get release country data for partial title and/or director matches.
    """
    return self.__query_and_post_process('country', title=title, director=director)

  def get_genres(self, title, director):
    """
    Get release country data for partial title and/or director matches.
    """
    return self.__query_and_post_process('genre', title=title, director=director)