def ascii(string : str ):
    for i in range(len(string)):
        toplam = 0
        toplam += int(ord(string[i]))
    return toplam

result = ascii(input("değerler gir : "))

print(result)