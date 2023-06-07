from insan import Insan

class Issiz(Insan):
    def __init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk, tecrube):
        super().__init__(tc_no, ad, soyad, yas, cinsiyet, uyruk)
        self.__status = self.statu_bul()
        self.__tecrube = tecrube
        

    def get_status(self):
        return self.__status

    def set_status(self):
        self.__status = self.statu_bul()

    def get_tecrube(self):
        return self.__tecrube

    def set_tecrube(self, tecrube):
        self.__tecrube = tecrube

   