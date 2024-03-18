# hr_system/database/relational/__init__.py

from .queries import (
    get_resumes_by_user_id,
    get_hobbies_by_user_id,
    get_all_hobbies as get_all_hobbies_relational,
    get_all_cities as get_all_cities_relational,
    get_hobbies_by_city as get_hobbies_by_city_relational,
    get_users_by_institution as get_users_by_institution_relational,
)
