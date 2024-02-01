from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine(
    "postgresql://postgres:postgres@localhost:5432/postgres", echo=False
)

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()


class Student(Base):
    __tablename__ = "student"
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    age = Column(Integer)
    grade = Column(String(50))


Base.metadata.create_all(engine)

student1 = Student(name="Nuri", age=27, grade="Fifth")

session.add(student1)
session.commit()
