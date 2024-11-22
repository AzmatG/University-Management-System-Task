class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        self.mentor = ""
    def set_details(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    def get_details(self):
        return f"Name: {self.name}\nAge: {self.age}\n Gender: {self.gender}"
    def get_mentor(self):
        try:
            return f"{self.mentor} is mentoring {self.name}"
        except len(self.mentor) == 0:
            return "No mentor assigned."
class Student(Person):
    def __init__(self, name, age, gender, student_id, course):
        super().__init__(name, age, gender)
        self.student_id = student_id
        self.course = course
        self.grade = []
    def set_student_details(self, student_id, course):
        self.student_id = student_id
        self.course = course
    def add_grade(self, grade):
        self.grade.append(grade)
    def calculate_average_grade(self):
        try: 
            return round(sum(self.grade)/len(self.grade), 2)
        except:
            return "an exception has occurred."
    def get_student_summary(self):            
        return f"Name: {self.name}\nAge: {self.age}\nGender: {self.gender}\nStudent_id: {self.student_id}\nGrades: {self.grade}"
class Professor(Person):
    def __init__(self, name, age, gender, staff_id, department, salary):
        super().__init__(name, age, gender)
        self.staff_id = staff_id
        self.department = department
        self.salary = salary
        self.mentors = []
    def set_professor_details(self, staff_id, department, salary):
        self.staff_id = staff_id
        self.department = department
        self.salary = salary
    def give_feedback(self, student, feedback):
        return f"Feedback for {student.name}: {feedback}"
    def increase_salary(self, percentage):
        self.salary += self.salary*(percentage/100)
    def get_professor_summary(self):
        return f"Name: {self.name}\nAge: {self.age}\nGender: {self.gender}\nStaff Id: {self.staff_id}\nDepartment: {self.department} department\nSalary: {self.salary}"
    def mentor_student(self, student):
        self.mentors.append(student.name)
        student.mentor = self.name
        return f"{self.name} is now mentoring {student.name} on {student.course}."
    def get_mentored_students(self):
        try:
            return f"{self.name} is mentoring {self.mentors}"
        except len(self.mentors) == 0:
            return f"{self.name} is mentoring no one"
class Admin(Person):
    def __init__(self, name, age, gender, admin_id, office, years_of_service):
        super().__init__(name, age, gender)
        self.admin_id = admin_id
        self.office = office
        self.years_of_service = years_of_service
    def set_admin_details(self, admin_id, office, years_of_service):
        self.admin_id = admin_id
        self.office = office
        self.years_of_service = years_of_service
    def increment_service_years(self):
        self.years_of_service += 1
    def get_admin_summary(self):
        return f"Name: {self.name} \nAge:{self.age} \nGender: {self.gender} \nAdmin_Id: {self.admin_id}   \nOffice: {self.office} \nYears of Service: {self.years_of_service}"
        
        
 
 
 #A Showcase of functionality
 
 
    
    
student = Student("Kana", 18, "Female", "K18", "Acting")
professor = Professor("Aizen", 90, "Block", "12345", "Spanish", 100)
admin = Admin("Himmel", 65, "Male", "H65", "Room 12F", 23)
print("\nAdding grades\n")
print(student.get_student_summary())
student.add_grade(90)
student.add_grade(10)
student.add_grade(40)
print(student.get_student_summary())
print(f"Average grade => {student.calculate_average_grade()}")
print("\nProfessor Things\n")

print(professor.give_feedback(student, "Good Work!"))
print(f"Old Salary => {professor.salary}")
professor.increase_salary(10)
print(f"New Salary => {professor.salary}")

print("\nAdmin Things\n")
print(f"Old years => {admin.years_of_service}")
admin.increment_service_years()
print(f"New Years => {admin.years_of_service}")

print("\nMentoring System\n")

print(professor.mentor_student(student))
print(student.get_mentor())
print(professor.get_mentored_students())