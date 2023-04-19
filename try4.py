import datetime
from dateutil.relativedelta import relativedelta


class Person:
    def __init__(self, dob):
        self._dob = dob

    @property
    def age(self):
        return relativedelta(datetime.datetime.today(), self._dob).years
    
    @age.setter
    def age(self, value):
        today = datetime.datetime.today()
        self._dob = today.replace(year=today.year - value)


moshe = Person(datetime.datetime(2000, 4, 1))
print(moshe.age)
moshe.age = 33
print(moshe.age)