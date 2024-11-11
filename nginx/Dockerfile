FROM nginx:1.27.2-alpine

USER root
# Add bash for boot cmd
RUN apk update && apk upgrade --no-cache
RUN apk add --no-cache bash
COPY nginx.conf.template /etc/nginx/nginx.conf.template


ARG FASTAPI_SERVER_ADDR
ENV FASTAPI_SERVER_ADDR $FASTAPI_SERVER_ADDR

ARG STREAMLIT_FRONTEND_ADDR
ENV STREAMLIT_FRONTEND_ADDR $STREAMLIT_FRONTEND_ADDR

RUN envsubst '$FASTAPI_SERVER_ADDR,$STREAMLIT_FRONTEND_ADDR' < /etc/nginx/nginx.conf.template > /etc/nginx/nginx.conf

WORKDIR /app

# USER nginx TODO uncommenting this makes nginx giving blanc page

CMD nginx -g 'daemon off;'


EXPOSE 80