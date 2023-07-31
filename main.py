from API import save_vac_json
from DB import create_and_insert_BD
from DBManager import db_m

if __name__ == "__main__":
    save_vac_json()
    create_and_insert_BD()
    db_m.get_vacancies_with_higher_salary()
