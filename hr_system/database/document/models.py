from mongoengine import Document, StringField, ListField, ReferenceField, EmbeddedDocument, EmbeddedDocumentListField, connect

connect('hr_system')

class Hobby(Document):
    name = StringField(required=True, unique=True)

class PreviousJob(EmbeddedDocument):
    city = StringField(required=True)
    institution_name = StringField(required=True)

class Resume(EmbeddedDocument):
    city = StringField(required=True)
    hobbies = ListField(ReferenceField(Hobby))
    previous_jobs = EmbeddedDocumentListField(PreviousJob)

class User(Document):
    login = StringField(required=True, unique=True)
    password = StringField(required=True)
    resumes = EmbeddedDocumentListField(Resume)
