from fastapi import APIRouter
import config.db
from ..schemas.index import *
from ..models.index import *
from ..services.index import *


companyRoute = APIRouter()

companyService = company_service.CompanyService()
session = config.db.SessionFactory()


@companyRoute.get("/company", response_model=list[CompanyOutput])
async def getAllCompanies() -> list[CompanyOutput]:
    companies = await companyService.getAllCompanies(session)

    companyOutputs: list[CompanyOutput] = []

    country = ""
    founding_date = ""
    description = ""

    for company in companies:
        if company.country == None:
            country == "country not specified"

        if company.founding_date == None:
            founding_date == "founding date not specified"

        if company.description == None:
            description == "description not specified"

        companyOutputs.append(
            CompanyOutput(
                company_id=company.company_id,
                name=company.name,
                country=country,
                founding_date=founding_date,
                description=description,
            )
        )

    return companyOutputs
