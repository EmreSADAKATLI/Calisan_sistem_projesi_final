class Insan:
    """
    İnsan sınıfında (Insan.py); tc_no, ad, soyad, yaş, cinsiyet, uyruk bilgileri private değişkenleri olarak 
    bulunmalıdır
    """
    def __init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk):
        # __ ise private
        self.__tc_no = tc_no
        self.__ad = ad
        self.__soyad = soyad
        self.__yas = yas
        self.__cinsiyet = cinsiyet
        self.__uyruk = uyruk

  
