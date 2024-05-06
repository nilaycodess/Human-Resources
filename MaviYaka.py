import pandas as pd
from Calisan import Calisan
class MaviYaka(Calisan): # Calisan sınıfından kalıtım yoluyla nesne oluşturma
    def __init__(self,  tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas, yipranma_payi):
        super().__init__(tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas)
        self.__yipranma_payi = yipranma_payi
        self.__yenimaas = None
    # get ve set metodları:
    def get_yipranma_payi(self):
        return self.__yipranma_payi

    def set_yipranma_payi(self, yipranma_payi):
        self.__yipranma_payi = yipranma_payi

    def set_yenimaas(self, yenimaas):
        self.__yenimaas = yenimaas

    def get_yenimaas(self):
        return self.__yenimaas

    # zam hakki hesaplama:
    def zam_hakki(self):
        try:
            zam_orani = 0
            if self.get_tecrube() < 2: #eğer tecrübe 2 den küçükse:
                zam_orani = self.get_yipranma_payi() * 10
            elif 2 <= self.get_tecrube() <= 4 and self.get_maas() < 15000: # 2 ile 4 arasındaysa:
                zam_orani = (self.get_maas() % self.get_tecrube()) / 2 + (self.get_yipranma_payi() * 10)
            elif self.get_tecrube() > 4 and self.get_maas() < 25000: # 4ten büyükse:
                zam_orani = (self.get_maas() % self.get_tecrube()) / 3 + (self.get_yipranma_payi() * 10)
            # yeni maaş hesaplama:
            yeni_maas = int(self.get_maas() + self.get_maas()*zam_orani/100)
            if yeni_maas == self.get_maas():
                self.set_yenimaas(yeni_maas)
            else:
                self.set_yenimaas(yeni_maas)

        except Exception as hata: # hata bulunma durumunda ekrana yazdırır.
            print("Hata bulundu:", hata)
            return self.get_maas()

    # str metodu ile bilgileri yazdırma
    def __str__(self):
        MaviYaka.zam_hakki(self)
        return f"Ad: {self.get_ad()}\n" \
               f"Soyad: {self.get_soyad()}\n" \
               f"Tecrube: {self.get_tecrube()}\n" \
