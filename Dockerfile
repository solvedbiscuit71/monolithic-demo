FROM python:3.10.14-alpine

EXPOSE 8080

RUN mkdir -p /home/app

WORKDIR /home/app

COPY ./server .

RUN python3 -m venv .venv && source .venv/bin/activate

RUN pip install -r requirements.txt

CMD ["python", "app.py"]
