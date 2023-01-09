from typing import Union
from pydantic import BaseModel, validator
from fastapi import HTTPException, status


class CompanyOutput(BaseModel):
    company_id: int
    name: str
    country: Union[str, None] = None
    founding_date: Union[str, None] = None
    description: Union[str, None] = None

    @validator("company_id")
    def company_id_must_not_empty(cls, value):
        if value == "":
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Company Id must not be empty",
            )
        return value

    @validator("name")
    def name_must_not_empty(cls, value):
        if value == "":
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="Name must not be empty"
            )
        return value
