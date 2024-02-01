from sqlalchemy import create_engine, Column, Integer, String, MetaData
from sqlalchemy.orm import declarative_base, Session

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
    name = Column(String)
    grade = Column(Integer)


# MetaData nesnesini oluştur
metadata = MetaData()

# Modeli bağlı olduğun veritabanındaki tabloya eşleştir
Base.metadata.bind = engine
metadata.reflect(bind=engine)

# Session oluştur
session = Session(engine)

# "student" tablosundaki tüm değerleri çek
students = session.query(Student).all()

# Çekilen verileri ekrana yazdır
for student in students:
    print(f"ID: {student.id}, Name: {student.name}, Grade: {student.grade}")
