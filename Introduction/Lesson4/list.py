# sehirler = ["ist","ank","konya","izmir","ant"]
# sehirler[2]

# sehirler[:3] # 3 dahil değil
# sehirler[1:3] # 1:start indx --> 3:stop index(dahil değil)
# print("istanbul" in sehirler) # true veya false degeri döndürür. var olup olmadıgını kontrol eder.

# sehirler.index("konya") # indx no verir

##### Ternary If ########

def varmi():
    sehirler = ["ist","ank","konya","izmir","ant"]

    sehir = input("şehir gir :")
    result = f'{sehir} şehirler listesinde yer al{("" if sehir in sehirler else "m" )}ıyor' 
    ## eğer sağlıyorsa if den önceki tırnak içini dahil eder , 
    # sağlamıyorsa else den sonraki "" içindeki değerleri dahil eder
    
    print(result)

varmi()

########
#zip ## listeleri birleştiri
#zip(myList1,myList2) 

########

#append liste içine eleman ekleme için kullanılır

sehirler = ["ank","ist"]
sehirler.append("konya")
sehirler

########

# insert() belirli bir pozisyona elaman eklemk için kullanılır

sehirler.insert(1,"bursa")
sehirler

########

# .pop() son eleman siler

sehirler.pop() # indeks verilmezse son elemanı siler
sehirler.pop(0) # verilenindeksi siler

########
#remove --> eleman siler. pop'dan farkı index almadan elemanı direk silebilir
# mükerrer eleamn varsa sağdan sola bulduğı ilk elemanı siler.

myList = [1,2,3,4,5,6,7,1,8]
myList
myList.remove(7)
myList

#########
#sort --> elemanları sıralar
sortMyList = myList.sort()
sortMyList

#reverse --> elemanları tersden sıralar
reverseMyList = myList.reverse()
print(reverseMyList)
myList

#del --> listeyi siler

del myList
myList

