FROM nginx:1.27-alpine
RUN apk add --no-cache openssl dos2unix
COPY nginx.conf /etc/nginx/nginx.conf
COPY entrypoint.sh /entrypoint.sh
RUN dos2unix /entrypoint.sh && chmod +x /entrypoint.sh
EXPOSE 443
ENTRYPOINT ["/entrypoint.sh"]