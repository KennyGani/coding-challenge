export class Deal {
    async getAllDealsForId(id: string) {
        const deals = await fetch('http://localhost:8000/deal/' + id, {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
            },
        });

        return deals;
    }
}
