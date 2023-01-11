import React, { useEffect, useState } from 'react';

import { Company } from '../../routes/company.route';
import { Deal } from '../../routes/deal.route';
import styles from './../../styles/Home.module.css';

export default function Home() {
    const [companiesList, setDealsList] = useState([]);
    const [companyName, setCompanyName] = useState('');

    async function getAllDealsForId() {
        const searchParams = new URLSearchParams(document.location.search);

        const id = searchParams.get('id');

        if (id == null) {
            throw 0;
        }

        const deals = await new Deal().getAllDealsForId(id);
        const dealsOutput = await deals.json();

        const company = await new Company().getCompanyForId(id);
        const companyOutput = await company.json();

        setDealsList(dealsOutput);
        setCompanyName(companyOutput.name);
    }

    useEffect(() => {
        getAllDealsForId();
    }, []);

    return (
        <>
            <ul className={styles.main}>
                <h1>Deals with {companyName}:</h1>
                {companiesList.map((deal: any) => (
                    <div key={deal.company_id}>
                        <br></br>
                        <span>Deal date : {`${deal.date}`}</span>
                        <br></br>
                        <span>
                            funding amount : ${`${deal.funding_amount}`}
                        </span>
                        <br></br>
                        <span>funding round : {`${deal.funding_round}`}</span>
                        <br></br>
                    </div>
                ))}
            </ul>
        </>
    );
}
