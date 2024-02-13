from beanie import Document
from pydantic import BaseModel
from typing import Optional

class employee(Document):
    em_emp_id: str
    em_emp_name: str
    em_first_name: str
    em_middle_name: str
    em_last_name: str
    em_position: str
    em_dept_code: str
    em_salespers: bool
