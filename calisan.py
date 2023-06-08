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

    
   
