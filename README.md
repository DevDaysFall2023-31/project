# project

## Start

> Prerequisites:
> - docker, docker compose
> - supabase cli (for local development)

1. Configure environment
```
cp .env.local .env
vim .env
```

2. Build images and start
```
supabase start

docker compose build
docker compose up -d
```
