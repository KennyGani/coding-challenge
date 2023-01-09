from sqlalchemy.orm import Session

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
            return await companyRepository.getAllCompanies(db)
        except Exception as error:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"failed to get all companies. {error}",
            )
