import pandas as pd
from Insan import Insan
from Issiz import Issiz
from Calisan import Calisan
from MaviYaka import MaviYaka
from BeyazYaka import BeyazYaka

try:
    # İnsan sınıfı için 2 nesne üretme:
    insan1 = Insan("12345678910", "Ahmet", "Kaya", 24, "Erkek", "Türk")
    insan2 = Insan("10987654321", "Fatma", "Korkmaz", 30, "Kadın", "Türk")
    # insan nesnelerini yazdır
    print("İnsan Nesneleri:")
    print(insan1)
    print(insan2)
    # hata oluşma durumunda hatayı yazdırır
except Exception as hata:
    print("Hata: İnsan nesneleri oluşturulurken bir hata oluştu.")
    print(str(hata))
try:
    # İşsiz sınıfı için 3 nesne üretme:
    issiz1 = Issiz("11111111111", "Ali", "Yılmaz", 26, "Erkek", "Türk", {"Maviyaka": 2, "Beyazyaka": 1, "Yönetici": 3})
    issiz2 = Issiz("22222222222", "Ayşe", "Yaman", 34, "Kadın", "Türk", {"Maviyaka": 1, "Beyazyaka": 2, "Yönetici": 1})
    issiz3 = Issiz("33333333333", "Mehmet", "Demir", 36, "Erkek", "Türk", {"Maviyaka": 3, "Beyazyaka": 3, "Yönetici": 2})
    print("İşsiz Nesneleri:")
    print(issiz1)
    print(issiz2)
    print(issiz3)
except Exception as hata:
    print("Hata: İşsiz nesneleri oluşturulurken bir hata oluştu.")
    print(str(hata))

try:
    # Çalışan sınıfı için 3 nesne üretme:
    calisan1 = Calisan("44444444444", "Mustafa", "Karademir", 25, "Erkek", "Türk", "Teknoloji", 5, 8000)
    calisan2 = Calisan("55555555555", "Fatih", "Doğru", 32, "Erkek", "Türk", "Finans", 10, 12000)
    calisan3 = Calisan("66666666666", "Aylin", "Kısa", 35, "Kadın", "Türk", "Pazarlama", 3, 6000)
    print("Çalışan Nesneleri:")
    print(calisan1)
    print(calisan2)
    print(calisan3)
except Exception as hata:
    print("Hata: Çalışan nesneleri oluşturulurken bir hata oluştu.")
    print(str(hata))

try:
    # Mavi yaka sınıfı için 3 nesne üretme:
    mavi_yaka1 = MaviYaka("77777777777", "Şeref", "Bodur", 25, "Erkek", "Türk", "İnşaat", 4, 15500, 0.2)
    mavi_yaka2 = MaviYaka("88888888888", "Veli", "Gök", 31, "Erkek", "Türk", "Temizlik", 2, 23000, 0.2)
    mavi_yaka3 = MaviYaka("99999999999", "Hasan", "Güngören", 35, "Erkek", "Türk", "Ulaşım", 6, 14000, 0.2)

    print("Mavi Yaka Nesneleri:")
    print(mavi_yaka1)
    print(mavi_yaka2)
    print(mavi_yaka3)
except Exception as hata:
    print("Hata: Mavi yaka nesneleri oluşturulurken bir hata oluştu.")
    print(str(hata))

try:
    # Beyaz yaka sınıfı için 3 nesne üretilme
    beyaz_yaka1 = BeyazYaka("10101010101", "Ceyda", "Ekşi", 25, "Kadın", "Türk", "Bilgi Teknolojileri", 8, 10000, 2000)
    beyaz_yaka2 = BeyazYaka("20202020202", "Emre", "Can", 30, "Erkek", "Türk", "Finans", 5, 9000, 1500)
    beyaz_yaka3 = BeyazYaka("30303030303", "Sibel", "Doğan", 35, "Kadın", "Türk", "Pazarlama", 7, 11000, 2500)
    print("Beyaz Yaka Nesneleri:")
    print(beyaz_yaka1)
    print(beyaz_yaka2)
    print(beyaz_yaka3)
except Exception as hata:
    print("Hata: Beyaz yaka nesneleri oluşturulurken bir hata oluştu.")
    print(str(hata))

# DataFrame oluşturma
data = {
    "nesne": ["Çalışan", "Çalışan", "Çalışan", "Mavi Yaka", "Mavi Yaka", "Mavi Yaka", "Beyaz Yaka", "Beyaz Yaka", "Beyaz Yaka"],
    "tc_no": [calisan1.get_tc_no(), calisan2.get_tc_no(), calisan3.get_tc_no(), mavi_yaka1.get_tc_no(), mavi_yaka2.get_tc_no(), mavi_yaka3.get_tc_no(), beyaz_yaka1.get_tc_no(), beyaz_yaka2.get_tc_no(), beyaz_yaka3.get_tc_no()],
    "ad": [calisan1.get_ad(), calisan2.get_ad(), calisan3.get_ad(), mavi_yaka1.get_ad(), mavi_yaka2.get_ad(), mavi_yaka3.get_ad(), beyaz_yaka1.get_ad(), beyaz_yaka2.get_ad(), beyaz_yaka3.get_ad()],
    "soyad": [calisan1.get_soyad(), calisan2.get_soyad(), calisan3.get_soyad(), mavi_yaka1.get_soyad(), mavi_yaka2.get_soyad(), mavi_yaka3.get_soyad(), beyaz_yaka1.get_soyad(), beyaz_yaka2.get_soyad(), beyaz_yaka3.get_soyad()],
    "yas": [calisan1.get_yas(), calisan2.get_yas(), calisan3.get_yas(), mavi_yaka1.get_yas(), mavi_yaka2.get_yas(), mavi_yaka3.get_yas(), beyaz_yaka1.get_yas(), beyaz_yaka2.get_yas(), beyaz_yaka3.get_yas()],
    "cinsiyet": [calisan1.get_cinsiyet(), calisan2.get_cinsiyet(), calisan3.get_cinsiyet(), mavi_yaka1.get_cinsiyet(), mavi_yaka2.get_cinsiyet(), mavi_yaka3.get_cinsiyet(), beyaz_yaka1.get_cinsiyet(), beyaz_yaka2.get_cinsiyet(), beyaz_yaka3.get_cinsiyet()],
    "uyruk": [calisan1.get_uyruk(), calisan2.get_uyruk(), calisan3.get_uyruk(), mavi_yaka1.get_uyruk(), mavi_yaka2.get_uyruk(), mavi_yaka3.get_uyruk(), beyaz_yaka1.get_uyruk(), beyaz_yaka2.get_uyruk(), beyaz_yaka3.get_uyruk()],
    "sektör": [calisan1.get_sektor(), calisan2.get_sektor(), calisan3.get_sektor(), mavi_yaka1.get_sektor(), mavi_yaka2.get_sektor(), mavi_yaka3.get_sektor(), beyaz_yaka1.get_sektor(), beyaz_yaka2.get_sektor(), beyaz_yaka3.get_sektor()],
    "tecrübe": [calisan1.get_tecrube(), calisan2.get_tecrube(), calisan3.get_tecrube(), mavi_yaka1.get_tecrube(), mavi_yaka2.get_tecrube(), mavi_yaka3.get_tecrube(), beyaz_yaka1.get_tecrube(), beyaz_yaka2.get_tecrube(), beyaz_yaka3.get_tecrube()],
    "maaş": [calisan1.get_maas(), calisan2.get_maas(), calisan3.get_maas(), mavi_yaka1.get_maas(), mavi_yaka2.get_maas(), mavi_yaka3.get_maas(), beyaz_yaka1.get_maas(), beyaz_yaka2.get_maas(), beyaz_yaka3.get_maas()],
    "yıpranma_payı": [0, 0, 0, mavi_yaka1.get_yipranma_payi(), mavi_yaka2.get_yipranma_payi(), mavi_yaka3.get_yipranma_payi(),0,0,0],
    "teşvik_primi": [0, 0, 0, 0, 0, 0, beyaz_yaka1.get_tesvik_primi(), beyaz_yaka2.get_tesvik_primi(), beyaz_yaka3.get_tesvik_primi()],
    "yeni_maaş": [calisan1.get_yenimaas(), calisan2.get_yenimaas(), calisan3.get_yenimaas(), mavi_yaka1.get_yenimaas(), mavi_yaka2.get_yenimaas(), mavi_yaka3.get_yenimaas(), beyaz_yaka1.get_yenimaas(), beyaz_yaka2.get_yenimaas(), beyaz_yaka3.get_yenimaas()]
}
# Dataframe i ekrana yazdırma:
df = pd.DataFrame(data)
print(df)

# Boş değerlere 0 atama
df.fillna(0, inplace=True)

# Gruplama ve ortalama hesaplama
grouped = df.groupby("nesne")[["tecrübe", "yeni_maaş"]].mean()
print("Tecrübe ve Yeni Maaş Ortalamaları:")
print(grouped)

# Maaşı 15000 TL üzerinde olanların sayısını bulup yazdırma
maas_ustunde = df[df["maaş"] > 15000]
maas_ustunde_sayisi = len(maas_ustunde)
print("Maaşı 15000 TL üzerinde olanların sayısı:", maas_ustunde_sayisi)

# Yeni maaşa göre DataFrame i sıralama
df.sort_values("yeni_maaş", inplace=True)
print("Yeni Maaşa Göre Sıralama:")
print(df)

# Tecrübesi 3 seneden fazla olan Beyaz yakalıları bulma
beyazYaka_tecrube = df[(df["nesne"] == "Beyaz Yaka") & (df["tecrübe"] > 3)]
print("Tecrübesi 3 seneden fazla olan Beyaz yakalılar:")
print(beyazYaka_tecrube)

# Yeni maaşı 10000 TL üzerinde olanları bulma
yeni_maas_ustunde = df[df["yeni_maaş"] > 10000]
satirlar2_5 = yeni_maas_ustunde.iloc[2:5, [2, 9]]  # Sütun indekslerini ayrı ayrı belirtme
print("Yeni Maaşı 10000 TL üzerinde olanların 2-5 satırları:")
print(satirlar2_5)

# Yeni DataFrame yazdırma
yeni_df = df[["ad", "soyad", "sektör", "yeni_maaş"]]
print("Yeni DataFrame:")
print(yeni_df)