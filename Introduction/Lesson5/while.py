#sonsuz döngü örneği
# while(True):
#     print("abc")

###############
# i = 0
# while i <= 100:
#     if i % 2 == 0:
#         print (i)
#     i = i + 1

##########

# i = 1
# cift = 0
# tek = 0
# while i <= 1000:
#     if i % 2 == 0:
#         cift = cift + 1
#     else:     
#         tek = tek + 1
#     i = i + 1   
# print(cift)

############

# metin = input("metin gir : ")
# uzunluk = 0
# while uzunluk < len(metin):
#     print(metin[uzunluk])
#     uzunluk += 1

########

def new_func():
    num1 =input("sayi :")
    i = 0
    toplam = 0
    while i < len(num1):
        toplam = int(num1[i]) + toplam
        i = i+1
    print(toplam)

new_func()