from insan import Insan

class Issiz(Insan):
    def __init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk, tecrube):
        super().__init__(tc_no, ad, soyad, yas, cinsiyet, uyruk)
        self.__status = self.statu_bul()
        self.__tecrube = tecrube
        

