from pydantic import BaseModel

class EmployeeBase(BaseModel):
    employee_name: str
    role: str
    department: str

class EmployeeCreate(EmployeeBase):
    pass

class Employee(EmployeeBase):
    employee_id: int

    class Config:
        from_attributes = True



