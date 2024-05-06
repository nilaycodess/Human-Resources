import pandas as pd
from Calisan import Calisan
class BeyazYaka(Calisan):
    def __init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas, tesvik_primi):
        super().__init__(tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas)
        self.__tesvik_primi = tesvik_primi
        self.__yenimaas = None

    def get_tesvik_primi(self):
        return self.__tesvik_primi

    def set_tesvik_primi(self, tesvik_primi):
        self.__tesvik_primi = tesvik_primi

    def set_yenimaas(self, yenimaas):
        self.__yenimaas = yenimaas

    def get_yenimaas(self):
        return self.__yenimaas

    def zam_hakki(self):
        try:
            zam_orani = 0 # başta zam oranına 0 değeri atanır
            # zam hakkı hesaplaması:
            if self.get_tecrube() >= 2 and self.get_tecrube() <= 4 and self.get_maas() <= 15000:
                zam_orani = (self.get_maas() % self.get_tecrube()) * 5 + self.get_tesvik_primi()
            elif self.get_tecrube() > 4 and self.get_maas() <= 25000:
                zam_orani = (self.get_maas() % self.get_tecrube()) * 4 + self.get_tesvik_primi()
            # yeni maaaş hesaplaması
            yeni_maas = int(self.get_maas() + zam_orani)
            if yeni_maas == self.get_maas():
                self.set_yenimaas(yeni_maas)
            else:
                self.set_yenimaas(yeni_maas)

        except Exception as hata: # hata oluşursa yazdırma
            print("Hata:", str(hata))
    # str metodu ile bilgileri yazdırma
    def __str__(self):
        BeyazYaka.zam_hakki(self)
        return f"Ad: {self.get_ad()}\nSoyad: {self.get_soyad()}\nTecrübe: {self.get_tecrube()}\nYeni Maaş: {self.get_yenimaas()}"