#!/bin/bash

cd client
npm run build

cd ../server
source .venv/bin/activate
python app.py