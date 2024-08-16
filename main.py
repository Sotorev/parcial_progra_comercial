from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import engine, Base, get_db
import crud
import schemas

Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.post("/employees/", response_model=schemas.Employee)
def create_employee(employee: schemas.EmployeeCreate, db: Session = Depends(get_db)):
    return crud.create_employee(db=db, employee=employee)


@app.get("/employees/", response_model=list[schemas.Employee])
def read_employees(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_employees(db=db, skip=skip, limit=limit)


@app.post("/projects/", response_model=schemas.Project)
def create_project(project: schemas.ProjectCreate, db: Session = Depends(get_db)):
    return crud.create_project(db=db, project=project)


@app.get("/projects/", response_model=list[schemas.Project])
def read_projects(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_projects(db=db, skip=skip, limit=limit)


@app.post("/projects/{project_id}/assign/{employee_id}", response_model=schemas.Employee)
def assign_employee(project_id: int, employee_id: int, db: Session = Depends(get_db)):
    return crud.assign_employee_to_project(db=db, employee_id=employee_id, project_id=project_id)


@app.delete("/projects/unassign/{employee_id}", response_model=schemas.Employee)
def unassign_employee(employee_id: int, db: Session = Depends(get_db)):
    return crud.unassign_employee_from_project(db=db, employee_id=employee_id)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
