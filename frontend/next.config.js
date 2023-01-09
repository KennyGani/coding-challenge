module.exports = {
    source: '/_next/:path*',
    headers: [
        {
            key: 'Access-Control-Allow-Origin',
            value: 'http://localhost:80',
        },
    ],
    experimental: {
        outputStandalone: true,
    },
};
