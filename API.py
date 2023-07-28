import json

import requests


def employee_api():
    employee_id = [1740, 5814433, 55590, 32918, 24241, 16498, 77365, 20496, 80981, 40714]
    all_emp = []
    for item in employee_id:
        response = requests.get(f"https://api.hh.ru/employers/{item}")
        resp_j = response.json()
        all_emp.append(resp_j)
    return all_emp


def vacancies_api():
    employee_id = [1740, 5814433, 55590, 32918, 24241, 16498, 77365, 20496, 80981, 40714]
    all_vacancies = []
    for item in employee_id:
        response = requests.get(f"https://api.hh.ru/vacancies?employer_id={item}")
        resp_j = response.json()
        all_vacancies.append(resp_j)
    return all_vacancies


def save_emp_json():
    with open('company.json', 'w', encoding='utf-8') as file:
        json.dump(employee_api(), file, ensure_ascii=False, indent=4)


def open_emp_json():
    with open('company.json', 'r', encoding='utf-8') as file:
        return json.load(file)

def save_vac_json():
    with open('vacancies.json', 'w', encoding='utf-8') as file:
        json.dump(vacancies_api(), file, ensure_ascii=False, indent=4)


def open_vac_json():
    with open('vacancies.json', 'r', encoding='utf-8') as file:
        return json.load(file)

save_vac_json()