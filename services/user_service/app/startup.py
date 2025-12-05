#!/usr/bin/env python3
"""Startup script that runs migrations and starts the server."""
import os
import subprocess
import sys
from pathlib import Path

# Change to app directory
app_dir = Path(__file__).parent
os.chdir(app_dir)

def run_migrations():
    """Run Alembic migrations."""
    print("Running database migrations...")
    try:
        result = subprocess.run(
            ["alembic", "upgrade", "head"],
            check=True,
            capture_output=True,
            text=True
        )
        print("Migrations completed successfully")
        print(result.stdout)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Migration failed: {e.stderr}", file=sys.stderr)
        return False

def start_server():
    """Start the Uvicorn server."""
    print("Starting server...")
    subprocess.run([
        "uvicorn",
        "app.main:app",
        "--host", "0.0.0.0",
        "--port", "8000"
    ])

if __name__ == "__main__":
    if not run_migrations():
        sys.exit(1)
    start_server()

