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

    return companies


@companyRoute.get("/company/{id}", response_model=CompanyOutput)
async def getCompanyForId(id: int) -> CompanyOutput:
    company = await companyService.getCompanyForId(session, id)

    return company
