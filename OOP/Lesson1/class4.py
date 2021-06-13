from datetime import datetime,timedelta


class Employee:
    first: str = None
    last: str = None
    mail: str = None 
    hireDate : str = f'{datetime.now().day}/{datetime.now().month}/{datetime.now().year}'
    fireDays : int = 0
    fireDate:str = 'Kadrolu olarak alınmıştır'

    def iseAl(self):
        if self.fireDays>0:
            time : datetime = datetime.now() + timedelta(days=self.fireDays)
            self.fireDate = f'{time.day}/{time.month}/{time.year}'

emp = Employee()

print(emp.hireDate)