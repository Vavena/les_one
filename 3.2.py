class Dog:
    def __init__(self, name, age):
        self._name = name
        self._age = age
    def sit(self):
        return(self._name,'сидит')
    def roll_over(self):
        return(self._name,'перекатилось')

a = Dog('willie', 6)
b = Dog("lucy", 3)
print(a.sit(),a.roll_over())
print(b.sit(),b.roll_over())