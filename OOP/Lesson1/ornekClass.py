class Personel:
    ad = ""
    soyad = ""
    maas = 500
    departman = ""

    def __init__(self,x,y,z,d) -> None:
        self.ad = x
        self.soyad = y
        self.maas = z
        self.departman = d

    def __str__(self) -> str:
        return f'{self.ad} ve {self.soyad}'

    def updateDept(self,yeni):
         self.departman = yeni 

    def zamYap(self,guncelMaas):
         oran = self.maas / guncelMaas
         self.maas = guncelMaas
         print(oran)

eleman = Personel("ali","veli",500,"IT")

print(eleman)
eleman.updateDept("Marketing")
print(eleman.departman)

eleman.zamYap(1000)
eleman.maas


