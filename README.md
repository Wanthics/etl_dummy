# ETL Pipeline: JSONPlaceholder API to PostgreSQL

## Deskripsi Project
Project ini bertujuan untuk mengambil data post dari JSONPlaceholder API, melakukan transformasi sederhana, lalu menyimpannya ke database PostgreSQL.

### Tahapan ETL:
1. **Extract**: Mengambil data post dari [JSONPlaceholder API](https://jsonplaceholder.typicode.com/posts).
2. **Transform**: Mengubah nama kolom agar lebih deskriptif.
3. **Load**: Memasukkan data ke PostgreSQL untuk dianalisis lebih lanjut.

---

## Tech Stack
- **Python** (requests, pandas, psycopg2)
- **PostgreSQL**
- **Docker** (opsional)

---

## Arsitektur ETL
```plaintext
[JSONPlaceholder API] ---> [extract.py] ---> [transform.py] ---> [load.py] ---> [PostgreSQL]
```

---

## Cara Menjalankan Project

### 1. Persiapan
- Pastikan **Python 3** dan **PostgreSQL** sudah terinstal.
- Clone repositori ini:
  ```bash
  git clone https://github.com/username/repo-name.git
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
- **Extract data dari API**:
  ```bash
  python extract.py
  ```
- **Transform data**:
  ```bash
  python transform.py
  ```
- **Load data ke PostgreSQL**:
  ```bash
  python load.py
  ```

---

## Otomatisasi ETL Pipeline

Agar ETL pipeline berjalan secara otomatis pada interval tertentu, gunakan metode berikut:

### Linux/macOS (Cron Job)
1. Buka terminal dan edit crontab:
   ```bash
   crontab -e
   ```
2. Tambahkan baris berikut untuk menjalankan ETL setiap hari pukul 02:00 AM:
   ```bash
   0 2 * * * /usr/bin/python3 /path/to/your/project/run_etl.sh
   ```
3. Buat file `run_etl.sh` di direktori project:
   ```bash
   #!/bin/bash
   source /path/to/your/project/venv/bin/activate
   python /path/to/your/project/extract.py
   python /path/to/your/project/transform.py
   python /path/to/your/project/load.py
   ```
4. Berikan izin eksekusi:
   ```bash
   chmod +x run_etl.sh
   ```

### Windows (Task Scheduler)
1. Buka **Task Scheduler** dan buat tugas baru.
2. Pilih **Create Basic Task**, beri nama "ETL Pipeline".
3. Atur trigger ke **Daily** dan tentukan jam eksekusi.
4. Pada tab **Action**, pilih **Start a Program** dan masukkan:
   ```
   C:\Users\YourUser\AppData\Local\Programs\Python\Python39\python.exe
   ```
   dengan argument:
   ```
   C:\path\to\your\project\run_etl.bat
   ```
5. Buat file `run_etl.bat`:
   ```bat
   @echo off
   call C:\path\to\your\project\venv\Scripts\activate
   python C:\path\to\your\project\extract.py
   python C:\path\to\your\project\transform.py
   python C:\path\to\your\project\load.py
   ```
6. Simpan dan jalankan Task Scheduler.

Dengan otomatisasi ini, ETL pipeline dapat berjalan secara berkala tanpa intervensi manual.
