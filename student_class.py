"""Create a Student class and initialize it with name and roll number. Make methods to :
1. Display - It should display all informations of the student.
2. setAge - It should assign age to student
3. setMarks - It should assign marks to the student."""

class Student():
    "Student Class with age and marks"

    def __init__(self, name, roll_num):
        self.name= name
        self.roll_num= roll_num
        self.age=0
        self.marks=0
        


    def setAge(self, age):
        "Set Age to Student"
        self.age=age

    def set_marks(self, marks):
        self.marks=marks

    def display(self):
        print("Student Name:", self.name)
        print("Roll_number:", self.roll_num)
        print("Age:", self.age)
        print("Marks:", self.marks)

    

Student_object = Student("Vid", 26)
Student_kavya_object = Student("Kavya", 34)
Student_object.setAge(94)
Student_object.set_marks(78)
Student_object.display()

Student_kavya_object.setAge(30)
Student_kavya_object.set_marks(56)
Student_kavya_object.display()