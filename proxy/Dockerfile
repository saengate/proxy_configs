FROM nginx:1.23.2

RUN apt-get update -q
RUN apt-get install -y nano curl libpq-dev apt-utils gettext apt-utils git

COPY nginx.conf /etc/nginx/sites-available/proxy_api.conf

RUN chmod 0655 /etc/nginx/sites-available/proxy_api.conf

RUN bash -c "ln -sf /etc/nginx/sites-available/proxy_api.conf /etc/nginx/conf.d/proxy_api.conf"

RUN rm -rf /etc/nginx/conf.d/default.conf

EXPOSE 80

CMD ["bash",                        \
    "-c",                           \
    "service nginx start &&          \
    /bin/bash"                      \
    ]
