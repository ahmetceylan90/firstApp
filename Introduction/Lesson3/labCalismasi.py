#lab1
# try:
#     num = int(input("sayı giriniz"))
#     if num < 0 :
#         print("deger 0'dan büyük ve eşit olmalı")
#     elif num> 100:
#         print("deger 100'dan küçük ve eşit olmalı")
#     else:
#         print("girdiginiz sayi :",num)
# except:
#     pass

#############

#lab2
# try:
#     num = int(input("sayi alalim :"))
#     if num % 2 == 0:
#         print(f"{num} sayisi çifttir")
#     else:
#         print(f"{num} sayisi tektir")
# except:
#     print("değerleri kontrol edin")

#############

#lab3
# try:
#     username = input("username giriniz : ")
#     password = input("şifre giriniz :")

#     if username != "admin":
#         print("username yanlış girdiniz")
#     elif username == "admin" and password != '123':
#         print("şifrenizi yanlış girdiniz")
#     else:
#         print("tebrikler")
    
# except:
#     print("kontrol ediniz")

###########

#lab4

# try:
#     nott = int(input("not gir :"))

#     if nott >= 0 and nott <= 30:
#         print("notunuz FF")
#     elif nott >= 31 and nott <= 50:
#         print("notunuz DD") 
#     elif nott >= 51 and nott <= 70:
#         print("notunuz CC")
#     elif nott >= 71 and nott <= 84:
#         print("notunuz BB")
#     elif nott >= 85 and nott <= 100:
#         print("notunuz AA")
#     else:
#         print("notunuzu kontrol edin")
# except:
#     print("işlem hatalı")

############

#lab5

try:
    urun = input("urun gir :")
    if urun in ("domates","biber","patlıcan"):
        print("sebze")
    elif urun in ("şampuan","deodarant","parfüm"):
        print("kozmetik")
    elif urun in ("tv","pc","kulaklık"):
        print("teknoloji")
    else:
        print("bu ürün çeşidi bizde yok")
except:
    pass