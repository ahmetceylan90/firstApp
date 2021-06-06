def farkHesapla():
    go_on ='y'
    tek_sayilar = []

    while go_on == 'y' or go_on == 'Y':
        number = float(input("sayı gir: "))
        if number % 2 !=0:
            tek_sayilar.append(number)
        go_on = input('yeni sayi girmek ister misiniz y/N :' )
    return max(tek_sayilar) - min(tek_sayilar)

print (farkHesapla())