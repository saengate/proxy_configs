FROM nginx:1.23.2

RUN apt-get update -q
RUN apt-get install -y nano curl supervisor libpq-dev apt-utils gettext apt-utils git

COPY nginx.conf /etc/nginx/sites-available/proxy_api.conf
COPY supervisord.conf /etc/supervisor/supervisord.conf

RUN chmod 0655 /etc/nginx/sites-available/proxy_api.conf
RUN chmod 0644 /etc/supervisor/supervisord.conf

RUN bash -c "ln -sf /etc/nginx/sites-available/proxy_api.conf /etc/nginx/conf.d/proxy_api.conf"

RUN rm -rf /etc/nginx/conf.d/default.conf

COPY runsupervisor /usr/local/bin/runsupervisor
RUN chmod 755 /usr/local/bin/runsupervisor

EXPOSE 80

CMD ["bash",                        \
    "-c",                           \
    "service supervisor start &&    \
    supervisorctl reread &&         \
    supervisorctl update &&         \
    supervisorctl start all &&      \
    service nginx start &&          \
    /bin/bash"                      \
    ]
