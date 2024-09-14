
"""Application Models"""
from werkzeug.security import generate_password_hash, check_password_hash

import psycopg2

DB_CONN = {
    "user": "postgres",
    "password": "password",
    "host": "localhost",
    "port": 5432,
    "dbname": "postgres",
}

def create_user():
    """Create a new user"""

    query = """
        INSERT INTO users (email, fullname, password, created_at)
        VALUES (%(email)s, %(fullname)s, %(password)s, now())
        RETURNING id
    """
    data = {
        "email": "test2@test.com",
        "fullname": "Chandler Bing",
        "password": generate_password_hash("password123"),
    }

    with psycopg2.connect(**DB_CONN) as conn:
        with conn.cursor() as cur:

            cur.execute(query, data)
            last_id = cur.fetchone()[0]
    
    return last_id



def login(email, password):
    """Login a user"""
    
    with psycopg2.connect(**DB_CONN) as conn:
        with conn.cursor() as cur:

            query = "SELECT id, email, fullname, password, created_at FROM users WHERE email=%s"

            cur.execute(query, (email, ))
            res_user = cur.fetchone()

    user = {
        "id": res_user[0],
        "email": res_user[1],
        "fullname": res_user[2],
        "password": res_user[3],
        "created_at": res_user[4]
    }
    if not res_user or not check_password_hash(res_user[3], password):
        return
    return user
