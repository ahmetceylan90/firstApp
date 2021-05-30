myList =["a","b","c","d","e","f","g"]

for i in myList:
    newList =[]
    newList.append(i.upper())
    print(newList)

myList =["a","b","c","d","e","f","g"]
yeniListe= []
yeniListe = [x.upper() for x in myList]     

print(yeniListe)