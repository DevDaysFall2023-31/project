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

**If you want to run service via docker you should change localhost ip address in .env file to host ip.** You can do it using setup_ip.sh script:
```
./setup_ip.sh .env
```

2. Build images and start
```
supabase start
supabase db reset

docker compose build
docker compose up -d
```
