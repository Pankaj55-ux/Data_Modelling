import os

import psycopg2


def connect(dbname):
    """Connect to PostgreSQL using environment-based credentials."""
    return psycopg2.connect(
        host=os.getenv("PGHOST", "127.0.0.1"),
        port=os.getenv("PGPORT", "5432"),
        dbname=dbname,
        user=os.getenv("PGUSER", "postgres"),
        password=os.getenv("PGPASSWORD"),
    )