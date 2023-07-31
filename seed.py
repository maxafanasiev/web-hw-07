import random
from faker import Faker
from datetime import datetime, timedelta
from connect_db import session
from model import Group, Student, Subject, Grade, Teacher

faker = Faker()

if __name__ == '__main__':
    subjects_data = [
        'Mathematics',
        'Physics',
        'Chemistry',
        'Biology',
        'History'
    ]

    for i in range(1, 4):
        new_group = Group(group_name=f"Group {i}")
        session.add(new_group)
        session.commit()

    for i in range(1, 6):
        new_teacher = Teacher(teacher_name=f"Teacher {i}")
        session.add(new_teacher)
        session.commit()

    for i in range(50):
        new_student = Student(student_name=faker.name(), group_id=random.randint(1, 3))
        session.add(new_student)
        session.commit()

    for t_id, subj in enumerate(subjects_data):
        new_subject = Subject(subject_name=subj, teacher_id=t_id+1)
        session.add(new_subject)
        session.commit()

    for st_id in range(1, 51):
        for gr in range(20):
            new_grade = Grade(student_id=st_id,
                              subject_id=random.randint(1, 5),
                              grade=random.randint(1, 100),
                              date=datetime.now()-timedelta(random.randint(1, 200))
                              )
            session.add(new_grade)
            session.commit()

    session.close()
