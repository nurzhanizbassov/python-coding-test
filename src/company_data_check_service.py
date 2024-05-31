import csv
from typing import Any, Dict, List, Tuple

from fastapi import HTTPException, status

from src.company_data import (
    CompanyDataItem,
)
from src.constants import (
    CEO,
    COMPANY_NAME,
    DEBT_IN_MILLIONS,
    DEBT_TO_EQUITY_RATIO,
    EBITDA_IN_MILLIONS,
    EBITDA_MARGIN,
    ENTERPRISE_VALUE_IN_MILLIONS,
    EQUITY_IN_MILLIONS,
    INDUSTRY,
    LOCATION,
    MARKET_CAPITALIZATION,
    NET_INCOME_IN_MILLIONS,
    NET_INCOME_MARGIN,
    NUMBER_OF_EMPLOYEES,
    P_E_RATIO,
    REVENUE_GROWTH_RATE,
    REVENUE_IN_MILLIONS,
    ROA_RETURN_ON_ASSETS,
    ROE_RETURN_ON_EQUITY,
)
from src.pdf_service import PdfService


class CompanyDataCheckService:
    def __init__(self):
        self.pdf_service = PdfService(key="TEST_KEY")

    def check_data(
        self,
        file_path: str,
    ) -> List[CompanyDataItem]:
        try:
            company_data_in = self.pdf_service.extract(
                file_path=file_path,
            )
            column_names, raw_data = self._get_data_from_db(
                company_name=company_data_in[COMPANY_NAME],
            )
            return self._construct_company_data(
                company_data_in=company_data_in,
                column_names=column_names,
                raw_data=raw_data,
            )

        except HTTPException as he:
            raise HTTPException(
                status_code=he.status_code,
                detail=he.detail,
            )

        except FileNotFoundError as fe:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=str(fe),
            )

        except Exception:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Something went wrong",
            )

    def _get_data_from_db(
        self,
        company_name: str,
    ) -> Tuple:
        with open("data/database.csv", newline="") as db:
            csv_reader = csv.reader(db)
            column_names = next(csv_reader)
            for row in csv_reader:
                if row[0].lower() == company_name.lower():
                    return column_names, row

    def _construct_company_data(
        self,
        company_data_in: Dict,
        column_names: List[str],
        raw_data: List[Any],
    ) -> List[CompanyDataItem]:
        company_data = []

        if COMPANY_NAME in column_names:
            reported_value = company_data_in.get(COMPANY_NAME)
            db_value = raw_data[column_names.index(COMPANY_NAME)]
            company_data_item = CompanyDataItem(
                field=COMPANY_NAME,
                reported_value=reported_value,
                db_value=db_value,
                match=reported_value == db_value,
            )
            company_data.append(company_data_item)

        if INDUSTRY in column_names:
            reported_value = company_data_in.get(INDUSTRY)
            db_value = raw_data[column_names.index(INDUSTRY)]
            company_data_item = CompanyDataItem(
                field=INDUSTRY,
                reported_value=reported_value,
                db_value=db_value,
                match=reported_value == db_value,
            )
            company_data.append(company_data_item)

        if MARKET_CAPITALIZATION in column_names:
            reported_value = company_data_in.get(MARKET_CAPITALIZATION)
            db_value = float(raw_data[column_names.index(MARKET_CAPITALIZATION)])
            company_data_item = CompanyDataItem(
                field=MARKET_CAPITALIZATION,
                reported_value=reported_value,
                db_value=db_value,
                match=reported_value == db_value,
            )
            company_data.append(company_data_item)
        if REVENUE_IN_MILLIONS in column_names:
            reported_value = company_data_in.get(REVENUE_IN_MILLIONS)
            db_value = float(raw_data[column_names.index(REVENUE_IN_MILLIONS)])
            company_data_item = CompanyDataItem(
                field=REVENUE_IN_MILLIONS,
                reported_value=reported_value,
                db_value=db_value,
                match=reported_value == db_value,
            )
            company_data.append(company_data_item)
        if EBITDA_IN_MILLIONS in column_names:
            reported_value = company_data_in.get(EBITDA_IN_MILLIONS)
            db_value = float(raw_data[column_names.index(EBITDA_IN_MILLIONS)])
            company_data_item = CompanyDataItem(
                field=EBITDA_IN_MILLIONS,
                reported_value=reported_value,
                db_value=db_value,
                match=reported_value == db_value,
            )
            company_data.append(company_data_item)
        if NET_INCOME_IN_MILLIONS in column_names:
            reported_value = company_data_in.get(NET_INCOME_IN_MILLIONS)
            db_value = float(raw_data[column_names.index(NET_INCOME_IN_MILLIONS)])
            company_data_item = CompanyDataItem(
                field=NET_INCOME_IN_MILLIONS,
                reported_value=reported_value,
                db_value=db_value,
                match=reported_value == db_value,
            )
            company_data.append(company_data_item)
        if DEBT_IN_MILLIONS in column_names:
            reported_value = company_data_in.get(DEBT_IN_MILLIONS)
            db_value = float(raw_data[column_names.index(DEBT_IN_MILLIONS)])
            company_data_item = CompanyDataItem(
                field=DEBT_IN_MILLIONS,
                reported_value=reported_value,
                db_value=db_value,
                match=reported_value == db_value,
            )
            company_data.append(company_data_item)
        if EQUITY_IN_MILLIONS in column_names:
            reported_value = company_data_in.get(EQUITY_IN_MILLIONS)
            db_value = float(raw_data[column_names.index(EQUITY_IN_MILLIONS)])
            company_data_item = CompanyDataItem(
                field=EQUITY_IN_MILLIONS,
                reported_value=reported_value,
                db_value=db_value,
                match=reported_value == db_value,
            )
            company_data.append(company_data_item)
        if ENTERPRISE_VALUE_IN_MILLIONS in column_names:
            reported_value = company_data_in.get(ENTERPRISE_VALUE_IN_MILLIONS)
            db_value = float(raw_data[column_names.index(ENTERPRISE_VALUE_IN_MILLIONS)])
            company_data_item = CompanyDataItem(
                field=ENTERPRISE_VALUE_IN_MILLIONS,
                reported_value=reported_value,
                db_value=db_value,
                match=reported_value == db_value,
            )
            company_data.append(company_data_item)
        if P_E_RATIO in column_names:
            reported_value = company_data_in.get(P_E_RATIO)
            db_value = float(raw_data[column_names.index(P_E_RATIO)])
            company_data_item = CompanyDataItem(
                field=P_E_RATIO,
                reported_value=reported_value,
                db_value=db_value,
                match=reported_value == db_value,
            )
            company_data.append(company_data_item)
        if REVENUE_GROWTH_RATE in column_names:
            reported_value = company_data_in.get(REVENUE_GROWTH_RATE)
            db_value = float(raw_data[column_names.index(REVENUE_GROWTH_RATE)])
            company_data_item = CompanyDataItem(
                field=REVENUE_GROWTH_RATE,
                reported_value=reported_value,
                db_value=db_value,
                match=reported_value == db_value,
            )
            company_data.append(company_data_item)
        if EBITDA_MARGIN in column_names:
            reported_value = company_data_in.get(EBITDA_MARGIN)
            db_value = float(raw_data[column_names.index(EBITDA_MARGIN)])
            company_data_item = CompanyDataItem(
                field=EBITDA_MARGIN,
                reported_value=reported_value,
                db_value=db_value,
                match=reported_value == db_value,
            )
            company_data.append(company_data_item)
        if NET_INCOME_MARGIN in column_names:
            reported_value = company_data_in.get(NET_INCOME_MARGIN)
            db_value = float(raw_data[column_names.index(NET_INCOME_MARGIN)])
            company_data_item = CompanyDataItem(
                field=NET_INCOME_MARGIN,
                reported_value=reported_value,
                db_value=db_value,
                match=reported_value == db_value,
            )
            company_data.append(company_data_item)
        if ROE_RETURN_ON_EQUITY in column_names:
            reported_value = company_data_in.get(ROE_RETURN_ON_EQUITY)
            db_value = float(raw_data[column_names.index(ROE_RETURN_ON_EQUITY)])
            company_data_item = CompanyDataItem(
                field=ROE_RETURN_ON_EQUITY,
                reported_value=reported_value,
                db_value=db_value,
                match=reported_value == db_value,
            )
            company_data.append(company_data_item)
        if ROA_RETURN_ON_ASSETS in column_names:
            reported_value = company_data_in.get(ROA_RETURN_ON_ASSETS)
            db_value = float(raw_data[column_names.index(ROA_RETURN_ON_ASSETS)])
            company_data_item = CompanyDataItem(
                field=ROA_RETURN_ON_ASSETS,
                reported_value=reported_value,
                db_value=db_value,
                match=reported_value == db_value,
            )
            company_data.append(company_data_item)
        if DEBT_TO_EQUITY_RATIO in column_names:
            reported_value = company_data_in.get(DEBT_TO_EQUITY_RATIO)
            db_value = float(raw_data[column_names.index(DEBT_TO_EQUITY_RATIO)])
            company_data_item = CompanyDataItem(
                field=DEBT_TO_EQUITY_RATIO,
                reported_value=reported_value,
                db_value=db_value,
                match=reported_value == db_value,
            )
            company_data.append(company_data_item)
        if LOCATION in column_names:
            reported_value = company_data_in.get(LOCATION)
            db_value = raw_data[column_names.index(LOCATION)]
            company_data_item = CompanyDataItem(
                field=LOCATION,
                reported_value=reported_value,
                db_value=db_value,
                match=reported_value == db_value,
            )
            company_data.append(company_data_item)
        if CEO in column_names:
            reported_value = company_data_in.get(CEO)
            db_value = raw_data[column_names.index(CEO)]
            company_data_item = CompanyDataItem(
                field=CEO,
                reported_value=reported_value,
                db_value=db_value,
                match=reported_value == db_value,
            )
            company_data.append(company_data_item)
        if NUMBER_OF_EMPLOYEES in column_names:
            reported_value = company_data_in.get(NUMBER_OF_EMPLOYEES)
            db_value = int(raw_data[column_names.index(NUMBER_OF_EMPLOYEES)])
            company_data_item = CompanyDataItem(
                field=NUMBER_OF_EMPLOYEES,
                reported_value=reported_value,
                db_value=db_value,
                match=reported_value == db_value,
            )
            company_data.append(company_data_item)

        return company_data


company_data_check_service = CompanyDataCheckService()
