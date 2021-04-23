FROM nginx:mainline-alpine
COPY ./nginx/uwsgi_params /etc/nginx/uwsgi_params
COPY ./nginx/conf /etc/nginx/conf.d