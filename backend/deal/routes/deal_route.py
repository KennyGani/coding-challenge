from fastapi import APIRouter
from ..schemas.outputs.enums.index import *
from ..models.index import *
from ..schemas.index import *
from ..services.index import *
import config.db

dealRoute = APIRouter()
dealService = deal_service.CompanyService()
session = config.db.SessionFactory()


@dealRoute.get("/deal/{id}", response_model=list[DealOutput])
async def getAllDealsForId(id: int) -> list[DealOutput]:
    deals = await dealService.getAllDealsForId(session, id)

    dealOutputs: list[DealOutput] = []

    for deal in deals:
        dealOutputs.append(
            DealOutput(
                company_id=deal.company_id,
                date=deal.date,
                funding_amount=deal.funding_amount,
                funding_round=deal.funding_round,
            )
        )

    return dealOutputs
