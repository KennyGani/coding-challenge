cd backend

export CODING_CHALLENGE_PATH="prod"
export CODING_CHALLENGE_HOST="localhost"

uvicorn index:app --reload