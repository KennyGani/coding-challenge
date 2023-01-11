from sqlalchemy.orm import Session
from dateutil import parser

from ..schemas.index import *
from ..repositories.index import *
from ..models.index import *
from fastapi import HTTPException, status

companyRepository = company_repository.CompanyRepository()


class CompanyService:

    # this variable must only be created once
    def __init__(self) -> None:
        print("company service is created")

    async def getAllCompanies(
        self,
        db: Session,
    ) -> list[Company]:
        try:
            companies = await companyRepository.getAllCompanies(db)

            companyOutputs: list[CompanyOutput] = []

            for company in companies:

                if company.country == "":
                    countryOutput = "country not specified"
                else:
                    countryOutput = company.country

                if company.founding_date == "":
                    founding_dateOutput = "founding date not specified"
                else:
                    founding_dateOutput = company.founding_date

                if company.description == "":
                    descriptionOutput = "description not specified"
                else:
                    descriptionOutput = company.description

                companyOutputs.append(
                    CompanyOutput(
                        company_id=company.company_id,
                        name=company.name,
                        country=countryOutput,
                        founding_date=founding_dateOutput,
                        description=descriptionOutput,
                    )
                )

            return companyOutputs

        except Exception as error:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"failed to get all companies. {error}",
            )

    async def getCompanyForId(self, db: Session, id: int) -> Company:
        try:
            company = await companyRepository.getCompanyForId(db, id)

            if company.country == "":
                countryOutput = "country not specified"
            else:
                countryOutput = company.country
            if company.founding_date == "":
                founding_dateOutput = "founding date not specified"
            else:
                founding_dateOutput = company.founding_date
            if company.description == "":
                descriptionOutput = "description not specified"
            else:
                descriptionOutput = company.description

            return CompanyOutput(
                company_id=company.company_id,
                name=company.name,
                country=countryOutput,
                founding_date=founding_dateOutput,
                description=descriptionOutput,
            )

        except Exception as error:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"failed to get company with id {id}. {error}",
            )
