from random import randint 

i=0
sayi=[]
while i<6:
    if i not in sayi:
        sayi.append(randint(1,49))
    i += 1
print(sayi)