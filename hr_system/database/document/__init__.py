# hr_system/database/document/__init__.py

from .queries import (
    get_resumes_by_user_login as doc_get_resumes_by_user_login,
    get_hobbies_by_user_login as doc_get_hobbies_by_user_login,
    get_all_hobbies as doc_get_all_hobbies,
    get_all_cities as doc_get_all_cities,
    get_hobbies_by_city as doc_get_hobbies_by_city,
    get_users_by_institution as doc_get_users_by_institution,
)
