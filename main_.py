import pandas as pd
from insan import Insan
from calisan import Calisan
from beyaz_yaka import BeyazYaka
from mavi_yaka import MaviYaka
from issiz import Issiz

insan1 = Insan("11111111111", "Ahmet", "Yılmaz", 30, "Erkek", "Türk")
insan2 = Insan("22222222222", "Ayşe", "Demir", 25, "Kadın", "Türk")

issiz_dict = {'mavi yaka': 2, 'beyaz yaka': 3, 'yönetici': 10}

issiz1 = Issiz("33333333333", "Ali", "Kara", 40, "Erkek", "Türk", issiz_dict)
issiz2 = Issiz("44444444444", "Fatma", "Beyaz", 35, "Kadın", "Türk", issiz_dict)
issiz3 = Issiz("55555555555", "Mehmet", "Yeşil", 45, "Erkek", "Türk", issiz_dict)

calisan1 = Calisan("66666666666", "Ahmet", "Yıldız", 35, "Erkek", "Türk", "Teknoloji", 3, 10000)
calisan2 = Calisan("77777777777", "Ayşe", "Kara", 28, "Kadın", "Türk", "Muhasebe", 5, 20000)
calisan3 = Calisan("88888888888", "Mehmet", "Beyaz", 40, "Erkek", "Türk", "İnşaat", 7, 30000)

maviyaka1 = MaviYaka("99999999999", "Ali", "Yeşil", 32, "Erkek", "Türk", "Üretim",  15000, 5,  200)
maviyaka2 = MaviYaka("10101010101", "Fatma", "Kara", 30, "Kadın", "Türk", "Lojistik",  12000, 3,  150)
# bir tane daha mavi yaka oluşturulacak 

beyazyaka1 = BeyazYaka("12121212121", "Ahmet", "Beyaz", 38, "Erkek", "Türk", "İnsan Kaynakları", 5, 18000, 500)
beyazyaka2 = BeyazYaka("13131313131", "Ayşe", "Yeşil", 42, "Kadın", "Türk", "Finans", 6, 22000, 800)
# bir tane daha beyaz yaka oluşturulacak 

calisanlar = [calisan1, calisan2, calisan3, maviyaka1, maviyaka2, beyazyaka1, beyazyaka2]


# Boş bir veri çerçevesi oluşturulur
df = pd.DataFrame(columns=["T.C. Kimlik No", "Ad", "Soyad", "Yaş", "Cinsiyet", "Uyruk", "Yıpranma Payı", "Teşvik Primi", "Maaş", "Yeni Maaş", "Tecrübe", "Sektör", "Grup"])

# Çalışanları dolaşarak veri çerçevesine eklenirken gruplandırma ve hesaplama yapılır
dfs = []
for calisan in calisanlar:
    if isinstance(calisan, BeyazYaka):
        grup = "Beyaz Yaka"
    elif isinstance(calisan, MaviYaka):
        grup = "Mavi Yaka"
    else:
        grup = "Diğer"
    
    # Create a dictionary with calisan data
    calisan_data = {
        "T.C. Kimlik No": calisan.get_tc_no(),
        "Ad": calisan.get_ad(),
        "Soyad": calisan.get_soyad(),
        "Yaş": calisan.get_yas(),
        "Cinsiyet": calisan.get_cinsiyet(),
        "Uyruk": calisan.get_uyruk(),
        "Yıpranma Payı": calisan.get_yipranma_payi() if hasattr(calisan, "get_yipranma_payi") else 0,
        "Teşvik Primi": calisan.get_tesvik_primi() if hasattr(calisan, "get_tesvik_primi") else 0,
        "Maaş": calisan.get_eski_maas(),
        "Yeni Maaş": calisan.get_yeni_maas(),
        "Sektör": calisan.get_sektor(),
        "Tecrübe": calisan.get_tecrube(),
        "Grup": grup
    }
    