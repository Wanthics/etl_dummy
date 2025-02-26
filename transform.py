import pandas as pd
from extract import extract_data

def transform_data(data):
    """Transformasi data API menjadi format DataFrame."""
    df = pd.DataFrame(data)

    # Hanya ambil kolom yang dibutuhkan
    df = df[['id', 'userId', 'title', 'body']]

    # Rename kolom agar lebih mudah dibaca
    df.columns = ['post_id', 'user_id', 'post_title', 'post_body']

    print("Data berhasil ditransformasikan!")
    print(df.head())  # Menampilkan 5 data pertama
    return df

if __name__ == "__main__":
    raw_data = extract_data()
    if raw_data:
        transform_data(raw_data)
