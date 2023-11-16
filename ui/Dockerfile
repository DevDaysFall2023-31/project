FROM node:16.11 AS builder
WORKDIR /usr/src
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run-script build

FROM nginx:1.23.4-alpine
COPY nginx/default.conf /etc/nginx/conf.d/default.conf
COPY --from=builder /usr/src/build /usr/share/nginx/html
