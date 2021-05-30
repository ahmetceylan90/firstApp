from sehirler import sehirler

for sehir in sehirler:
    print(sehir["Name"],"-" * (30 - len(sehir["Name"])))

    for x,y in sehir.items():
        print(f"{x:<15}:{y}")
    #      print("""
    #  Şehir -----------------------
    #  Şehir Id           : {0}
    #  Şehir Adı          : {1}
    #  Şehir Plaka Kodu   : {2}
    #  Şehir Telefon Kodu : {3}
    #      """.format())
