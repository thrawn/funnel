import psycopg2
import os

try:
    #connect_str = "dbname='postgres' user='postgres' host='localhost' " + \
    #              "password=os.environ['DB_PASSWORD'] port=5432"
    # use our connection values to establish a connection

    DATABASE_URL = os.environ['DATABASE_URL']

    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    #conn = psycopg2.connect(connect_str)
    # create a psycopg2 cursor that can execute queries
    cursor = conn.cursor()
    # create a new table with a single column called "name"
    #cursor.execute("""CREATE TABLE tutorials (name char(40));""")
    # run a SELECT statement - no data in there, but we can try it
    cursor.execute("SELECT 5+5 as test1")
    print(cursor.fetchone())
    #rows = cursor.fetchall()
    #print(rows)
except Exception as e:
    print("Uh oh, can't connect. Invalid dbname, user or password?")
    print(e)
