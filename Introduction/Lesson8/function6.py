def temizle(string : str):
    myList= []
    myList = string.split() 
    
    for n in range(len(myList)):
         if myList[n] not in ("ç","ş","ğ","ö","ü"):
             myList.append([n])
    return myList

print(temizle("a" "b" "c"))

