myList1 = [1,2,3,4,5,6]
myList2 = ["a","b","c","d","e","f"]

newList = zip(myList1,myList2)

type(newList)

for i in newList:
    print(i)
    list = i

type(list)