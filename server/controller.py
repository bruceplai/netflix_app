
import sqlite3

class Controller:
  """
  Application controller
  """
  def __init__(self) -> None:
    self.db_file = '/tmp/db/netflix.db'

  def get_titles(self):
    """
    Get data for all titles
    """
    results = []
    db_conn = sqlite3.connect(self.db_file)
    with db_conn:
      cur = db_conn.cursor()
      query = cur.execute("SELECT * FROM titles")

      colnames = [des[0] for des in query.description]
      for row in cur.fetchall():
        row_dict = {}
        for i in range(len(colnames)):
          row_dict[colnames[i]] = row[i]
        results.append(row_dict)
    return results
  
  def get_title(self, id: str):
    """
    Get title data by id, which is matched to show_id in the titles table
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
