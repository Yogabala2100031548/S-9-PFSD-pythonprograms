class Student:
    id = 10
    name = "abc"
    def display(self):
        print(self.id, self.name)
std = Student()
std.display()
del std.id
del std