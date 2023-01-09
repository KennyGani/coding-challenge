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

    date = ""
    founding_amount = ""

    for deal in deals:
        if deals.date == None:
            date = "date not specified"

        if deals.founding_amount == None:
            founding_amount = "founding amount not specified"
        dealOutputs.append(
            DealOutput(
                company_id=deal.company_id,
                date=date,
                founding_amount=founding_amount,
                founding_round=deal.founding_round,
            )
        )

    return dealOutputs
