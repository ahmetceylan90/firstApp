from random import randint 

try:
    toplam = int(input("adet gir : "))
except Exception as ex:
    print(ex)
else:
    i = 0
    numbers=[]
    while i < toplam:
        sayilar = set()
        while True:
            sayi = randint(1,49)
            n =str(sayi)
            n= f"0{n}" if len(n) == 1 else n
            sayilar.add(str(n))

            if len(sayilar) == 6:
                sayilar = sorted(sayilar)
                numbers.append(sayilar)
                break
    i += 1
    i= 0
    while i < len(numbers):
        print("-".join(numbers[i]))
        i += 1

