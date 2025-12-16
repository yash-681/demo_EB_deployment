FROM public.ecr.aws/nginx/nginx:alpine


COPY . /usr/share/nginx/html

EXPOSE 8000
