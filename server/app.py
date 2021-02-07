"""
Netflix data API app
"""

import os
import logging

from typing import List, Optional
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from controller import Controller
from title import Title
from data_point import DataPoint

app = FastAPI()
cltr = Controller()

origins = [
  'http://localhost:4200'
]

app.add_middleware(
  CORSMiddleware,
  allow_origins=origins,
  allow_credentials=True,
  allow_methods=['*'],
  allow_headers=['*']
)

logger = logging.getLogger('app')
app_path = os.path.abspath(__file__)
app_dir = os.path.dirname(app_path)
os.chdir(app_dir)
if 'APP_ENV' in os.environ and os.environ['APP_ENV'].lower() == 'dev':
    logger.setLevel(logging.DEBUG)

@app.get('/')
async def get_base():
  return 'Netflix data app'

@app.get('/title')
async def get_titles(
  id: Optional[str] = None,
  title: Optional[str] = None,
  director: Optional[str] = None,
  actor: Optional[str] = None
) -> List[Title]:
  if id:
    return [cltr.model.get_title(id)]
  return cltr.model.get_titles(title, director, actor)

@app.get('/year')
async def get_years(
  title: Optional[str] = None,
  director: Optional[str] = None,
  actor: Optional[str] = None
) -> List[DataPoint]:
  return cltr.model.get_years(title, director, actor)

@app.get('/rating')
async def get_ratings(
  title: Optional[str] = None,
  director: Optional[str] = None,
  actor: Optional[str] = None
) -> List[DataPoint]:
  return cltr.model.get_ratings(title, director, actor)

@app.get('/country')
async def get_countries(
  title: Optional[str] = None,
  director: Optional[str] = None,
  actor: Optional[str] = None
) -> List[DataPoint]:
  return cltr.model.get_countries(title, director, actor)

@app.get('/genre')
async def get_genres(
  title: Optional[str] = None,
  director: Optional[str] = None,
  actor: Optional[str] = None
) -> List[DataPoint]:
  return cltr.model.get_genres(title, director, actor)

if __name__ == '__main__':
  import uvicorn
  uvicorn.run(app, host='0.0.0.0', port=9090)