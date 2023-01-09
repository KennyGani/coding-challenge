import Link from 'next/link';
import React, { useEffect, useState } from 'react';

import { Company } from '../routes/company.route';
import styles from '../styles/Home.module.css';

export default function Home() {
    const [companiesList, setCompaniesList] = useState([]);

    async function getAllCompanies() {
        const companies = await new Company().getAllCompanies();
        const companiesOutput = await companies.json();

        setCompaniesList(companiesOutput);
    }

    useEffect(() => {
        getAllCompanies();
    }, []);

    return (
        <>
            <ul className={styles.main}>
                <h1>Company Name:</h1>
                {companiesList.map((company: any) => (
                    <Link
                        key={company.company_id}
                        href={'/deal?id=' + company.company_id}
                        legacyBehavior
                    >
                        <li>
                            <span>{`${company.name}`}</span>
                            <br></br>
                            <span>{`${company.country}`}</span>
                            <br></br>
                            <span>{`${company.founding_date}`}</span>
                            <br></br>
                            <span>{`${company.description}`}</span>
                            <br></br>
                            <br></br>
                        </li>
                    </Link>
                ))}
            </ul>
        </>
    );
}
