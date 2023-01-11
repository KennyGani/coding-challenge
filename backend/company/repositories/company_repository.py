from sqlalchemy.orm import Session

from ..schemas.index import *
from ..models.index import *


class CompanyRepository:

    # this variable must only be created once
    def __init__(self) -> None:
        print("Company repository is created")

    async def getAllCompanies(
        self,
        db: Session,
    ) -> list[Company]:
        return db.query(Company).all()

    async def getCompanyForId(
        self,
        db: Session,
        id: int,
    ) -> list[Company]:
        return db.query(Company).filter(Company.company_id == id).first()
