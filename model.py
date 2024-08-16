from sqlalchemy import Column, String, Integer, Date, ForeignKey, Float
from sqlalchemy.orm import relationship
from database import Base


class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))
    surname = Column(String(100))
    email = Column(String(100), unique=True, index=True)
    phone = Column(String(20))
    position = Column(String(50))
    salary = Column(Float)
    hire_date = Column(Date)
    address = Column(String(200))
    project_id = Column(Integer, ForeignKey('projects.id'))

    project = relationship("Project", back_populates="employees")


class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))
    description = Column(String(200))
    start_date = Column(Date)
    end_date = Column(Date)
    completion_percentage = Column(Float)

    employees = relationship("Employee", back_populates="project")
