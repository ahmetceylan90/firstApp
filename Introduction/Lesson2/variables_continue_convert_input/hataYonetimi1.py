try:
    sayi1 = int(input("ilk sayi : "))
    sayi2 = int(input("ikinci sayi : "))

    toplam = sayi2 + sayi1
    fark =  sayi1 - sayi2
    carp = sayi1 * sayi2
    bol = sayi1 / sayi2

    print(f"toplama : {toplam} \n fark : {fark} \n carp : {carp} \n bol : {bol}")
except ValueError:
    print("valueerror")
except ZeroDivisionError:
    print("ZeroDivisionError")
except:
    print("sayi giriniz")

# programci hatalari

# istisnai hatalar --> kesin çözümü olmayabilir. örn. network kopması , elektrik kesintisi

# mantiksal hatalar --> çözümü en zor hatalardır

# try:

#     sayi = int(input("sayi giriniz"))
#     print (f"tebrikler {sayi} girdiniz")
# except:
#     print("olmadı")

# print("devam etti")
