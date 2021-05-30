metin = input("metin gir :")
sesliHarfler=["a","e","i","ı","u","ü","o","ö","A","E","I","İ","O","Ö","U","Ü"]
yeniSesli=[]
yeniSessiz=[]
i=0
while i <len (metin):
    if metin[i] in sesliHarfler:
        yeniSesli.append(metin[i])
    else:
        yeniSessiz.append(metin[i])
    i += 1

print(yeniSessiz)
print(yeniSesli)