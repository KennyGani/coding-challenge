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
            deals = await dealRepository.getAllDealsForId(db, id)
            dealOutputs: list[DealOutput] = []

            for deal in deals:

                if deal.funding_amount == "":
                    fundingAmountOutput = "funding amount not specified"
                else:
                    fundingAmountOutput = deal.funding_amount

                dealOutputs.append(
                    DealOutput(
                        date=deal.date,
                        funding_amount=fundingAmountOutput,
                        funding_round=deal.funding_round,
                        company_id=deal.company_id,
                    )
                )

            return dealOutputs

        except Exception as error:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"failed to get all deals. {error}",
            )
