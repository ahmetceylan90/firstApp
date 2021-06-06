isim = input("isim gir : ")
soyIsim = input("Soy isim gir : ")

def isimSoyisim(x,y):
    sonuc = x[:2].upper() + x[2:]
    sonuc2 = y.lower().replace("a","e")
    sonuc3 = (f"{sonuc}.{sonuc2}@hotmail.com")
    return sonuc,sonuc2,sonuc3

print("isim,soyisim",isimSoyisim(isim,soyIsim))
    
