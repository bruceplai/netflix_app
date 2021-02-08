# Netflix Explorer Application

This application is a proof of concept that allows browse through data for thousands of Netflix titles
and look at a few statistics on them (such as number titles by release year).  The data source is from
<a href="https://www.kaggle.com/shivamb/netflix-shows/data">Kaggle</a>.

## Overall architecture

The appication is split into db, server, and client parts.  The db part consists of the raw data in CSV format
and a simple script to do some light processing and importing into SQLite.  The server side is based on Python
and <a href="https://fastapi.tiangolo.com/">FastAPI</a> with a <a href="https://www.uvicorn.org/">Uvicorn</a> 
HTTP server.  The client side is built in <a href="https://angular.io/">Angular</a> and relies on the 
Angular Material library for its look and feel.

### DB

SQLite was chosen as the DB because of native support in Python and quick prototyping.  Pandas was used
as a helper library to rename columns so that they would not have to be remapped on the client side.
Data is stored in the 'titles' table in 'netflix.db'.

### Server

The entry point for the server is app.py, which has endpoint handling for returning titles, release years, 
ratings, release countries, and genres.  Title data is essentially rows of titles table, while the rest of data
is returned as counts grouped by release year, rating, etc.  This is due to the way the client consumes the data.
All APIs allow for optional filtering parameters (partial/full title, partial/full director, partial/full actor),
with titles allowing for search by the additional 'id' parameter which matches unique IDs in the titles table.

### Client

The client consists of a table to explore all titles, with expandable rows to show more detailed info as well as 
a simple dashboard.  The dashboard allows the user to filter by title, director, and actor/actress.  Bar charts
for genre, year released, and country released are displayed.

## Installation and Setup

The steps below apply to localhost installation.
For quick install, it is assumed that you have docker and docker-compose installed.
For manual steps look at the Manual Setup section

### Setup with Docker

```bash
docker-compose build
docker-compose up
```
The server and client will be available on port 9090 and 80 of localhost.  Nginx is the client server. 

### Manual Setup

First import data.  Go into the db directory.
```bash
python import_data.py
```

Go into the server directory and install dependencies for the server.
Run the server.
```bash
python install -r requirements.txt
./run.sh -d
```

Go into the client directory and install dependencies for the client.
Run the client.
```bash
npm i -g @angular/cli@latest
npm i
ng serve
```
The server and client will be available on port 9090 and 4200 of localhost.

## Future enhancements
-SSL support
-Implement login for dashboard
-Add poster images to title details
