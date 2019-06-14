# DROP TABLES

time_table_drop = "DROP TABLE time"
user_table_drop = "DROP TABLE user"
artist_table_drop = "DROP TABLE artist"
song_table_drop = "DROP TABLE song"
songplay_table_drop = "DROP TABLE songplay"

# CREATE TABLES

time_table_create = ("""
""")

user_table_create = ("""
""")

artist_table_create = ("""
""")

song_table_create = ("""
""")

songplay_table_create = ("CREATE TABLE songplay (songplay_id INTEGER PRIMARY KEY, \
                                                 user_id INTEGER, \
                                                 song_id INTEGER, \
                                                 artist_id INTEGER, \
                                                 session_id INTEGER, \
                                                 start_time ,\
                                                 level ,\
                                                 location ,\
                                                 user_agent)")



# INSERT RECORDS

songplay_table_insert = ("""
""")

user_table_insert = ("""
""")

song_table_insert = ("""
""")

artist_table_insert = ("""
""")


time_table_insert = ("""
""")

# FIND SONGS

song_select = ("""
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]
