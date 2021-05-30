sayilar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
           11, 12, 13, 14, 15, 16, 17, 18, 
           19, 20, 12, 43, 56, 76, 87, 98, 
           56, 78, 91, 212, 344, 5, 6, 4, 453, 23, 11, 21, 32, 43, 56]

i=0
while i< len(sayilar):
    if sayilar[i] % 2 == 0:
        ciftSayilar=[]
        ciftSayilar.append(sayilar[i])
    else:
        tekSayilar=[]
        tekSayilar.append(sayilar[i])
    i = i+1    
print(ciftSayilar)
print(tekSayilar)

