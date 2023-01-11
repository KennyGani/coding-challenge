from fastapi.testclient import TestClient
import pytest
import index
import deal.models.deal_model as model
import deal.routes.deal_route as route
import deal.schemas.outputs.deal_output_schema as schema

import config.db

config.db.Base.metadata.create_all(bind=config.db.engine)

client = TestClient(index.app)


@pytest.mark.asyncio
async def test_get_all_deals_when_empty():
    route.session.execute("drop table deals")
    config.db.Base.metadata.create_all(bind=config.db.engine)

    response = client.get("/deal")
    assert response.status_code == 404
    assert response.json() == {"detail": "Not Found"}


@pytest.mark.asyncio
async def test_get_all_deals_when_not_empty():
    route.session.execute("drop table deals")
    config.db.Base.metadata.create_all(bind=config.db.engine)

    fakeDeal = model.Deal(
        company_id=1,
        date="1566147853000",
        funding_round=schema.FundingRoundEnumOutput.Seed,
        funding_amount="1670131.0",
    )

    fakeDeal2 = model.Deal(
        company_id=1,
        date="54321345",
        funding_round=schema.FundingRoundEnumOutput.SeriesA,
        funding_amount="9827678.0",
    )

    route.session.add(fakeDeal)
    route.session.add(fakeDeal2)
    route.session.commit()

    response = client.get("/deal/1")
    assert response.status_code == 200
    assert response.json() == [
        {
            "company_id": fakeDeal.company_id,
            "date": fakeDeal.date,
            "funding_round": fakeDeal.funding_round,
            "funding_amount": str(fakeDeal.funding_amount),
        },
        {
            "company_id": fakeDeal2.company_id,
            "date": fakeDeal2.date,
            "funding_round": fakeDeal2.funding_round,
            "funding_amount": str(fakeDeal2.funding_amount),
        },
    ]
