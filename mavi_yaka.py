from calisan import Calisan

class MaviYaka(Calisan):
    def __init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, maas, tecrube, yipranma_payi):
        self.__yipranma_payi = yipranma_payi
        self.set_tecrube(tecrube)
        self.set_eski_maas(maas)
        self.__yeni_maas_mavi_yaka = self.zam_hakki()
        super().__init__(tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube,  maas)
        

    def get_yipranma_payi(self):
        return self.__yipranma_payi

    def set_yipranma_payi(self, yipranma_payi):
        self.__yipranma_payi = yipranma_payi

    def get_yeni_maas_mavi_yaka(self):
        return self.__yeni_maas_mavi_yaka
    
    def set_yeni_maas_mavi_yaka(self):
        self.__yeni_maas_mavi_yaka = self.zam_hakki()


    def zam_hakki(self):
        try:
            if self.get_tecrube() < 2:
                return (10 * self.__yipranma_payi) + self.get_eski_maas()
        
            elif self.get_tecrube() <= 4 and self.get_eski_maas() < 15000:
                return ((self.get_eski_maas() / self.get_tecrube()) / 2) + (self.__yipranma_payi * 10) + self.get_eski_maas()
            
            elif self.get_tecrube() > 4 and self.get_eski_maas() < 25000:
                return ((self.get_eski_maas() / self.get_tecrube()) / 3) + (self.__yipranma_payi * 10) + self.get_eski_maas()

            else:
                return self.get_eski_maas()
        
        except Exception as e:
            raise Exception(f"Hata: {str(e)}")

    def __str__(self):
        return f"Ad: {self.get_ad()}, Soyad: {self.get_soyad()}, Tecrübe: {self.get_tecrube()}, Yeni Maaş: {self.__yeni_maas_mavi_yaka}"
