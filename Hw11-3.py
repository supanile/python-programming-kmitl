class Student:
    def __init__(self):
        self.name = ""
        self.sex = ""

    def setName(self, n):
        self.name = n

    def setSex(self, s):
        self.sex = s

    def getName(self):
        return self.name

    def getSex(self):
        return self.sex

    def student_info(self):
        return f"Student 1\nName: {self.name}\nSex: {self.sex}\n"
    
    def student_info2(self):
        return f"Student 2\nName: {self.name}\nSex: {self.sex}"
            
s1 = Student()
s1.setName(input("Enter name for student 1: "))
s1.setSex(input("Enter sex for student 1: "))

s2 = Student()
s2.setName(input("Enter name for student 2: "))
s2.setSex(input("Enter sex for student 2: "))

print(s1.student_info())
print(s2.student_info2())
#Supawich Sangrattanayon 64050694

