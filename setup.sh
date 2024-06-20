#!/bin/bash

cd client
npm i
npm run build

cd ../server
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
deactivate