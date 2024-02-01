from sqlalchemy import create_engine, Column, Integer, String, MetaData
from sqlalchemy.orm import declarative_base, Session
from sqlalchemy import or_

# PostgreSQL veritabanı bağlantı URL'si
db_url = "postgresql://postgres:postgres@localhost:5432/postgres"

# SQLAlchemy engine oluştur
engine = create_engine(db_url)

# SQLAlchemy Base sınıfını oluştur
Base = declarative_base()


# "student" tablosu için model
class Student(Base):
    __tablename__ = "student"
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    age = Column(Integer)
    grade = Column(String(50))


# MetaData nesnesini oluştur
metadata = MetaData()

# Modeli bağlı olduğun veritabanındaki tabloya eşleştir
Base.metadata.bind = engine
metadata.reflect(bind=engine)

# Session oluştur
session = Session(engine)


#delete operation
student1 = session.query(Student).filter(Student.name == "Nuri").first()
session.delete(student1)
session.commit()


#Yukarıda yapılan işlemin sonucunu
#Aşağıdaki kod ile görüntülersen Nuri isimli satırın silindiğini görürsün.
students = session.query(Student)
for student in students:
    print(student.name, student.age, student.grade)



