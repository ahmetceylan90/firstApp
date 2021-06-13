class Student:
    """
    self:
    """
    firstName : str = None

    def notVer(self,note):
        print(f"{self.firstName} isimli ögrencinin notu {note}")
    
    def yoklama(self,result):
        print(f'{self.firstName} isimli ögrenci derse gel{( "" if result else "me")}diğinden yoklmada gözükmedi')

    def cezaVer(self,type):
        print(f"{self.firstName} isimli ögrenciye {type}cezası verildi")

ogr1 = Student()
ogr1.firstName = "Ahmet"
ogr1.notVer(80)

ogr2 = Student()
ogr2.firstName = "Gülsüm"

ogr2.cezaVer("disiplin")

ogr2.yoklama(True)