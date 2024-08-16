from pydantic import BaseModel
from typing import List, Optional
from datetime import date


class EmployeeBase(BaseModel):
    name: str
    surname: str
    email: str
    phone: str
    position: str
    salary: float
    hire_date: date
    address: str
    project_id: Optional[int] = None


class EmployeeCreate(EmployeeBase):
    pass


class Employee(EmployeeBase):
    id: int

    class Config:
        orm_mode = True


class ProjectBase(BaseModel):
    name: str
    description: str
    start_date: date
    end_date: date
    completion_percentage: float


class ProjectCreate(ProjectBase):
    pass


class Project(ProjectBase):
    id: int
    employees: List[Employee] = []

    class Config:
        orm_mode = True
