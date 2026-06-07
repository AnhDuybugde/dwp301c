FROM nginx:1.25-alpine

LABEL maintainer="AnhDuybugde"
LABEL application="guestbook"

COPY index.html /usr/share/nginx/html/index.html

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
