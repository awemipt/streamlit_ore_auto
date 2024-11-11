#!/bin/bash

GLOBAL_ENV_CONTENT="
# =======================================================================================================================================================================================

BACKEND_URL_DEV=http://localhost:8000
# BACKEND_URL_DEV=http://host.docker.internal:8000
SECRETS_FILE_PATH=/fastapi/secrets/passwords.json
STREAMLIT_FRONTED_ADDR=streamlit:8501
FASTAPI_BACKEND_ADDR

# =======================================================================================================================================================================================
# Postgres setup

POSTGRES_HOST=db-postgres
POSTGRES_PORT=5432
POSTGRES_USER=postgres
PGDATA=/var/lib/postgresql/data/pgdata
POSTGRES_PASSWORD_FILE=/run/secrets/db-password
DROP_TABLE_FLAG=True
# =======================================================================================================================================================================================
"


echo "$GLOBAL_ENV_CONTENT" > ./.env

echo ".env successefully created."