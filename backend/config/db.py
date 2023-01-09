from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

path = os.getenv("CODING_CHALLENGE_PATH", "dev")
host = os.getenv("CODING_CHALLENGE_HOST", "host.docker.internal")

connect_string = f"mysql+pymysql://root:password@{host}:3306/challenge_{path}"

SQLALCHEMY_DATABASE_URL = connect_string

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionFactory = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
