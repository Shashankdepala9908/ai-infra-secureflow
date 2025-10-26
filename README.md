# SecureFlow Inference System

This project demonstrates a secure and observable AI inference stack with:

- **gateway-layer**: reverse proxy for TLS and request routing
- **model-service**: FastAPI app with /health, /ready, /infer endpoints
- **data-store**: Postgres database for minimal audit
- **prometheus** and **grafana**: monitoring and visualization

## Usage

```bash
cp .env.template .env
docker compose build
docker compose up -d
```

- Health check: `curl -sk https://localhost:9444/health`
- Readiness check: `curl -sk https://localhost:9444/ready`
- Inference: `curl -sk -X POST https://localhost:9444/infer`

## Stop

```bash
docker compose down
docker compose down -v
```
