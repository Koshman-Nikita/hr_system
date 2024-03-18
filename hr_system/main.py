import sys
sys.path.append('D:/projects/hr_system')

from models.user import User
from models.resume import Resume
from models.hobby import Hobby
from models.previous_job import PreviousJob

import sys
sys.path.append('D:/projects/hr_system')

# Імпорт функцій запитів для роботи з реляційною, документною та графовою базами даних
from database.relational import (
    get_resumes_by_user_id,
    get_hobbies_by_user_id,
    get_all_hobbies as get_all_hobbies_relational,
    get_all_cities as get_all_cities_relational,
    get_hobbies_by_city as get_hobbies_by_city_relational,
    get_users_by_institution as get_users_by_institution_relational,
)

from database.document import (
    doc_get_resumes_by_user_login,
    doc_get_hobbies_by_user_login,
    doc_get_all_hobbies,
    doc_get_all_cities,
    doc_get_hobbies_by_city,
    doc_get_users_by_institution,
)

from database.graph import (
    graph_get_resumes_by_user_login,
    graph_get_hobbies_by_user_login,
    graph_get_all_hobbies,
    graph_get_all_cities,
    graph_get_hobbies_by_city,
    graph_get_users_by_institution,
)

def main():
    print("1. Relational Database Queries")
    # Приклади реляційної БД
    print("\nGetting resumes by user ID:")
    print(get_resumes_by_user_id(1))
    print("\nGetting hobbies by user ID:")
    print(get_hobbies_by_user_id(1))
    print("\nGetting all hobbies:")
    print(get_all_hobbies_relational())
    print("\nGetting all cities from resumes:")
    print(get_all_cities_relational())
    print("\nGetting hobbies by city name 'Kyiv':")
    print(get_hobbies_by_city_relational('Kyiv'))
    print("\nGetting users who worked at 'Global Corp':")
    print(get_users_by_institution_relational('Global Corp'))

    print("2. Document Database Queries")
    # Приклади документної БД
    print("\nGetting resumes by user login:")
    print(doc_get_resumes_by_user_login('john_doe'))
    print("\nGetting hobbies by user login:")
    print(doc_get_hobbies_by_user_login('john_doe'))
    print("\nGetting all hobbies in the database:")
    print(doc_get_all_hobbies())
    print("\nGetting all cities from resumes:")
    print(doc_get_all_cities())
    print("\nGetting hobbies for users in 'Kyiv':")
    print(doc_get_hobbies_by_city('Kyiv'))
    print("\nGetting users who worked at 'Global Corp':")
    print(doc_get_users_by_institution('Global Corp'))

    print("3. Graph Database Queries")
    # Приклади графової БД
    print("\nGetting resumes by user login:")
    print(graph_get_resumes_by_user_login('john_doe'))
    print("\nGetting hobbies by user login:")
    print(graph_get_hobbies_by_user_login('john_doe'))
    print("\nGetting all hobbies in the database:")
    print(graph_get_all_hobbies())
    print("\nGetting all cities from resumes:")
    print(graph_get_all_cities())
    print("\nGetting hobbies for users in 'Kyiv':")
    print(graph_get_hobbies_by_city('Kyiv'))
    print("\nGetting users who worked at 'Global Corp':")
    print(graph_get_users_by_institution('Global Corp'))

if __name__ == "__main__":
    main()