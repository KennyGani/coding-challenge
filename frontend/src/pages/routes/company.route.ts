export class Company {
    async getAllCompanies() {
        const companies = await fetch('http://localhost:8000/company', {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
            },
        });

        return companies;
    }
}
