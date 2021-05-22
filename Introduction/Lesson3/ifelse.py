user = input("kullanici adi giiniz : ")
user = user.lower().replace('ç','c')

if user=="admin":
    print("Ana sayfya gidiyorsunuz")
else:
    print("hata aldınız")

#karşılaştırma operatorleri

# ==  soldaki değer sağdaki değere eşitse 
# != soldaki değer sağdaki degere eşit değilse
# > soldaki degerin sagdakinden büyük olma durumu
# < soldaki değer sağdaki değerden küçük olma durumu
# >=  soldaki degerin sagdakinden büyük veya eşit olma durumu
# <= soldaki değer sağdaki değerden küçük veya eşit olma durumu
