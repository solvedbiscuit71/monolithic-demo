FROM node:20-alpine as client-builder

WORKDIR /home/app
COPY ./client/package*.json ./
RUN npm install
COPY ./client/ ./
RUN npm run build

FROM python:3.10-alpine

WORKDIR /home/app
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
RUN apk add --no-cache gcc musl-dev linux-headers
COPY ./server/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5000
COPY ./server/ ./
COPY --from=client-builder /home/server/static ./static

CMD [ "flask", "run" ]
