import psycopg2
import pandas as pd
from transform import transform_data, extract_data

# Koneksi ke PostgreSQL
def connect_db():
    try:
        conn = psycopg2.connect(
            dbname="etl_db",
            user="postgres",
            password="newpassword",  # Ganti dengan password PostgreSQL
            host="localhost",
            port="5432"
        )
        return conn
    except Exception as e:
        print("Koneksi ke database gagal:", e)
        return None

# Buat tabel jika belum ada
def create_table(conn):
    with conn.cursor() as cur:
        cur.execute("""
            CREATE TABLE IF NOT EXISTS posts (
                post_id SERIAL PRIMARY KEY,
                user_id INTEGER,
                post_title TEXT,
                post_body TEXT
            )
        """)
        conn.commit()
        print("Tabel 'posts' siap digunakan!")

# Load data ke tabel
def load_data_to_db(conn, df):
    with conn.cursor() as cur:
        for _, row in df.iterrows():
            cur.execute("""
                INSERT INTO posts (post_id, user_id, post_title, post_body)
                VALUES (%s, %s, %s, %s)
                ON CONFLICT (post_id) DO NOTHING
            """, (row['post_id'], row['user_id'], row['post_title'], row['post_body']))
        conn.commit()
        print("Data berhasil dimasukkan ke database!")

if __name__ == "__main__":
    conn = connect_db()
    if conn:
        create_table(conn)
        raw_data = extract_data()
        if raw_data:
            transformed_data = transform_data(raw_data)
            load_data_to_db(conn, transformed_data)
        conn.close()
