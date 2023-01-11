from sqlalchemy import Column, Enum
from sqlalchemy.sql.sqltypes import Integer, String, Float
from .enums.index import *
from config.db import Base


class Deal(Base):
    __tablename__ = "deals"
    deal_id = Column(Integer, primary_key=True)
    company_id = Column(Integer)
    date = Column(String(255))
    funding_round = Column(
        Enum(
            FundingRoundEnum.SeriesA.value,
            FundingRoundEnum.SeriesB.value,
            FundingRoundEnum.SeriesC.value,
            FundingRoundEnum.Seed.value,
        )
    )
    funding_amount = Column(Float)
