from models import User, Resume, Hobby, PreviousJob
def get_resumes_by_user_login(login):
    user = User.objects(login=login).first()
    if user:
        return user.resumes
    return None

def get_hobbies_by_user_login(login):
    user = User.objects(login=login).first()
    if user:
        hobbies = set()
        for resume in user.resumes:
            for hobby in resume.hobbies:
                hobbies.add(hobby.name)
        return list(hobbies)
    return None

def get_all_hobbies():
    hobbies = set(Hobby.objects.all().values_list('name', flat=True))
    return list(hobbies)

def get_all_cities():
    users = User.objects()
    cities = set()
    for user in users:
        for resume in user.resumes:
            cities.add(resume.city)
    return list(cities)

def get_hobbies_by_city(city):
    users = User.objects(resumes__city=city)
    hobbies = set()
    for user in users:
        for resume in user.resumes:
            if resume.city == city:
                for hobby in resume.hobbies:
                    hobbies.add(hobby.name)
    return list(hobbies)

def get_users_by_institution(institution_name):
    users_with_institution = []
    for user in User.objects(resumes__previous_jobs__institution_name=institution_name):
        if any(job.institution_name == institution_name for resume in user.resumes for job in resume.previous_jobs):
            users_with_institution.append(user.login)
    return users_with_institution
