# kullanıcı input aracılığıyla uygulamaya sayı girecek, veee kullanıcı dilediği kadar sayı girebilir

# her sayı girildiğinde kullanıcıya yeni bir sayı girecekmisin? diye sorulacak, kullanıcı y tuşuna basarsa lütfen sayı giriniz diyip içeriye sayı alınacak

# kullanıcı harici bir tuşa basarsa, içeride yer alan tek sayıların en küçük ve en büyük sayısının birbirine olan farkını geriye dönsün :


def farkHesapla():
    go_on = 'y'
    tek_sayilar = []

    while go_on == 'y' or go_on == 'Y':
        number = float(input('Lütfen sayı giriniz : '))
        if(number % 2 != 0):
            tek_sayilar.append(number)
        go_on = input('yeni bir sayı eklemek istiyormusunuz (Y/N) : ')

    return max(tek_sayilar) - min(tek_sayilar)


sonuc = farkHesapla()
print('işlem sonucu :', sonuc)