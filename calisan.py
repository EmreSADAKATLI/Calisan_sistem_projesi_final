from insan import Insan


class Calisan(Insan):
    def __init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas):
        super().__init__(tc_no, ad, soyad, yas, cinsiyet, uyruk)
        self.__sektor = sektor
        self.__tecrube = tecrube
        self.__eski_maas = maas
        self.__yeni_maas = self.zam_hakki()

    def get_sektor(self):
        return self.__sektor

    def set_sektor(self, sektor):
        self.__sektor = sektor

    def get_tecrube(self):
        return self.__tecrube

    def set_tecrube(self, tecrube):
        self.__tecrube = tecrube

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
            if self.__tecrube < 2:
                return 0 + self.__eski_maas
            
            elif self.__tecrube <= 4 and self.__maas < 15000:
                return (self.__maas / self.__tecrube) + self.__eski_maas
            
            elif self.__tecrube > 4 and self.__maas < 25000:
                return ((self.__maas / self.__tecrube) / 2) + self.__eski_maas
                    
            else:
                return self.__eski_maas
            
        except Exception as e:
            raise Exception("Hata: ", str(e))


    def __str__(self):
        return f"Ad: {self.get_ad()}, Soyad: {self.get_soyad()}, Tecrübe: {self.__tecrube}, Yeni Maaş: {self.__yeni_maas}"
