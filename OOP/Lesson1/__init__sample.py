from datetime import datetime

class Personnel:
    adi: str = None
    soyAdi : str = None
    telefon:str = None
    mail:str = None
    kayitTarihi:str = None

    def __init__(self,firstname,lastname,telefon,mail) -> None:
        self.adi =  firstname
        self.soyAdi = lastname
        self.telefon = telefon
        self.mail = mail
        self.kayitTarihi = datetime.now()
    
    def __str__(self) -> str:
        return (f"adi : {self.adi}")

#per = Personnel()
# per.adi = 'ahmet'
# per.soyAdi = 'ceylan'

per1 = Personnel("ahmet","ceylan","ahmet.ceylan@gmail.com","12345")

print(per1)