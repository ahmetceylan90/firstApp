dizi = ["a","g","h","k"]

print(sorted(dizi))

mySet = set(sorted("AabscsdSA"))

mySet

locale.setlocale(locale.LC_ALL,locale = "tr_TR.UTF-8")

sonuc = sorted("bilgemadakadıköyankara",key=locale.strxfm)
