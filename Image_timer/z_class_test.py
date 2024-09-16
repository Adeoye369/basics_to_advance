from datetime import date


class Person():

    count = 0
    name = "Person Class"

    def __init__(self, n="Any name", age = 0):
        
        self.name = n
        self.age = age
        self.person_count()

    @classmethod
    def create_from_year(cls, name, year):
        return cls(name, date.today().year - year)

    @classmethod
    def set_class_name(cls, n):
        cls.name = n

    @classmethod
    def person_count(cls):
        cls.count += 1 



t4 = Person()
t3 = Person("Oma")
t2 = Person("Omolara", 32)
t1 = Person("Adeoye", 33)
t5 = Person.create_from_year("Omolara", 1999)


print(Person.count)
print(Person.name)
print(t5.age)



