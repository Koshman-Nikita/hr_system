# Імпортуємо потрібні класи та об'єкти з інших модулів
from models import User, Resume, Hobby, PreviousJob
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Налаштування з'єднання з базою даних
engine = create_engine('sqlite:///hr_system.db')
Session = sessionmaker(bind=engine)
session = Session()

# Функція для отримання резюме за ідентифікатором користувача
def get_resumes_by_user_id(user_id):
    return session.query(Resume).filter(Resume.user_id == user_id).all()

# Функція для отримання хоббі конкретного користувача
def get_hobbies_by_user_id(user_id):
    return session.query(Hobby).join(Resume.hobbies).filter(Resume.user_id == user_id).all()

# Функція для отримання усіх хоббі з усіх резюме
def get_all_hobbies():
    return session.query(Hobby).distinct().all()

# Функція для отримання усіх міст з усіх резюме
def get_all_cities():
    return session.query(Resume.city).distinct().all()

# Функція для отримання хоббі здобувачів за містом
def get_hobbies_by_city(city):
    return session.query(Hobby).join(Resume.hobbies).filter(Resume.city == city).distinct().all()

# Функція для отримання здобувачів, що працювали в певному закладі
def get_users_by_institution(institution_name):
    return session.query(User).join(Resume).join(PreviousJob).filter(PreviousJob.institution_name == institution_name).distinct().all()

# Приклад виклику функції (розкоментуйте для використання)
resumes = get_resumes_by_user_id(1)
for resume in resumes:
    print(resume.city, resume.user.login)

# Приклад завершення роботи з сесією (збереження змін і закриття з'єднання)
session.commit()
session.close()
