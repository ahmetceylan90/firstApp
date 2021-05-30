def harfAdetBul(m):
    sesliHarfler = ["a","e","i","ı","o","ö","u","ü"]
    m = list(m)
    metinSesli = list()
    metinSessiz = list()

    sesliToplam = 0
    sessizToplam = 0

    for i in m:
        if i in sesliHarfler:
            sesliToplam += 1
           
        else:
            sessizToplam += 1
            
    print(f"sesliAdet : {sesliToplam}, sessizToplam {sessizToplam}")


harfAdetBul("abcç")