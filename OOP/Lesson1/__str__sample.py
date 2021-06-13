class Personel:
    adi = ""
    soyadi = ""
    yas = 0

    def __str__(self) -> str:
        # default olarak ram deki adresini getiri. burda yapılacak değişiklikle
        # override edilebilr aşagıdaki örnekteki gibi

        return f'{self.soyadi}'

per = Personel()

per.adi = "ali"
per.soyadi = "veli"
per.yas = 100
