from calisan import Calisan
# Bu test branchidir
class BeyazYaka(Calisan):
    def __init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas, tesvik_primi):
        super().__init__(tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas)
        self.__tesvik_primi = tesvik_primi
        self.__yeni_maas_beyaz_yaka = self.zam_hakki()

    def get_tesvik_primi(self):
        return self.__tesvik_primi

    def set_tesvik_primi(self, tesvik_primi):
        self.__tesvik_primi = tesvik_primi

    def get_yeni_maas_beyaz_yaka(self):
        return self.__yeni_maas_beyaz_yaka
    
    def set_yeni_maas_beyaz_yaka(self):
        self.__yeni_maas_beyaz_yaka = self.zam_hakki()
    
    def zam_hakki(self):
        try:
            if self.get_tecrube() < 2:
                return self.__tesvik_primi + self.get_eski_maas()
        
            elif 2 <= self.get_tecrube() <= 4 and self.get_maas() < 15000:
                return ((self.get_eski_maas() / self.get_tecrube()) * 5)+ self.__tesvik_primi + self.get_eski_maas()
            
            elif self.get_tecrube() > 4 and self.get_eski_maas() < 25000:
                return ((self.get_eski_maas() / self.get_tecrube()) * 4) + self.__tesvik_primi + self.get_eski_maas()
            
            else:
                return self.get_eski_maas()
        
        except Exception as e:
            raise Exception(f"Hata: {str(e)}")

    def __str__(self):
        return f"Ad: {self.get_ad()}, Soyad: {self.get_soyad()}, Tecrübe: {self.get_tecrube()}, Yeni Maaş: {self.__yeni_maas_beyaz_yaka()}"
