import os
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

if __name__ == "__main__":
    while True:
        os.system('cls')

        print("="*100)
        print(f"{"Prediksi Harga Rumah Jabodetabek":^100}")
        print("="*100)

        # Load Data
        df = pd.read_csv("data_rumah_jabodetabek_bersih.csv")

        # One-Hot Encoding kolom city -> otomatis, tidak perlu manual satu-satu
        df_encoded = pd.get_dummies(df, columns=["city"], drop_first=True)

        # Tentukan Fitur Dan Target
        fitur_kolom = [kol for kol in df_encoded.columns if kol != "price_in_rp"]
        X = df_encoded[fitur_kolom]
        y = df_encoded["price_in_rp"]

        # Train Test 
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )

        # Buat Model Multiple Linear regresi
        model = LinearRegression()
        model.fit(X_train,y_train)

        # Uji Akurasi Model
        print("="*100)
        y_pred = model.predict(X_test)
        for fitur, koef in zip(X.columns, model.coef_):
            print(f"  {fitur:25s}: {koef:,.2f}")
        print("="*100)
        print(f"R² Score : {r2_score(y_test, y_pred):.3f}")
        print(f"MSE      : {mean_squared_error(y_test, y_pred):,.2f}")
        print("="*100)

        try:
            # Data Uji - input dari user
            land_size     = float(input("Masukkan Luas Tanah (m2)     : "))
            building_size = float(input("Masukkan Luas Bangunan (m2)  : "))
            bedrooms      =   int(input("Masukkan Jumlah Kamar Tidur  : "))
            bathrooms     =   int(input("Masukkan Jumlah Kamar Mandi  : "))
            kota_input    = input(f"Masukkan Kota {df['city'].unique().tolist()} : ")

            # Bikin baris data baru dengan format kolom SAMA PERSIS seperti X_train
            data_baru = pd.DataFrame([[0]*len(X.columns)], columns=X.columns)
            data_baru["land_size_m2"] = land_size
            data_baru["building_size_m2"] = building_size
            data_baru["bedrooms"] = bedrooms
            data_baru["bathrooms"] = bathrooms

            kolom_kota = f"city_{kota_input}"
            if kolom_kota in data_baru.columns:
                data_baru[kolom_kota] = True

            hasil_prediksi = model.predict(data_baru)

            print("="*100)
            print(f"Prediksi Harga Rumah : Rp {hasil_prediksi[0]:,.2f}")
            print("="*100)

            option_close = input("Apakah Kamu Ingin Mengulangi Lagi (ya/tidak) : ").lower()
            if option_close == "tidak" or option_close == "no":
                break

        except ValueError:
            print("Nilai Yang Kamu Masukkan Salah")