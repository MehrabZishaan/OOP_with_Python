import random
from School import School
class Person:
    def __init__(self, name):
        self.name = name

class Teacher(Person):
    def __init__(self, name):
        super().__init__(name)

    def teach(self):
        pass

    def __repr__(self):
        return f'{self.name}'

    def evaluate_exam(self):
        marks = random.randint(0, 100)
        return marks
            # Todo: set marks for the subject for each student

class Student(Person):
    def __init__(self, name, classroom):
        super().__init__(name)
        self.__id = None
        self.classroom = classroom
        self.marks = {}
        self.subject_grade = {}
        self.grade = None

    def calculate_final_frade(self):
        sum = 0
        for grade in self.subject_grade.values():
            # print(self.name, grade)     
            point = School.grade_to_value(grade)
            sum += point
            print(self.name, grade, point)
        points_average = sum/len(self.subject_grade)
        self.grade = School.value_to_grade(points_average)
        print(f"{self.name} Final Grade: {self.grade} with point average {points_average}")
    
    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id == value