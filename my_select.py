from sqlalchemy import func, desc
from connect_db import session
from model import Group, Student, Subject, Grade, Teacher


def select_1():
    # Знайти 5 студентів із найбільшим середнім балом з усіх предметів.
    print('\nSelect 1')
    top_students = session.query(Student, func.avg(Grade.grade).label('average_grade')). \
        join(Grade). \
        group_by(Student). \
        order_by(desc('average_grade')). \
        limit(5).all()

    for student, average_grade in top_students:
        print(f"Student: {student.student_name}, Average Grade: {average_grade:.2f}")


def select_2():
    # Знайти студента із найвищим середнім балом з певного предмета.
    print('\nSelect 2')
    subject_name = "Mathematics"
    top_student = session.query(Student, func.avg(Grade.grade).label('average_grade')). \
        join(Grade). \
        join(Subject). \
        filter(Subject.subject_name == subject_name). \
        group_by(Student). \
        order_by(desc('average_grade')). \
        first()

    if top_student:
        student, average_grade = top_student
        print(f"Top student: {student.student_name}, Average Grade: {average_grade:.2f}, Subject: {subject_name}")
    else:
        print(f"No student found for the subject: {subject_name}")


def select_3():
    # Знайти середній бал у групах з певного предмета.
    print('\nSelect 3')
    subject_name = "Physics"
    average_grades_by_group = session.query(Group.group_name, func.avg(Grade.grade).label('average_grade')). \
        select_from(Group). \
        join(Student). \
        join(Grade). \
        join(Subject). \
        filter(Subject.subject_name == subject_name). \
        group_by(Group.group_name). \
        all()

    if average_grades_by_group:
        print(f"Subject: {subject_name}")
        for group_name, average_grade in average_grades_by_group:
            print(f"Group: {group_name}, Average Grade: {average_grade:.2f}")
    else:
        print(f"No data found for the subject: {subject_name}")


def select_4():
    # Знайти середній бал на потоці (по всій таблиці оцінок).
    print('\nSelect 4')
    average_grade = session.query(func.avg(Grade.grade)).scalar()

    if average_grade is not None:
        print(f"Average Grade across all grades: {average_grade:.2f}")
    else:
        print("No grades found in the table.")


def select_5():
    # Знайти, які курси читає певний викладач.
    print('\nSelect 5')
    teacher_name = "Teacher 1"

    courses_taught_by_teacher = session.query(Subject.subject_name). \
        join(Teacher). \
        filter(Teacher.teacher_name == teacher_name). \
        all()

    if courses_taught_by_teacher:
        print(f"Courses taught by {teacher_name}:")
        for course in courses_taught_by_teacher:
            print(course.subject_name)
    else:
        print(f"No courses found for teacher: {teacher_name}")


def select_6():
    # Знайти список студентів у певній групі.
    print('\nSelect 6')
    group_name = 'Group 1'

    all_student_by_group = session.query(Student.student_name). \
        join(Group). \
        filter(Group.group_name == group_name). \
        all()

    if all_student_by_group:
        print(f"Students in {group_name}:")
        for student in all_student_by_group:
            print(student.student_name)
    else:
        print(f"No students found in group: {group_name}")


def select_7():
    # Знайти оцінки студентів в окремій групі з певного предмета.
    print('\nSelect 7')
    group_name = 'Group 2'
    subject_name = 'Biology'

    grades_in_group_for_subject = session.query(Student.student_name, Grade.grade). \
        join(Grade). \
        join(Group). \
        join(Subject). \
        filter(Group.group_name == group_name, Subject.subject_name == subject_name). \
        all()

    if grades_in_group_for_subject:
        print(f"Grades of students in {group_name} for {subject_name}:")
        for student_name, grade in grades_in_group_for_subject:
            print(f"Student: {student_name}, Grade: {grade}")
    else:
        print(f"No grades found for {subject_name} in group: {group_name}")


def select_8():
    # Знайти середній бал, який ставить певний викладач зі своїх предметів.
    print('\nSelect 8')
    teacher_name = 'Teacher 2'
    average_grade_by_teacher = session.query(func.avg(Grade.grade)). \
        join(Subject). \
        join(Teacher). \
        filter(Teacher.teacher_name == teacher_name). \
        scalar()

    if average_grade_by_teacher is not None:
        print(f"Average grade given by {teacher_name}: {average_grade_by_teacher:.2f}")
    else:
        print(f"No grades found for teacher: {teacher_name}")


def select_9():
    # Знайти список курсів, які відвідує певний студент.
    print('\nSelect 9')
    student_name = "Felicia Kelly"

    # Query to find the courses attended by the specific student
    courses_attended_by_student = session.query(Subject.subject_name). \
        join(Grade). \
        join(Student). \
        filter(Student.student_name == student_name). \
        all()

    if courses_attended_by_student:
        print(f"Courses attended by {student_name}:")
        for course in courses_attended_by_student:
            print(course.subject_name)
    else:
        print(f"No courses found for student: {student_name}")


def select_10():
    # Список курсів, які певному студенту читає певний викладач.
    print('\nSelect 10')
    student_name = 'Felicia Kelly'
    teacher_name = 'Teacher 3'

    courses_attended_by_student_from_teacher = session.query(Subject.subject_name). \
        join(Grade). \
        join(Student). \
        join(Teacher). \
        filter(Student.student_name == student_name, Teacher.teacher_name == teacher_name). \
        all()

    if courses_attended_by_student_from_teacher:
        print(f"Courses attended by {student_name}, taught by {teacher_name}:")
        for course in courses_attended_by_student_from_teacher:
            print(course.subject_name)
    else:
        print(f"No courses found for student: {student_name}, taught by teacher: {teacher_name}")


def select_11():
    # Середній бал, який певний викладач ставить певному студентові.
    print('\nSelect 11')
    teacher_name = 'Teacher 1'
    student_name = 'Felicia Kelly'

    average_grade_given_by_teacher_to_student = session.query(func.avg(Grade.grade)). \
        join(Subject). \
        join(Teacher). \
        join(Student). \
        filter(Student.student_name == student_name, Teacher.teacher_name == teacher_name). \
        scalar()

    if average_grade_given_by_teacher_to_student is not None:
        print(
            f"Average grade given by {teacher_name} to {student_name}: {average_grade_given_by_teacher_to_student:.2f}")
    else:
        print(f"No grades found for teacher: {teacher_name}, student: {student_name}.")


def select_12():
    # Оцінки студентів у певній групі з певного предмета на останньому занятті.
    print('\nSelect 12')
    group_name = 'Group 1'
    subject_name = 'History'
    last_session_grade = session.query(Grade.grade). \
        join(Student). \
        join(Subject). \
        join(Group). \
        filter(Group.group_name == group_name, Subject.subject_name == subject_name). \
        order_by(desc(Grade.date)). \
        first()

    if last_session_grade:
        print(f"Last session grade for {subject_name} in group {group_name}: {last_session_grade.grade}")
    else:
        print(f"No grades found for {subject_name} in group: {group_name}")


if __name__ == '__main__':
    select_1()
    select_2()
    select_3()
    select_4()
    select_5()
    select_6()
    select_7()
    select_8()
    select_9()
    select_10()
    select_11()
    select_12()

    session.close()