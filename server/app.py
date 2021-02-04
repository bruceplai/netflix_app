import os
import logging

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

@app.get('/titles')
def get_titles():
  return cltr.get_titles()

@app.get('/title/{id}')
def get_title(id: str):
  return cltr.get_title(id)

if __name__ == '__main__':
  import uvicorn
  uvicorn.run(app, host='0.0.0.0', port=9090)