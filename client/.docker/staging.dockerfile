FROM node:14.15.4 as node

WORKDIR /app

COPY . .

RUN npm i -g @angular/cli@latest
RUN npm i
RUN ng build --configuration=staging

FROM nginx:alpine

COPY --from=node /app/dist/netflix /usr/share/nginx/html
COPY --from=node /app/.docker/nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80
