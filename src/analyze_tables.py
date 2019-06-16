import psycopg2
from sql_queries import analyze_table_queries
from config import DB_HOST, DB_PORT, DB_USER, DB_PASSWORD, DB_NAME_DEFAULT, DB_NAME_SPARKIFY

def connect_database():

    # connect to sparkify database
    conn = psycopg2.connect("host={} port={} dbname={} user={} password={}".format(DB_HOST, DB_PORT, DB_NAME_SPARKIFY, DB_USER, DB_PASSWORD))
    cur = conn.cursor()

    return cur, conn


def run_query(query, cur, conn):
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
    cur, conn = connect_database()

    for query in analyze_table_queries:
        run_query(query, cur, conn)


if __name__ == "__main__":
    main()
