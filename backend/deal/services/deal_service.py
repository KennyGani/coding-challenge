from sqlalchemy.orm import Session

from ..schemas.index import *
from ..repositories.index import *
from ..models.index import *
from fastapi import HTTPException, status

dealRepository = deal_repository.DealRepository()


class CompanyService:

    # this variable must only be created once
    def __init__(self) -> None:
        print("Deal service is created")

    async def getAllDealsForId(self, db: Session, id: int) -> list[Deal]:
        try:
            return await dealRepository.getAllDealsForId(db, id)
        except Exception as error:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"failed to get all deals. {error}",
            )
