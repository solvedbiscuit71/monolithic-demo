# Monolithic Template

## Frontend

- Node Version (v20.11.1)
- NPM Version (10.2.4)

## Backend

- Python Version (3.10.12 or higher)
- Pip Version (24.0)

# Run local

1. Install the correct version of node and python as mentioned above
2. Run the `./script/setup.sh` script
3. Run the `./script/host.sh` script
4. Your application will be hosted at [http://127.0.0.1:8080/](http://127.0.0.1:8080/)

# Docker

1. Run the migrate script to export the client artifact

```bash
./script/migrate.sh
```

2. Build the docker image

```bash
docker build -t monolithic-template:latest .
```

3. Run the container

```bash
docker run -d -p 8080:8080 --name web-app monolithic-template:latest
```
