import sys
sys.path.append('D:/projects/hr_system')

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base()

# Визначення таблиці для зв'язків many-to-many між хоббі та резюме
resume_hobby_link = Table('resume_hobby', Base.metadata,
                          Column('resume_id', Integer, ForeignKey('resumes.id'), primary_key=True),
                          Column('hobby_id', Integer, ForeignKey('hobbies.id'), primary_key=True)
                          )


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    login = Column(String, unique=True)
    password = Column(String)
    resumes = relationship('Resume', back_populates='user')


class Resume(Base):
    __tablename__ = 'resumes'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    city = Column(String)
    user = relationship('User', back_populates='resumes')
    hobbies = relationship('Hobby', secondary=resume_hobby_link, back_populates='resumes')
    jobs = relationship('PreviousJob', back_populates='resume')


class Hobby(Base):
    __tablename__ = 'hobbies'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    resumes = relationship('Resume', secondary=resume_hobby_link, back_populates='hobbies')


class PreviousJob(Base):
    __tablename__ = 'previous_jobs'

    id = Column(Integer, primary_key=True)
    resume_id = Column(Integer, ForeignKey('resumes.id'))
    city = Column(String)
    institution_name = Column(String)
    resume = relationship('Resume', back_populates='jobs')
