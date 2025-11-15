#!/bin/bash
set -euo pipefail

# Simple entrypoint for hosting providers like Railway/Railpack.
# Installs backend deps (if needed) and launches the Flask API.
PROJECT_ROOT="$(cd "$(dirname "$0")" && pwd)"
BACKEND_DIR="$PROJECT_ROOT/backend"
cd "$BACKEND_DIR"

PYTHON_BIN="${PYTHON_BIN:-python3}"

if ! command -v "$PYTHON_BIN" >/dev/null 2>&1; then
  if command -v python >/dev/null 2>&1; then
    PYTHON_BIN="python"
  elif command -v apt-get >/dev/null 2>&1; then
    echo "📦 Installing python3..."
    apt-get update >/dev/null
    apt-get install -y python3 python3-pip python3-venv >/dev/null
    PYTHON_BIN="python3"
  else
    echo "❌ Neither python3 nor python is available on PATH."
    exit 1
  fi
fi

VENV_PATH="$BACKEND_DIR/.venv"

if [ ! -d "$VENV_PATH" ]; then
  echo "⚙️  Creating virtual environment at $VENV_PATH"
  "$PYTHON_BIN" -m venv "$VENV_PATH"
fi

source "$VENV_PATH/bin/activate"

if [ -f requirements.txt ]; then
  pip install --no-cache-dir -r requirements.txt
fi

exec python app.py
