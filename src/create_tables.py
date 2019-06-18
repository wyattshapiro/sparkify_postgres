import psycopg2
from sql_queries import create_table_queries, drop_table_queries
from config import DB_HOST, DB_PORT, DB_USER, DB_PASSWORD, DB_NAME_DEFAULT, DB_NAME_SPARKIFY


def create_database():
    """Connect to default database and reset the new database.

    Return
        cur: cursor object, cursor bound to the connection that allows PostgreSQL to execute
        conn: connection object, connection to a PostgreSQL database instance

    """

    # connect to default database
    conn = psycopg2.connect("host={} port={} dbname={} user={} password={}".format(DB_HOST, DB_PORT, DB_NAME_DEFAULT, DB_USER, DB_PASSWORD))
    conn.set_session(autocommit=True)
    cur = conn.cursor()

    # create sparkify database with UTF8 encoding
    cur.execute("DROP DATABASE IF EXISTS {}".format(DB_NAME_SPARKIFY))
    cur.execute("CREATE DATABASE sparkifydb WITH ENCODING 'utf8' TEMPLATE template0")

    # close connection to default database
    conn.close()

    # connect to sparkify database
    conn = psycopg2.connect("host={} port={} dbname={} user={} password={}".format(DB_HOST, DB_PORT, DB_NAME_SPARKIFY, DB_USER, DB_PASSWORD))
    cur = conn.cursor()

    return cur, conn


def drop_tables(cur, conn):
    """Drop the tables in the database as specified by list of queries, drop_table_queries.

    Args
        cur: cursor object, cursor bound to the connection that allows PostgreSQL to execute
        conn: connection object, connection to a PostgreSQL database instance

    """
    for query in drop_table_queries:
        cur.execute(query)
        conn.commit()


def create_tables(cur, conn):
    """Create the tables in the database as specified in list of queries, create_table_queries.

    Args
        cur: cursor object, cursor bound to the connection that allows PostgreSQL to execute
        conn: connection object, connection to a PostgreSQL database instance

    """
    for query in create_table_queries:
        cur.execute(query)
        conn.commit()


def main():
    """Reset the database and it's associated tables."""
    cur, conn = create_database()

    drop_tables(cur, conn)
    create_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()
