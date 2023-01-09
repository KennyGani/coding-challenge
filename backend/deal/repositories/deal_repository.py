from sqlalchemy.orm import Session

from ..schemas.index import *
from ..models.index import *


class DealRepository:

    # this variable must only be created once
    def __init__(self) -> None:
        print("Deal repository is created")

    async def getAllDealsForId(self, db: Session, company_id: int) -> list[Deal]:
        return db.query(Deal).filter(Deal.company_id == company_id)
