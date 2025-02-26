# ETL Pipeline: JSONPlaceholder API to PostgreSQL

## Deskripsi Project
Project ini bertujuan untuk mengambil data post dari JSONPlaceholder API, melakukan transformasi sederhana, lalu menyimpannya ke database PostgreSQL.

### Tahapan ETL:
1. Extract: Mengambil data post dari [JSONPlaceholder API](https://jsonplaceholder.typicode.com/posts).
2. Transform: Mengubah nama kolom agar lebih deskriptif.
3. Load: Memasukkan data ke PostgreSQL untuk dianalisis lebih lanjut.

## Tech Stack
- Python (requests, pandas, psycopg2)
- PostgreSQL
- Docker (opsional)

## Arsitektur ETL
```plaintext
[JSONPlaceholder API] ---> [extract.py] ---> [transform.py] ---> [load.py] ---> [PostgreSQL]
```

## Cara Menjalankan Project

### 1. Persiapan
- Pastikan Python 3 dan PostgreSQL sudah terinstal.
- Clone repositori ini:
  ```bash
  git clone https://github.com/Wanthics/etl_dummy.git
  cd repo-name
  ```
- Buat virtual environment:
  ```bash
  python -m venv venv
  source venv/bin/activate  # Mac/Linux
  venv\Scripts\activate  # Windows
  ```
- Install dependency:
  ```bash
  pip install -r requirements.txt
  ```

### 2. Setup Database
- Buat database di PostgreSQL:
  ```sql
  CREATE DATABASE etl_project;
  ```
- Jalankan skrip SQL untuk membuat tabel:
  ```sql
  CREATE TABLE posts (
      post_id INT PRIMARY KEY,
      user_id INT,
      post_title TEXT,
      post_body TEXT
  );
  ```

### 3. Jalankan ETL Pipeline
- Extract data dari API:
  ```bash
  python extract.py
  ```
- Transform data:
  ```bash
  python transform.py
  ```
- Load data ke PostgreSQL:
  ```bash
  python load.py
  ```
