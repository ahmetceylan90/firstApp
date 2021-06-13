class Employee:
    firstName : str  = None # default degeri null
    lastName : str = "" # çıktı olarak birşey yazmaz
    mail : str = None
    phone : str = ""

emp = Employee()

emp.firstName = "ahmet"
emp.lastName = "ceylan"

emp.firstName

print(emp.firstName)