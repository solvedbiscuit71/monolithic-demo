FROM alpine:3.20

ENV DOCKER_BUILD=1

EXPOSE 8080

RUN mkdir -p /home/app

WORKDIR /home/app

COPY . .

RUN apk add --upgrade python3 nodejs npm

RUN ./setup.sh

CMD ["/bin/sh", "host.sh"]
