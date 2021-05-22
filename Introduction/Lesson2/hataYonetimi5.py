try:
    # db connection 
    # connection open
    # crud işlemleri
    # connection close
    sayi = int(input("sayi giriniz"))
    print("teşekkürler")
except:
    print("hata oldu")
finally:
    # connection close
    print("istisnasız çalıştım")

