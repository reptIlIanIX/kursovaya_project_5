CREATE TABLE vacancies
(
    vacancies_id int PRIMARY KEY,
    name text,
    employer_id int)

SELECT DISTINCT employer_name, COUNT(vacancies_id) FROM vacancies