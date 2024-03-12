class Student:
    def __init__(self, first_name, last_name, age, gender, weight):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.weight = weight

    def welcome(self):
        return f"Welcome, {self.first_name} {self.last_name}!"

first_name = input("Enter First name: ")
last_name = input("Enter Last name: ")
age = int(input("Enter Age: "))
gender = input("Enter Gender: ")
weight = float(input("Enter Weight: "))

student = Student(first_name, last_name, age, gender, weight)

print(student.welcome())
#Supawit Sangrattanayon 64050694

