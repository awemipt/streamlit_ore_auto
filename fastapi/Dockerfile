FROM tiangolo/uvicorn-gunicorn:python3.9
RUN \
  apt-get update \
  && apt-get -y install gettext-base \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*
RUN mkdir /fastapi
COPY requirements.txt /fastapi

WORKDIR /fastapi

RUN pip install --upgrade pip

RUN pip install -r requirements.txt -f https://download.pytorch.org/whl/torch_stable.html

COPY . /fastapi

ARG ADMIN_PASS_HASH
ARG CHITA_PASS_HASH
ARG SPB_PASS_HASH
ENV ADMIN_PASS_HASH=$ADMIN_PASS_HASH
ENV CHITA_PASS_HASH=$CHITA_PASS_HASH
ENV SPB_PASS_HASH=$SPB_PASS_HASH

RUN envsubst '$ADMIN_PASS_HASH,$CHITA_PASS_HASH,$SPB_PASS_HASH' < /fastapi/secrets/passwords.json.template > /fastapi/secrets/passwords.json
EXPOSE 8000

CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8000" ]