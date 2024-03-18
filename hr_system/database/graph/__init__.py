# hr_system/database/graph/__init__.py

from .queries import (
    get_resumes_by_user_login as graph_get_resumes_by_user_login,
    get_hobbies_by_user_login as graph_get_hobbies_by_user_login,
    get_all_hobbies as graph_get_all_hobbies,
    get_all_cities as graph_get_all_cities,
    get_hobbies_by_city as graph_get_hobbies_by_city,
    get_users_by_institution as graph_get_users_by_institution,
)
