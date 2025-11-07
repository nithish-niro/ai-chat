#!/usr/bin/env bash
set -euo pipefail

# Simple deploy helper (local): render docker-compose and copy to remote then run docker-compose
# Usage: ./scripts/deploy.sh <ssh-user@host> <remote-dir>
# Requires DOCKERHUB_USERNAME env var to be set locally and ssh access to the remote host

if [ "$#" -lt 2 ]; then
  echo "Usage: $0 <ssh-user@host> <remote-dir>"
  exit 2
fi

REMOTE_HOST="$1"
REMOTE_DIR="$2"

BACKEND_IMAGE="${DOCKERHUB_USERNAME:-your-dockerhub}/ai-chat-backend:latest"
FRONTEND_IMAGE="${DOCKERHUB_USERNAME:-your-dockerhub}/ai-chat-frontend:latest"

echo "Rendering docker-compose.prod.yml with images:"
echo "  backend: ${BACKEND_IMAGE}"
echo "  frontend: ${FRONTEND_IMAGE}"

sed "s|REPLACE_BACKEND_IMAGE|${BACKEND_IMAGE}|g; s|REPLACE_FRONTEND_IMAGE|${FRONTEND_IMAGE}|g" docker-compose.prod.yml > rendered-docker-compose.yml

echo "Copying rendered docker-compose to ${REMOTE_HOST}:${REMOTE_DIR}"
scp rendered-docker-compose.yml "${REMOTE_HOST}:${REMOTE_DIR}/docker-compose.yml"

echo "Running docker-compose on remote host"
ssh "${REMOTE_HOST}" "mkdir -p ${REMOTE_DIR} && cd ${REMOTE_DIR} && docker-compose pull && docker-compose up -d"

echo "Deployment complete."
