# HR Management API

This is a RESTful API for a Human Resources Management System built using FastAPI and MySQL. The API allows for the management of employees and projects, including the ability to assign employees to projects.

## Features

- Create, read, update, and delete employees.
- Create, read, and update projects.
- Assign employees to projects.
- Ensure that an employee can only work on one project at a time.
- Track project start and end dates, and completion percentage.

## Requirements

- Python 3.8+
- FastAPI
- Uvicorn
- SQLAlchemy
- MySQL
- PyMySQL

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/hr-management-api.git
   cd hr-management-api

2. **Install FastAPI and dependencies**
   pip install "fastapi[standard]"
   pip install sqlalchemy pymysql

3. **Run the api**
   fastapi dev main.py


## API Endpoints
Employees
Create an employee:

POST /employees/
Request Body:
json
Copy code
{
  "name": "John",
  "surname": "Doe",
  "email": "john.doe@example.com",
  "phone": "555-1234",
  "position": "Developer",
  "salary": 60000,
  "hire_date": "2024-08-16",
  "address": "123 Main St, Anytown",
  "project_id": null
}
Read all employees:

GET /employees/
Read a specific employee:

GET /employees/{employee_id}
Update an employee:

PUT /employees/{employee_id}
Request Body:
json
Copy code
{
  "name": "John",
  "surname": "Doe",
  "email": "john.doe@example.com",
  "phone": "555-1234",
  "position": "Developer",
  "salary": 65000,
  "hire_date": "2024-08-16",
  "address": "123 Main St, Anytown",
  "project_id": 1
}
Delete an employee:

DELETE /employees/{employee_id}
Projects
Create a project:

POST /projects/
Request Body:
json
Copy code
{
  "name": "Project Alpha",
  "description": "A new software project",
  "start_date": "2024-08-16",
  "end_date": "2025-02-16",
  "completion_percentage": 0.0
}
Read all projects:

GET /projects/
Read a specific project:

GET /projects/{project_id}
Update a project:

PUT /projects/{project_id}
Request Body:
json
Copy code
{
  "name": "Project Alpha",
  "description": "A new software project",
  "start_date": "2024-08-16",
  "end_date": "2025-02-16",
  "completion_percentage": 50.0
}
Assign an employee to a project:

POST /projects/{project_id}/assign/{employee_id}
Unassign an employee from a project:

DELETE /projects/unassign/{employee_id}
