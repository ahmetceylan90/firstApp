# 1 - 
def ornek1():

    num1 = input("ilk sayi : ")
    num2 = input("ikinci sayi : ")

    toplam = int(num1) + int(num2)
    fark = int(num1) - int(num2)
    mod = toplam % fark 
    print(mod)

# 2. problem
def ornek2():
    sayi = input("sayi gir :")
    sayi2 = int(sayi) - 10 + 20
    modSayi = sayi2 % 2
    print(modSayi)

#ornek2()    

#3. problem
def ornek3():
    number1 = input("number1 :")
    number2 = input("number2 :")

    number1 = int(number1)
    number2 = int(number2)

    number1Kare = number1 ** 2
    number2Kare = number2 ** 2

    kareToplam = number1Kare + number2Kare
    kareFark = number1Kare - number2Kare

    sonuc = kareToplam + kareFark
    print(sonuc)

#ornek3()

#4. problem 
def ornek4():
    vize = input("vize gir :")
    final = input("final gir :")

    alinanNot = int(vize) * 0.30 + int(final) * 0.70
    print(alinanNot)

#ornek4()

#5. problem
def ornek5():
    isim = input("isim gir : ")
    soyIsim = input("Soyisim gir : ")
    print(isim + "." + soyIsim + "@hotmail.com")
    mail = "{}.{}@hotmail.com".format(isim,soyIsim) # alternatif 2
    #mail = "{0}.{1}@hotmail.com".format(isim,soyIsim) alternatif 3
    print(mail)
    mail2 = f"{isim}.{soyIsim}@hotmail.com" # alternatif 4
    print(mail2)

ornek5()