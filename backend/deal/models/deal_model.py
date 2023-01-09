from sqlalchemy import Column, Enum
from sqlalchemy.sql.sqltypes import Integer, String
from .enums.index import *
from config.db import Base


class Deal(Base):
    __tablename__ = "deals"
    company_id = Column(Integer)
    date = Column(String(255))
    founding_round = Column(
        Enum(
            FoundingRoundEnum.SeriesA.value,
            FoundingRoundEnum.SeriesB.value,
            FoundingRoundEnum.SeriesC.value,
            FoundingRoundEnum.Seed.value,
        )
    )
    founding_amount = Column(float(255))
