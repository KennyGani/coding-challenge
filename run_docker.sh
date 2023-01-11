cd backend

docker build -t backend-challenge-image .   
docker run -d --name backend_challenge -p 80:80 backend-challenge-image

cd ./../frontend

docker build -t frontend-challenge-image .
docker run -d --name frontend_challenge -p 3000:3000 frontend-challenge-image
