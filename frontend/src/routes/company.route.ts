export class Company {
    async getAllCompanies() {
        const companies = await fetch('http://localhost:80/company', {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
            },
        });

        return companies;
    }
}
