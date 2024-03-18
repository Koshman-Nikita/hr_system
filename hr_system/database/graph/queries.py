from py2neo import Graph
from models import User, Resume, Hobby, PreviousJob

# Встановлення з'єднання з Neo4j
graph = Graph("bolt://localhost:7687", auth=("neo4j", "your_password"))

def get_resumes_by_user_login(login):
    query = """
    MATCH (u:User {login: $login})-[:HAS_RESUME]->(r:Resume)
    RETURN r
    """
    return graph.run(query, login=login).data()

def get_hobbies_by_user_login(login):
    query = """
    MATCH (u:User {login: $login})-[:HAS_RESUME]->(:Resume)-[:INTERESTED_IN]->(h:Hobby)
    RETURN h.name AS hobby
    """
    return graph.run(query, login=login).data()

def get_all_hobbies():
    query = """
    MATCH (:Resume)-[:INTERESTED_IN]->(h:Hobby)
    RETURN DISTINCT h.name AS hobby
    """
    return graph.run(query).data()

def get_all_cities():
    query = """
    MATCH (r:Resume)-[:LOCATED_IN]->(c:City)
    RETURN DISTINCT c.name AS city
    """
    return graph.run(query).data()

def get_hobbies_by_city(city_name):
    query = """
    MATCH (:Resume)-[:LOCATED_IN]->(c:City {name: $city_name})<-[:LOCATED_IN]-(r:Resume)-[:INTERESTED_IN]->(h:Hobby)
    RETURN DISTINCT h.name AS hobby
    """
    return graph.run(query, city_name=city_name).data()

def get_users_by_institution(institution_name):
    query = """
    MATCH (u:User)-[:HAS_RESUME]->(:Resume)-[:HAS_WORKED_AT]->(j:PreviousJob {institution_name: $institution_name})
    RETURN DISTINCT u.login AS userLogin
    """
    return graph.run(query, institution_name=institution_name).data()
