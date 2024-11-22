class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    def set_details(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    def get_details(self):
        return f"Name: {self.name}\nAge: {self.age}\n Gender: {self.gender}"
        
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
            return sum(self.grade)/len(self.grade)
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
    def set_professor_details(self, staff_id, department, salary):
        self.staff_id = staff_id
        self.department = department
        self.salary = salary
    def give_feedback(self, student, feedback):
        print(f"Feedback for {student}: {feedback}")
    def increase_salary(self, percentage):
        self.salary += self.salary(percentage/100)
    def get_professor_summary(self):
        return f"Name: {self.name}\nAge: {self.age}\nGender: {self.gender}\nStaff Id: {self.staff_id}\nDepartment: {self.department}\nSalary: {self.salary}"
class Admin(Person):
    def __init__(self, name, age, gender, admin_id, office, years_of_service):
        super().__init__(name, age, gender)
        self.admin_id = admin_id
        self.office = office
        self.years_of_service = years_of_service
    def set_admin_details(self, admin_id, office, years_of_service):
        self.admin_id = admin_id
        self.office = office
        self.years_of_service
        
 
 
 
 
 
    
    
student = Student("Kana", 18, "Female", "K18", "Acting")
professor = Professor("Aizen", 90, "Block", "12345", "Spanish", 0)
#professor.give_feedback(student.name, "Nice slap!")