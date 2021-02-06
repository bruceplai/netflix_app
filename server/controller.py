
import sqlite3

class Controller:
  """
  Application controller
  """
  def __init__(self) -> None:
    self.db_file = '/tmp/db/netflix.db'
  
  def get_title(self, id: str):
    """
    Get title data by id, which is matched to id in the titles table
    """
    db_conn = sqlite3.connect(self.db_file)
    with db_conn:
      cursor = db_conn.cursor()
      query = cursor.execute("SELECT * FROM titles WHERE show_id = ?", [id])

      colnames = [des[0] for des in query.description]
      result = cursor.fetchone()
      if not result:
        return None
      result_dict = {}
      for i in range(len(colnames)):
        result_dict[colnames[i]] = result[i]
    return result_dict

  def get_titles(self, title, director):
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
        row_dict = {}
        for i in range(len(colnames)):
          row_dict[colnames[i]] = row[i]
        results.append(row_dict)
    return results

  def get_years(self, title, director):
    """
    Get release year data for partial title and/or director matches.
    """
    results = []
    query_addon = []
    if title:
      query_addon.append(f"title LIKE '%{title}%'")
    if director:
      query_addon.append(f"director LIKE '%{director}%'")
    if query_addon:
      query_addon = " WHERE " + " AND ".join(query_addon)
    db_conn = sqlite3.connect(self.db_file)
    with db_conn:
      cur = db_conn.cursor()
      if query_addon:
        query = cur.execute(
          "SELECT releaseYear AS name, COUNT(releaseYear) AS value \
          FROM titles"
          + query_addon +
          " GROUP BY releaseYear"
        )
      else:
        query = cur.execute(
          "SELECT releaseYear AS name, COUNT(releaseYear) AS value \
          FROM titles \
          GROUP BY releaseYear"
        )
      colnames = [des[0] for des in query.description]
      for row in cur.fetchall():
        row_dict = {}
        for i in range(len(colnames)):
          row_dict[colnames[i]] = row[i]
        results.append(row_dict)
    return results

  def get_ratings(self, title, director):
    """
    Get rating data for partial title and/or director matches.
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
        query = cur.execute(
          "SELECT rating AS name, COUNT(rating) AS value \
          FROM titles \
          WHERE rating IS NOT NULL AND " + query_addon +
          " GROUP BY rating"
        )
      else:
        query = cur.execute(
          "SELECT rating AS name, COUNT(rating) AS value \
          FROM titles \
          WHERE rating IS NOT NULL \
          GROUP BY rating"
        )
      colnames = [des[0] for des in query.description]
      for row in cur.fetchall():
        row_dict = {}
        for i in range(len(colnames)):
          row_dict[colnames[i]] = row[i]
        results.append(row_dict)
    return results

  def get_countries(self, title, director):
    """
    Get release country data for partial title and/or director matches.
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
        cur.execute("SELECT country FROM titles WHERE country IS NOT NULL AND " + query_addon)
      else:
        cur.execute("SELECT country FROM titles WHERE country IS NOT NULL")
      countries = {}
      for row in cur.fetchall():
        country_list = row[0].split(',')
        for country in country_list:
          country = country.strip()
          if country not in countries:
            countries[country] = 1
          else:
            countries[country] += 1
    for item in countries.items():
      results.append({'name': item[0], 'value': item[1]})
    return results

  def get_genres(self, title, director):
    """
    Get release country data for partial title and/or director matches.
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
        cur.execute("SELECT genre FROM titles WHERE genre IS NOT NULL AND " + query_addon)
      else:
        cur.execute("SELECT genre FROM titles WHERE genre IS NOT NULL")
      countries = {}
      for row in cur.fetchall():
        country_list = row[0].split(',')
        for country in country_list:
          country = country.strip()
          if country not in countries:
            countries[country] = 1
          else:
            countries[country] += 1
    for item in countries.items():
      results.append({'name': item[0], 'value': item[1]})
    return results