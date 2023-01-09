from fastapi.testclient import TestClient
import pytest
import index
import company.models.company_model as model
import company.routes.company_route as route
import config.db

config.db.Base.metadata.create_all(bind=config.db.engine)

client = TestClient(index.app)


@pytest.mark.asyncio
async def test_get_all_companies_when_empty():
    route.session.execute("drop table companies")
    config.db.Base.metadata.create_all(bind=config.db.engine)

    response = client.get("/company")
    assert response.status_code == 200
    assert response.json() == []


@pytest.mark.asyncio
async def test_get_all_companies_when_not_empty():
    route.session.execute("drop table companies")
    config.db.Base.metadata.create_all(bind=config.db.engine)

    fakeCompany = model.Company(
        name="Mayer and Sons",
        country="Sweden",
        founding_date="2021-06-11T02:09:34Z",
        description="Secured scalable standardization",
    )

    route.session.add(fakeCompany)
    route.session.commit()
    route.session.refresh(fakeCompany)

    response = client.get("/company")

    assert response.status_code == 200
    assert response.json() == [
        {
            "company_id": fakeCompany.company_id,
            "name": fakeCompany.name,
            "country": fakeCompany.country,
            "founding_date": fakeCompany.founding_date,
            "description": fakeCompany.description,
        }
    ]
