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

    async getCompanyForId(id: string) {
        const company = await fetch('http://localhost:80/company/' + id, {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
            },
        });

        return company;
    }
}
