
# Data Modeling with Postgres for Sparkify

## Goal

Sparkify has been collecting on songs and user activity for their new music streaming app. One of their teams is interested in analyzing their users listening habits, which could help them classify their users for targeted ads, create/improve a recommendation algorithm for songs, and more. They are especially interested in the songs that users are playing.

Note: This project is for a fictional company and is part of Udacity's Data Engineering Nanodegree.

### Problem

Currently, Sparkify's user history and song data is stored in JSON log formats.
This format does not lend itself well to analysis.

### Solution

In order to enable a team to effectively gain insight from user activity, a data engineer needs to structure the data and load it into a database. The proposed plan consists of a Python ETL pipeline that will:

- Extract each JSON file into a pandas dataframe.
- Transform and load the data into a Postgres database with a star schema built to optimize for analysis of song plays.

## Data

### Song Dataset

- This dataset is a subset of real song data from the Million Song Dataset.
- Each file is in JSON format and contains metadata about a song and the artist of that song.
  - The files are partitioned by the first three letters of each song's track ID. For example:
    - song_data/A/B/C/TRABCEI128F424C983.json
    - song_data/A/A/B/TRAABJL12903CDCF1A.json

### Log Dataset

- This dataset is event data generated by an event simulator based on the songs in the dataset above.
- Each file is in JSON format and contains data about user events in the app.
  - The files are partitioned by year and month. For example:
    - log_data/2018/11/2018-11-12-events.json
    - log_data/2018/11/2018-11-13-events.json


## Data Models

### Entities

The database is structured as a star schema for analysis of song plays. As such, the fact table (ie center of the star) will be songplays, and it will have it's associated dimensions related as foreign keys.

Fact table
- songplays: records in log data associated with song plays

Dimension tables
- app_users: users in the app
- songs: songs in music database
- artists: artists in music database
- time: timestamps of records in songplays broken down into specific units

### Entity Relationship Diagram (ERD)

![Alt text](sparkify_ERD.png?raw=true "Sparkify ERD")


## Installation

Clone the repo onto your machine with the following command:

$ git checkout https://github.com/wyattshapiro/sparkify_postgres.git


## Dependencies

I use Python 3.7.

See https://www.python.org/downloads/ for information on download.

----

I use virtualenv to manage dependencies, if you have it installed you can run
the following commands from the root code directory to create the environment and
activate it:

$ python3 -m venv venv

$ source venv/bin/activate

See https://virtualenv.pypa.io/en/stable/ for more information.

----

I use pip to install dependencies, which comes installed in a virtualenv.
You can run the following to install dependencies:

$ pip install -r requirements.txt

See https://pip.pypa.io/en/stable/installing/ for more information.

----

I use a locally hosted PostgreSQL database.

See https://www.postgresql.org/ for more information.


## Usage

There are several main scripts:

- src/config.py: Specifies environmental variables for db connection. Storing credentials like this is not recommended. It is better practice to set as environmental variables and dynamically retrieve them.
- src/create_tables.py: Drops and creates your tables. You run this file to reset your tables before each time you run your ETL scripts.
  - src/test.ipynb: Displays the first few rows of each table to let you check your database.
- src/etl.py: Reads and processes *all files* from song_data and log_data and loads them into your tables.
  - src/etl.ipynb: For development. Reads and processes a *single file* from song_data and log_data and loads the data into your tables.
- src/analyze_tables.py: Runs queries on Postgres db to surface analytical insights.
- src/sql_queries.py: Contains all your sql queries, and is used during ETL process and analysis.

**Steps to run**
1. Navigate to top of project directory
2. Create virtualenv (see Dependencies)
3. Activate virtualenv (see Dependencies)
4. Install requirements (see Dependencies)
5. Start local postgres server (see Dependencies)
6. Configure src/config.py for postgres user
7. $ python3 src/create_tables.py
8. $ python3 src/etl.py
9. $ python3 src/analyze_tables.py

## Analysis

In src/analyze_tables.py, I created several example queries. These queries showed that:
- There are close to four times as many free users as paid users. However, paid users account for close to 80% of song plays.
- Users appear to play songs from all over the US.
- Song plays are highest from 9am-1pm.

## Future Optimizations

- Insert data using the COPY command to bulk insert log files instead of using INSERT on one row at a time
- Add data quality checks
- Create a dashboard for analytic queries
