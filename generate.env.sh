#!/bin/bash

GLOBAL_ENV_CONTENT="
#ngninx config

API_PORT=80
FASTAPI_SERVER_ADDR=fastapi:8000
STREAMLIT_FRONTEND_ADDR=streamlit:8501
# =======================================================================================================================================================================================

# BACKEND_URL_DEV=http://localhost:8000
BACKEND_URL_DEV=http://host.docker.internal:8000/api
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
"


echo "$GLOBAL_ENV_CONTENT" > ./.env

echo ".env successefully created."