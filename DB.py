# import json
#
# import psycopg2
#
# with psycopg2.connect(
#         host="localhost",
#         database="hw_5",
#         user="postgres",
#         password="Layne8841") as conn:
#     with conn.cursor() as cur:
#         with open('vacancies.json', encoding='utf-8') as my_file:
#             data = json.load(my_file)
#             new_data = data[0]['items']
#             print(new_data[0]['employer'])
#             cur.execute(""" create table if not exists vacancies(
#                 id integer, name text, employer json ) """)
#             query_sql = """ insert into vacancies
#                     select id, name, employer from json_populate_recordset(NULL::vacancies, %s) """
#             cur.execute(query_sql, (json.dumps(new_data),))


import json
import psycopg2

# read JSON data from file
with open('vacancies.json', encoding='utf-8') as f:
    data = json.load(f)
# connect to the database
conn = psycopg2.connect(host="localhost", database="hw_5", user="postgres", password="Layne8841")



# create a cursor
cur = conn.cursor()
# execute the INSERT statement
for item in data:
    cur.execute("""CREATE TABLE if not exists vacancies
(
    vacancies_id int PRIMARY KEY,
    name text,
    employer_id int) """)

    cur.execute("INSERT INTO vacancies (vacancies_id, name, employer_id) VALUES (%s, %s, %s)",
                (item["id"], item['name'], item['employer']['id']))

conn.commit()

cur.close()
conn.close()
