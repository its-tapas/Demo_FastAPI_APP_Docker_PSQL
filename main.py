from fastapi import FastAPI, Depends, HTTPException, Body
from sqlalchemy.orm import Session
import models, schemas
from database import SessionLocal, engine, Base


app = FastAPI()

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create Employee (POST)
@app.post("/employees/", response_model=schemas.Employee)
def create_employee(emp: schemas.EmployeeCreate, db: Session = Depends(get_db)):
    db_emp = models.Employee(**emp.dict())
    db.add(db_emp)
    db.commit()
    db.refresh(db_emp)
    return db_emp

# Read all Employees (GET)
@app.get("/employees/", response_model=list[schemas.Employee])
def read_employees(db: Session = Depends(get_db)):
    return db.query(models.Employee).all()

# Read single Employee (GET)
@app.get("/employees/{employee_id}", response_model=schemas.Employee)
def read_employee(employee_id: int, db: Session = Depends(get_db)):
    emp = db.query(models.Employee).filter(models.Employee.employee_id == employee_id).first()
    if not emp:
        raise HTTPException(status_code=404, detail="Employee not found")
    return emp

# Update Employee (PUT - full update)
@app.put("/employees/{employee_id}", response_model=schemas.Employee)
def update_employee(employee_id: int, emp_data: schemas.EmployeeCreate, db: Session = Depends(get_db)):
    emp = db.query(models.Employee).filter(models.Employee.employee_id == employee_id).first()
    if not emp:
        raise HTTPException(status_code=404, detail="Employee not found")
    for key, value in emp_data.dict().items():
        setattr(emp, key, value)
    db.commit()
    db.refresh(emp)
    return emp

# Partial Update Employee (PATCH)
@app.patch("/employees/{employee_id}", response_model=schemas.Employee)
def patch_employee(employee_id: int, emp_data: dict = Body(...), db: Session = Depends(get_db)):
    emp = db.query(models.Employee).filter(models.Employee.employee_id == employee_id).first()
    if not emp:
        raise HTTPException(status_code=404, detail="Employee not found")
    
    for key, value in emp_data.items():
        if hasattr(emp, key):
            setattr(emp, key, value)
    
    db.commit()
    db.refresh(emp)
    return emp

# Delete Employee (DELETE)
@app.delete("/employees/{employee_id}")
def delete_employee(employee_id: int, db: Session = Depends(get_db)):
    emp = db.query(models.Employee).filter(models.Employee.employee_id == employee_id).first()
    if not emp:
        raise HTTPException(status_code=404, detail="Employee not found")
    db.delete(emp)
    db.commit()
    return {"detail": "Employee deleted"}



