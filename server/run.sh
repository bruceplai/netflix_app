#!/bin/bash

PORT=9090
# Set application root dir so it can be run from any location
APPDIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
UV_ARGS="--app-dir=$APPDIR"

if [[ $* == -d ]]; then
    # Dev mode should auto-reload the application when code changes
    UV_ARGS="$UV_ARGS --reload"
    # Pass dev.env to application
    UV_ARGS="$UV_ARGS --env-file=$APPDIR/dev.env"
    echo "Starting app server in development mode..."
else
    echo "Starting app server in normal mode..."
fi

uvicorn app:app --host localhost --port $PORT $UV_ARGS