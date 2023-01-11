from typing import Union
from pydantic import BaseModel, validator
from fastapi import HTTPException, status
from .enums.index import FundingRoundEnumOutput


class DealOutput(BaseModel):
    company_id: int
    date: str
    funding_round: FundingRoundEnumOutput
    funding_amount: str

    @validator("company_id")
    def company_id_must_not_empty(cls, value):
        if value == "":
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Company Id must not be empty",
            )
        return value

    @validator("date")
    def date_must_not_empty(cls, value):
        if value == "":
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Date must not be empty",
            )
        return value

    @validator("funding_round")
    def funding_round_must_not_empty(cls, value):
        if value == "":
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="funding round must not be empty",
            )
        return value

    @validator("funding_amount")
    def funding_amount_must_not_empty(cls, value):
        if value == "":
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="funding amount must not be empty",
            )
        return value
