from School import School, ClassRoom, Subject
from Persons import Student, Teacher

def main():
    print("Congratulations! Your code is running")
    school = School('Adam Jee', 'U TT RR')
    
    eight = ClassRoom('eight')
    school.add_classroom(eight)
    nine = ClassRoom('nine')
    school.add_classroom(nine)
    ten = ClassRoom('ten')
    school.add_classroom(ten)

    # add students
    abul = Student('Abul khan', eight)
    school.student_admission(abul)
    babul = Student('Babul khan', eight)
    school.student_admission(babul)
    kabul = Student('Kabul khan', eight)
    school.student_admission(kabul)

    # subject & teacher
    physics_teacher = Teacher('Shahjahan')
    physics = Subject('Physics', physics_teacher)
    eight.add_subject(physics)

    chemistry_teacher = Teacher('Hajari Nag')
    chemistry = Subject('chemistry', chemistry_teacher)
    eight.add_subject(chemistry)

    biology_teacher = Teacher('Ajmol')
    biology = Subject('biology', biology_teacher)
    eight.add_subject(biology)

    eight.take_semester_final()
    

    print(school)


if __name__ == '__main__':
    main()