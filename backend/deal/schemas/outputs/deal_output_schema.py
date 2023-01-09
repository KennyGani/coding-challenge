from typing import Union
from pydantic import BaseModel, validator
from fastapi import HTTPException, status
from .enums.index import FoundingRoundEnumOutput


class DealOutput(BaseModel):
    company_id: int
    date: str
    founding_round: FoundingRoundEnumOutput
    founding_amount: str

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

    @validator("founding_round")
    def founding_round_must_not_empty(cls, value):
        if value == "":
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="founding round must not be empty",
            )
        return value

    @validator("founding_amount")
    def founding_amount_must_not_empty(cls, value):
        if value == "":
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="founding amount must not be empty",
            )
        return value
