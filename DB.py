import json

import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="mydatabase",
    user="postgres",
    password="1234"
)

with psycopg2.connect(
        host="localhost",
        database="mydatabase",
        user="postgres",
        password="1234") as conn:
    with conn.cursor() as cur:
        with open('company.json') as my_file:
            data = json.load(my_file)
            cur.execute(""" create table if not exists companies(
                id integer, name text, type text, description text,
                open_vacancies text) """)
            query_sql = """ insert into json_table
                select * from json_populate_recordset(NULL::companies, %s) """
            cur.execute(query_sql, (json.dumps(data),))
