from typing import Any
from pydantic import BaseModel


class CompanyDataCheckRequest(BaseModel):
    file_path: str


class CompanyDataItem(BaseModel):
    field: str
    reported_value: Any
    db_value: Any
    match: bool
