class Student:
    def __init__(self,fullname,rollno):
        self.fullname = fullname
        self.rollno = rollno
        print("New Student Added-------")


s1 = Student("Natasha",18)
print("Student Name is ",s1.fullname)
print("Student Roll No is ",s1.rollno)   


s2 = Student("Aliza",19)
print("Student Name is ",s2.fullname)
print("Student Roll No is ",s2.rollno)   


s3 = Student("Ayesha",20)
print("Student Name is ",s3.fullname)
print("Student Roll No is ",s3.rollno)