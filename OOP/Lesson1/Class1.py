class Employee:
    '''
    DOCSTRING eklenebilir
    '''
    firstName: str  = None # field diye isimlendirilir class içinde
    lastName: str = None
    mail: str = None
    phone: str = None

# instance alma (yeni bir örnek alma)

employee1 = Employee()
employee2 = Employee()

employee1.__doc__

adi = "" # değişken diye isimlendirilir global alanda

