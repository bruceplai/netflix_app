import os
import logging

from typing import Optional
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from controller import Controller

logger = logging.getLogger('app')

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

@app.get('/')
def get_base():
  return 'Netflix data server app'

@app.get('/title')
def get_titles(id: Optional[str] = None, title: Optional[str] = None, director: Optional[str] = None):
  if id:
    return cltr.get_title(id)
  return cltr.get_titles(title, director)

@app.get('/year')
def get_years(title: Optional[str] = None, director: Optional[str] = None):
  return cltr.get_years(title, director)

@app.get('/rating')
def get_ratings(title: Optional[str] = None, director: Optional[str] = None):
  return cltr.get_ratings(title, director)

@app.get('/country')
def get_countries(title: Optional[str] = None, director: Optional[str] = None):
  return cltr.get_countries(title, director)

@app.get('/genre')
def get_genres(title: Optional[str] = None, director: Optional[str] = None):
  return cltr.get_genres(title, director)

if __name__ == '__main__':
  import uvicorn
  uvicorn.run(app, host='0.0.0.0', port=9090)