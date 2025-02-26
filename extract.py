import requests

def extract_data():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        print(f"Berhasil mengambil {len(data)} data dari API!")
        return data
    else:
        print("Gagal mengambil data dari API:", response.status_code)
        return None

if __name__ == "__main__":
    extract_data()
