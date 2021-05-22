try:
    num1= int(input("sayi 1"))
    num2= int(input("sayi 2"))
    sonuc = num1/num2
    print("sonuc",sonuc)
except ValueError as ve:
    #pass şimdilik exception yazmak istemedigimizde buraya pass ekleyebilirz
    print("[ERROR Log]", ve)
else:
    try:
        print(num1/num2)
        print("islem sonucu")
    except ZeroDivisionError as  zd:
        print(zd) 
