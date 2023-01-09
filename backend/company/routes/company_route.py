from fastapi import APIRouter
import config.db

companyRoute = APIRouter()
companyService = company_service.CompanyService()
session = config.db.SessionFactory()


@companyRoute.get("/company", response_model=list[CompanyOutput])
async def getAllCompanys() -> list[CompanyOutput]:
    companies = await companyService.getAllCompanies(session)

    companyOutputs: list[CompanyOutput] = []

    for company in companies:
        companyOutputs.append(
            CompanyOutput(
                name=company.name,
                email=company.email,
                gender=company.gender,
                classKey=company.classKey,
            )
        )

    return companyOutputs