import Link from 'next/link';
import React, { useEffect, useState } from 'react';

import { Company } from './routes/company.route';
import styles from './styles/Home.module.css';

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
                        href={
                            '/deal/?companyName=' +
                            company.name +
                            '&id=' +
                            company.company_id
                        }
                        legacyBehavior
                    >
                        <span>{`${company.name}`}</span>
                    </Link>
                ))}
            </ul>
        </>
    );
}
