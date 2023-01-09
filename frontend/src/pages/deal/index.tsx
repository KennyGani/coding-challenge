import React, { useEffect, useState } from 'react';

import { Deal } from './../routes/deal.route';
import styles from './../styles/Home.module.css';

export default function Home() {
    const [companiesList, setDealsList] = useState([]);
    const [companyName, setCompanyName] = useState('');

    async function getAllDealsForId() {
        const searchParams = new URLSearchParams(document.location.search);

        const id = searchParams.get('id');
        const companyName = searchParams.get('companyName');

        if (id == null || companyName == null) {
            throw 0;
        }

        const deals = await new Deal().getAllDealsForId(id);
        const dealsOutput = await deals.json();

        console.log(id);

        setDealsList(dealsOutput);
        setCompanyName(companyName);
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
                        <span>{`${deal.date}`}</span>
                        <br></br>
                        <span>{`${deal.founding_amount}`}</span>
                        <br></br>
                        <span>{`${deal.founding_round}`}</span>
                        <br></br>
                        <span>{`${deal.company_id}`}</span>
                    </div>
                ))}
            </ul>
        </>
    );
}
