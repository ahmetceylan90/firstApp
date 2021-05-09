
# yorum satırı eklendi. 
# alt + z alt satıra satıra aşagı kaydırr

print("Hello world")

########### değişken tanımlama kuralları
# 1- sayi ile baslayamaz
# 2- birden fazla kelime ise küçük harfle başlayıp 
# her kelimenin ilk harfi büyük olması tavsiye edilir
# 3- tanımlı klemeiler değişken ismi olarak kullanilmaz
# 4- türkçe karakter kullanmayiniz

############### global alan içerisinde değişken tanımlama

userName = "ahmet"

{
    # bu alan globaldir
    b = 1
    # b değişkenine sadece burdaken ulaşılabilir
    {
        c = 2
        print (b + c)  = 3 ## bu sonucu verir
    }
    print(b+c) # hata alırız çünkü c bir alt kümede değişken olarak oluşturldugu için
}

############ sayısal veri tipleri
# int,float,
age = 10.21
wight = 79
print (age,wight, sep="***")

print (type(age))

# shift + alt + f --> kodları formatlar

########### mantıksal veri tipleri
retval = 2 > 10
print (retval)

########## \n metin içinde bir alt satıra geçmeyi sağlar