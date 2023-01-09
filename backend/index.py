from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import company.routes.company_route

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(company.routes.backend_route.companyRoute)
