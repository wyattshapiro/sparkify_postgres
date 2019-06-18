import psycopg2
from sql_queries import analyze_table_queries
from config import DB_HOST, DB_PORT, DB_USER, DB_PASSWORD, DB_NAME_DEFAULT, DB_NAME_SPARKIFY


def connect_database():
    """Connect to default database.

    Return
        cur: cursor object, cursor bound to the connection that allows PostgreSQL to execute
        conn: connection object, connection to a PostgreSQL database instance

    """
    # connect to sparkify database
    conn = psycopg2.connect("host={} port={} dbname={} user={} password={}".format(DB_HOST, DB_PORT, DB_NAME_SPARKIFY, DB_USER, DB_PASSWORD))
    cur = conn.cursor()

    return cur, conn


def run_query(query, cur, conn):
    """Run a query on an existing table in the database.

    Args
        query: string, SELECT query in PostgreSQL
        cur: cursor object, cursor bound to the connection that allows PostgreSQL to execute
        conn: connection object, connection to a PostgreSQL database instance

    """
    cur.execute(query)
    conn.commit()

    column_headers = []
    for column in cur.description:
        field_name = column[0]
        column_headers.append(field_name)
    print(column_headers)

    row = cur.fetchone()
    while row:
       print(row)
       row = cur.fetchone()

    print('-' * 5)


def main():
    """Connect to a database and run SELECT queries, as specified in analyze_table_queries."""
    cur, conn = connect_database()

    for query in analyze_table_queries:
        run_query(query, cur, conn)


if __name__ == "__main__":
    main()
