#!/usr/bin/env bash
set -euo pipefail

# Usage:
#   ./start.sh            # start normally
#   ./start.sh --reset    # wipe local DB and run migrations, then start

maybe_reset() {
  if [[ "${1:-}" == "--reset" ]]; then
    echo "[start.sh] Resetting database..."
    # Derive SQLite path from env var if provided; default to sproutify.db in CWD
    DB_PATH="sproutify.db"
    if [[ -n "${SQLALCHEMY_DATABASE_URI:-}" && "${SQLALCHEMY_DATABASE_URI}" == sqlite:///* ]]; then
      DB_PATH="${SQLALCHEMY_DATABASE_URI#sqlite:///}"
    fi
    # If it's SQLite, delete file; otherwise attempt full downgrade (optional)
    if [[ -n "$DB_PATH" ]]; then
      echo "[start.sh] Removing $DB_PATH"
      rm -f "$DB_PATH"
    fi
    echo "[start.sh] Applying migrations"
    flask --app sproutify db upgrade
  fi
}

maybe_reset "${1:-}"

flask --app sproutify run -p 5001 --debug
