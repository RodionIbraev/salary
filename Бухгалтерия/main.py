from application.salary import calculate_salary
from application.people import get_employees
from datetime import datetime as dt


if '__main__' == __name__:
    print(dt.today().date())
    calculate_salary()
    get_employees()