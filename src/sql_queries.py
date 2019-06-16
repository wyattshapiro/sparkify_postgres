# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplay;"
user_table_drop = "DROP TABLE IF EXISTS app_user;"
song_table_drop = "DROP TABLE IF EXISTS song;"
artist_table_drop = "DROP TABLE IF EXISTS artist;"
time_table_drop = "DROP TABLE IF EXISTS time;"

# CREATE TABLES

songplay_table_create = ("""CREATE TABLE IF NOT EXISTS songplay (songplay_id SERIAL PRIMARY KEY, \
                                                                 start_time VARCHAR, \
                                                                 user_id VARCHAR, \
                                                                 level VARCHAR,\
                                                                 song_id VARCHAR, \
                                                                 artist_id VARCHAR, \
                                                                 session_id VARCHAR, \
                                                                 location VARCHAR, \
                                                                 user_agent VARCHAR);""")

user_table_create = ("""CREATE TABLE IF NOT EXISTS app_user (user_id VARCHAR PRIMARY KEY, \
                                                             first_name VARCHAR, \
                                                             last_name VARCHAR, \
                                                             gender VARCHAR, \
                                                             level VARCHAR);""")

song_table_create = ("""CREATE TABLE IF NOT EXISTS song (song_id VARCHAR PRIMARY KEY, \
                                                         title VARCHAR, \
                                                         artist_id VARCHAR, \
                                                         year VARCHAR, \
                                                         duration DECIMAL);""")

artist_table_create = ("""CREATE TABLE IF NOT EXISTS artist (artist_id VARCHAR PRIMARY KEY, \
                                                             name VARCHAR, \
                                                             location VARCHAR, \
                                                             latitude VARCHAR, \
                                                             longitude VARCHAR);""")

time_table_create = ("""CREATE TABLE IF NOT EXISTS time (start_time TIME, \
                                                         hour VARCHAR, \
                                                         day VARCHAR, \
                                                         week VARCHAR, \
                                                         month VARCHAR, \
                                                         year VARCHAR, \
                                                         weekday VARCHAR);""")

# INSERT RECORDS

songplay_table_insert = ("""INSERT INTO songplay (start_time, user_id, level, song_id, artist_id, session_id, location, user_agent) \
                            VALUES(%s, %s, %s, %s, %s, %s, %s, %s);""")

user_table_insert = ("""INSERT INTO app_user (user_id, first_name, last_name, gender, level) \
                        VALUES(%s, %s, %s, %s, %s) \
                        ON CONFLICT (user_id) \
                        DO NOTHING;""")

song_table_insert = ("""INSERT INTO song (song_id, title, artist_id, year, duration) \
                        VALUES(%s, %s, %s, %s, %s) \
                        ON CONFLICT (song_id) \
                        DO NOTHING;""")

artist_table_insert = ("""INSERT INTO artist (artist_id, name, location, latitude, longitude) \
                          VALUES(%s, %s, %s, %s, %s) \
                          ON CONFLICT (artist_id) \
                          DO NOTHING;""")


time_table_insert = ("""INSERT INTO time (start_time, hour, day, week, month, year, weekday) \
                        VALUES(%s, %s, %s, %s, %s, %s, %s)""")

# FIND SONGS
# Query to find the song ID and artist ID based on the title, artist name, and duration of a song
song_select = ("""SELECT song.song_id, artist.artist_id \
                  FROM song \
                  JOIN artist ON (song.artist_id = artist.artist_id) \
                  WHERE (song.title = %s AND artist.name = %s AND song.duration = %s);""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]
