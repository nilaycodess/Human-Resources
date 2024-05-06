from Insan import Insan
class Issiz(Insan): # Insan sınıfından kalıtım yoluyla nesneler oluşturma
    def __init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk, tecrubeler):
        # super() metodu ile Insan sınıfının nesnelerine ulasıyoruz
        super().__init__(tc_no, ad, soyad, yas, cinsiyet, uyruk)
        # tecrubeler nesnesini de private olarak atıyoruz
        self.__tecrubeler = tecrubeler
        self.__oneri = None

    # get metodu ile tecrübe bilgilerine ulaşma
    def get_tecrubeler(self):
        return self.__tecrubeler
    # set metodu ile tecrubeler private değişkenine bir değer atama
    def set_tecrubeler(self, tecrubeler):
        self.__tecrubeler = tecrubeler

    def get_oneri(self):
        return self.__oneri

    def set_oneri(self, oneri):
        self.__oneri = oneri

    def statu_bul(self):
        try:
            mavi_yaka_etkisi = 0.2*self.__tecrubeler["Maviyaka"]
            beyaz_yaka_etkisi = 0.35*self.__tecrubeler["Beyazyaka"]
            yonetici_etkisi = 0.45*self.__tecrubeler["Yönetici"]

            if beyaz_yaka_etkisi > mavi_yaka_etkisi and beyaz_yaka_etkisi > yonetici_etkisi:
                self.set_oneri("Beyazyaka")
            elif mavi_yaka_etkisi > beyaz_yaka_etkisi and mavi_yaka_etkisi > yonetici_etkisi:
                self.set_oneri("Mavi yaka")
            else:
                self.set_oneri("Yönetici")

        except Exception as hata:
            print("Hata bulundu:", hata)

    # str metodu ile bilgileri yazdırma
    def __str__(self):
        Issiz.statu_bul(self)
        return f"Ad: {self.get_ad()}\n" \
               f"Soyad: {self.get_soyad()}\n" \
               f"Statü önerisi: {self.get_oneri()}\n"
