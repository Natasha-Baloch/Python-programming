class Student:
    def __init__(self,name,maths,physics,chemistry):
        self.name = name
        self.maths = maths
        self.physics = physics
        self.chemistry = chemistry

    def average(self):
        return (self.maths+self.physics+self.chemistry)/3


s1 = Student("Natasha",89,99,78)
print(s1.name)
print(s1.average())
            