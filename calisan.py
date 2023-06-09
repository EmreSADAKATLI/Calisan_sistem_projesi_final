from insan import Insan


class Calisan(Insan):
    def __init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube,  maas):
        self.__sektor = sektor
        self.tecrube = tecrube
        self.__eski_maas = maas
        self.__yeni_maas = self.zam_hakki()
        super().__init__(tc_no, ad, soyad, yas, cinsiyet, uyruk)
        

    def get_sektor(self):
        return self.__sektor

    def set_sektor(self, sektor):
        self.__sektor = sektor

    def get_tecrube(self):
        return self.tecrube

    def set_tecrube(self, tecrube):
        self.tecrube = tecrube

    def get_eski_maas(self):
        return self.__eski_maas

    def set_eski_maas(self, maas):
        self.__eski_maas = maas

    def get_yeni_maas(self):
        return self.__yeni_maas
    
    def set_yeni_maas(self):
        return self.zam_hakki()

    
    def zam_hakki(self):
        try:
            if self.tecrube < 2:
                return 0 + self.__eski_maas
            
            elif self.tecrube <= 4 and self.__eski_maas < 15000:
                return (self.__eski_maas / self.tecrube) + self.__eski_maas
            
            elif self.tecrube > 4 and self.__eski_maas < 25000:
                return ((self.__eski_maas / self.tecrube) / 2) + self.__eski_maas
                    
            else:
                return self.__eski_maas
            
        except Exception as e:
            raise Exception("Hata: ", str(e))


    def __str__(self):
        return f"Ad: {self.get_ad()}, Soyad: {self.get_soyad()}, Tecrübe: {self.__tecrube}, Yeni Maaş: {self.__yeni_maas}"
