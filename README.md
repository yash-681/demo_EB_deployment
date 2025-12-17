# Basic Python (Flask) App for Elastic Beanstalk / Docker

This repo builds a Docker image that runs a tiny Python web app on port **8000**.

## Endpoints
- `GET /` → Hello World
- `GET /health` → `{"status":"ok"}`

## Run locally (Docker)

```bash
docker build -t demo-python-app .
docker run --rm -p 8000:8000 demo-python-app
```

Then open `http://localhost:8000`.


