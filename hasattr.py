class Student:
    def __init__(self,id,name,cgpa):
        self.id=id
        self.name=name
        self.cgpa=cgpa
s=Student(10,'ABC',9.63)
print(getattr(s,'id'))
print(hasattr(s,"id"))