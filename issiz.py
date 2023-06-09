from insan import Insan

class Issiz(Insan):
    def __init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk, tecrube):
        
        self.__tecrube = tecrube
        self.__status = self.statu_bul()
        super().__init__(tc_no, ad, soyad, yas, cinsiyet, uyruk)
        
        

    def get_status(self):
        return self.__status

    def set_status(self):
        self.__status = self.statu_bul()

    def get_tecrube(self):
        return self.__tecrube

    def set_tecrube(self, tecrube):
        self.__tecrube = tecrube

    def statu_bul(self):
        try:
            etkiler = {
                "mavi yaka": self.__tecrube.get("mavi yaka", 0) * 0.2,
                "beyaz yaka": self.__tecrube.get("beyaz yaka", 0) * 0.35,
                "yönetici": self.__tecrube.get("yönetici", 0) * 0.45
            }
            self.__status = max(etkiler, key=etkiler.get)
        except Exception as e:
            raise Exception("Hata: ", str(e))

    def __str__(self):
        return f"Ad: {self.get_ad()}, Soyad: {self.get_soyad()}, En Uygun Statü: {self.__status}"
