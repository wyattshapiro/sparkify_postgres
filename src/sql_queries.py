# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplay;"
user_table_drop = "DROP TABLE IF EXISTS app_user;"
song_table_drop = "DROP TABLE IF EXISTS song;"
artist_table_drop = "DROP TABLE IF EXISTS artist;"
time_table_drop = "DROP TABLE IF EXISTS time;"

# CREATE TABLES

songplay_table_create = ("""CREATE TABLE IF NOT EXISTS songplay (songplay_id SERIAL PRIMARY KEY, \
                                                                 start_time TIMESTAMP, \
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
                                                         year INTEGER, \
                                                         duration DECIMAL);""")

artist_table_create = ("""CREATE TABLE IF NOT EXISTS artist (artist_id VARCHAR PRIMARY KEY, \
                                                             name VARCHAR, \
                                                             location VARCHAR, \
                                                             latitude DECIMAL, \
                                                             longitude DECIMAL);""")

time_table_create = ("""CREATE TABLE IF NOT EXISTS time (start_time TIMESTAMP, \
                                                         hour INTEGER, \
                                                         day INTEGER, \
                                                         week INTEGER, \
                                                         month INTEGER, \
                                                         year INTEGER, \
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

# ANALYZE TABLES

artist_play_count_all_time = ("""SELECT artist.name, COUNT(songplay.songplay_id) as songplay_count \
                                 FROM songplay \
                                 JOIN artist ON songplay.artist_id = artist.artist_id \
                                 GROUP BY artist.name \
                                 ORDER BY songplay_count DESC;""")

song_play_count_all_time = ("""SELECT song.title, COUNT(songplay.songplay_id) as songplay_count \
                               FROM songplay \
                               JOIN song ON songplay.song_id = song.song_id \
                               GROUP BY song.title \
                               ORDER BY songplay_count DESC;""")

user_by_level = ("""SELECT level as user_level, COUNT(user_id) as user_count \
                    FROM app_user \
                    GROUP BY level \
                    ORDER BY user_count DESC;""")

song_play_count_by_user_level = ("""SELECT app_user.level as user_level, COUNT(songplay.songplay_id) as songplay_count \
                                    FROM songplay \
                                    JOIN app_user ON songplay.user_id = app_user.user_id \
                                    GROUP BY app_user.level \
                                    ORDER BY songplay_count DESC;""")

song_play_count_by_location = ("""SELECT location as songplay_location, COUNT(songplay_id) as songplay_count \
                                  FROM songplay \
                                  GROUP BY location \
                                  ORDER BY songplay_count DESC \
                                  LIMIT 5;""")

song_play_count_daily_by_hour = ("""SELECT time.hour as hour_of_day, COUNT(songplay.songplay_id) as songplay_count \
                                    FROM songplay \
                                    JOIN time ON songplay.start_time = time.start_time \
                                    GROUP BY time.hour \
                                    ORDER BY songplay_count DESC \
                                    LIMIT 5;""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]
analyze_table_queries = [artist_play_count_all_time, song_play_count_all_time, user_by_level, song_play_count_by_user_level, song_play_count_by_location, song_play_count_daily_by_hour]
