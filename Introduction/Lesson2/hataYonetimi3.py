try:
    num = int(input("sayi giriniz :"))
    #num = num / 0
    print("islem basarili")
except ZeroDivisionError as hata2:
    print("[ERROR LOG] :", hata2)
except ValueError as hata3:
    print("[ERROR LOG] :", hata3)
except Exception as hata: # exceptinon en genel hata yakalama tipidir en son satırda yer almalıdır
    print("islem hatasi") # kullanci bilgilendirme mesajı
    print("[ERROR LOG] :", hata) # loglama için olusturduk , kullaniciya sisteme hata mesajlari gösterilmez