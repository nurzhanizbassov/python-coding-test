from typing import List
from fastapi import FastAPI, status
from src.company_data import (
    CompanyDataCheckRequest,
    CompanyDataItem,
)
from src.company_data_check_service import company_data_check_service

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post(
    "/upload-data",
    response_model=List[CompanyDataItem],
    status_code=status.HTTP_200_OK,
)
def upload_data(
    request: CompanyDataCheckRequest,
):
    return company_data_check_service.check_data(
        file_path=request.file_path,
    )
