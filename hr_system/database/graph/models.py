from py2neo.ogm import GraphObject, Property, RelatedTo, RelatedFrom

class User(GraphObject):
    __primarykey__ = "login"

    login = Property()
    password = Property()

    # Відносини один до багатьох з Резюме
    resumes = RelatedTo("Resume", "HAS_RESUME")

class Resume(GraphObject):
    __primarykey__ = "id"

    id = Property()
    # Місто не є окремим вузлом у цьому прикладі, але ви можете додати його як Property, якщо не потрібен вузол City
    city = Property()

    # Відносини багато до багатьох з Хобі
    hobbies = RelatedTo("Hobby", "INTERESTED_IN")

    # Відносина один до багатьох з Попередніми Місцями Роботи (кожне резюме може мати кілька попередніх місць роботи)
    previous_jobs = RelatedTo("PreviousJob", "HAS_WORKED_AT")

    # Зворотній зв'язок до Користувача
    owner = RelatedFrom("User", "HAS_RESUME")

class Hobby(GraphObject):
    __primarykey__ = "name"

    name = Property()

    # Зворотній зв'язок до Резюме
    resumes = RelatedFrom("Resume", "INTERESTED_IN")

class PreviousJob(GraphObject):
    __primarykey__ = "institution_name"

    institution_name = Property()
    city = Property()

    # Зворотній зв'язок до Резюме
    resumes = RelatedFrom("Resume", "HAS_WORKED_AT")
