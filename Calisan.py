from Insan import Insan
class Calisan(Insan):
    def __init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas):
        super().__init__(tc_no, ad, soyad, yas, cinsiyet, uyruk)
        self.__sektor = sektor
        self.__tecrube = tecrube
        self.__maas = maas
        self.__yenimaas = None
    # dget ve set metodları:
    def get_sektor(self):
        return self.__sektor

    def set_sektor(self, sektor):
        self.__sektor = sektor

    def get_tecrube(self):
        return self.__tecrube

    def set_tecrube(self, tecrube):
        self.__tecrube = tecrube

    def get_maas(self):
        return self.__maas

    def set_maas(self, maas):
        self.__maas = maas

    def set_yenimaas(self, yenimaas):
        self.__yenimaas = yenimaas

    def get_yenimaas(self):
        return self.__yenimaas

    def zam_hakki(self):
        try:
            zam_orani = 0
            if self.get_tecrube() < 2: # eger 2 den küçükse aşağıdaki işlemler:
                zam_orani = 0  # zam_orani = 0 ata
            elif 2 <= self.get_tecrube() <= 4 and self.get_maas() < 15000: # 2 ile 4 arasındaysa aşağıdaki işlemler:
                zam_orani = self.get_maas() % self.get_tecrube()
            elif self.get_tecrube() > 4 and self.get_maas() < 25000: # 4 den büyükse aşağıdaki işlemler:
                zam_orani = (self.get_maas() % self.get_tecrube()) / 2
            # yeni maaş hesaplama:
            yeni_maas = self.get_maas() + self.get_maas()*zam_orani/100
            if yeni_maas == self.get_maas():
                self.set_yenimaas(yeni_maas)
            else:
                self.set_yenimaas(yeni_maas)

        except Exception as hata: # hata oluşursa yazdırma
            print("Hata bulundu:", hata)
            return self.get_maas()
        # bilgileri str metodu ile yazdırma
    def __str__(self):
        Calisan.zam_hakki(self)
        return f"Ad: {self.get_ad()}\nSoyad: {self.get_soyad()}\nTecrübe: {self.get_tecrube()}\nYeni Maaş: {self.get_yenimaas()}"
