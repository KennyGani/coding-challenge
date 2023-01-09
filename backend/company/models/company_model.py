from sqlalchemy import Column
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import Base


class Company(Base):
    __tablename__ = "companies"
    company_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255))
    country = Column(String(255))
    founding_date = Column(String(255))
    description = Column(String(255))
