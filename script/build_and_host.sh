cd client
npm run build

cd ../server
source .venv/bin/activate
flask run --port 8080
