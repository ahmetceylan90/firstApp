sayilar = []

while True:
    print('Çıkmak için e tuşuna basınız')
    val = input('Lütfen sayı giriniz : ')
    if(val == 'e' or val == 'E'):
        break

    sayi = float(val)
    sayilar.append(sayi)


print(sayilar)