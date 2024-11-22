#!/bin/bash

GLOBAL_ENV_CONTENT="
#ngninx config

API_PORT=80
FASTAPI_SERVER_ADDR=fastapi:8000
STREAMLIT_FRONTEND_ADDR=streamlit:8501
# =======================================================================================================================================================================================

# BACKEND_URL_DEV=http://localhost:8000
# BACKEND_URL_DEV=http://host.docker.internal:8000/api`
SECRETS_FILE_PATH=/fastapi/secrets/passwords.json

# =======================================================================================================================================================================================
# Postgres setup

POSTGRES_HOST=db-postgres
POSTGRES_PORT=5432
POSTGRES_USER=postgres
PGDATA=/var/lib/postgresql/data/pgdata
POSTGRES_PASSWORD=asdlksjdguihedyuigduifjkdfhufdrjkhffyhjsgdfyhujheujkygh2h34yh123
DROP_TABLE_FLAG=False
# =======================================================================================================================================================================================

# FRONTEND CONFIG
COOKIE_PASSWORD=fdjldsdsfusadhfuadshfaiudsgfqeuyrrbaekjlgblguwbgflewkbg
COOKIE_PREFIX=SMC_DWT_TEST_COOKIE
# =======================================================================================================================================================================================
CHITA_PASS_HASH=eab7bcdcf99cc5c8fd74661a8bd1330814a9067c2194707a4c46a76902fd5592
ADMIN_PASS_HASH=fc618395b55f38756c9a98ec058c267830f84d448ca4e0b893951784b163b617
SPB_PASS_HASH=3a30dadb6d0bd388fa4cf7cb00d3398e9dac50538c53a062bc59b331b48882b8
"


echo "$GLOBAL_ENV_CONTENT" > ./.env

echo ".env successefully created."