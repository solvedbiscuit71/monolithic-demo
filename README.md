# Monolithic Template

## Frontend (mandatory to run)

- Node Version (v20.11.1)
- NPM Version (10.2.4)

## Backend

- Python Version (3.10.12 or higher)
- Pip Version (24.0)

# Deploy locally

1. Install the correct version of node and python as mentioned above
2. Run the setup script

```bash
./script/setup.sh
```

3. Run the host script to publish at [http://127.0.0.1:8080/](http://127.0.0.1:8080/)

```bash
./script/build_and_host.sh
```

# Deploy in Docker

1. Use docker compose to build and run the container

```bash
docker compose up -d
```

2. The flask app is publish at [http://127.0.0.1:8080/](http://127.0.0.1:8080/)