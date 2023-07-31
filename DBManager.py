import json

import psycopg2


class DBManager:
    with open('vacancies.json', encoding='utf-8') as f:
        data = json.load(f)
    # connect to the database
    conn = psycopg2.connect(host="localhost", database="postgres", user="postgres", password="Layne8841")

    # create a cursor
    cur = conn.cursor()

    def get_companies_and_vacancies_count(self):
        """получает список всех компаний и количество вакансий у каждой компании."""
        self.cur.execute("SELECT DISTINCT employer_name, COUNT(vacancies_id) FROM vacancies GROUP BY employer_name")
        vacancies = self.cur.fetchall()
        for x in vacancies:
            print(x)

    def get_all_vacancies(self):
        """получает список всех вакансий с указанием названия компании, названия вакансии и зарплаты и ссылки на вакансию."""
        self.cur.execute("SELECT * FROM vacancies")
        vacancies = self.cur.fetchall()
        for x in vacancies:
            print(x)

    def get_avg_salary(self):
        """получает среднюю зарплату по вакансиям."""
        self.cur.execute("SELECT (AVG(salary_to)+AVG(salary_from))/2 FROM vacancies")
        vacancies = self.cur.fetchall()
        for x in vacancies:
            print(x)

    def get_vacancies_with_higher_salary(self):
        """получает список всех вакансий, у которых зарплата выше средней по всем вакансиям."""
        self.cur.execute(
            "SELECT * FROM vacancies WHERE (salary_to + salary_from)/2 > (SELECT (AVG(salary_to)+AVG(salary_from))/2 from vacancies)")
        vacancies = self.cur.fetchall()
        for x in vacancies:
            print(x)

    def get_vacancies_with_keyword(self):
        """получает список всех вакансий, в названии которых содержатся переданные в метод слова, например “python”."""
        self.cur.execute(
            "SELECT * FROM vacancies WHERE vacancy_name in ('Грузчик') ")
        vacancies = self.cur.fetchall()
        for x in vacancies:
            print(x)


db_m = DBManager()
db_m.get_vacancies_with_keyword()
