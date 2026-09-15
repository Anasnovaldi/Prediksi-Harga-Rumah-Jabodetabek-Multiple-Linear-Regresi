# Prediksi-Harga-Rumah-Jabodetabek-Multiple-Linear-Regresi

## Cara Kerja
 
Program membaca data harga rumah, melatih model regresi, lalu meminta input dari pengguna (luas tanah, luas bangunan, jumlah kamar tidur/mandi, kota) untuk memprediksi estimasi harga rumah.
 
## Sumber Data
 
Dataset yang digunakan adalah **"Daftar Harga Rumah Jabodetabek"** dari Kaggle.
 
- Dibuat oleh: **Nafis Barizki**
- Lisensi: Unknown (tidak ditentukan oleh pembuat dataset)
- Dataset asli memiliki 27 kolom
## Modifikasi Data yang Dilakukan
 
Saya melakukan pembersihan dan penyederhanaan pada data asli, meliputi:
 
- Mengambil 6 kolom saja yang relevan: `land_size_m2`, `building_size_m2`, `bedrooms`, `bathrooms`, `city`, `price_in_rp`
- Membuang baris yang memiliki data kosong (missing value) pada kolom-kolom tersebut
- Menyimpan hasilnya sebagai file baru: `data_rumah_jabodetabek_bersih.csv`
Data mentah dan hasil analisis/model sepenuhnya merupakan hasil kerja saya sendiri; hanya data mentah asal yang berasal dari sumber Kaggle di atas.
 
## Cara Menjalankan
 
```bash
pip install pandas scikit-learn
python prediksi_harga_rumah.py
```
 