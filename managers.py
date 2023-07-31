from model import Teacher, Group, Student, Grade, Subject
from connect_db import session
from datetime import datetime
from sqlalchemy import desc


class ModelsManager:
    def __init__(self):
        self.session = session


class TeachersManager(ModelsManager):
    def update(self, args):
        teacher = self.session.query(Teacher).filter_by(teacher_id=args.teacher_id).first()
        if teacher:
            teacher.teacher_name = args.name
            self.session.commit()
            print(f"Teacher with ID={args.teacher_id} updated successfully.")
        else:
            print(f"Teacher with ID={args.teacher_id} not found.")

    def remove(self, id):
        teacher = self.session.query(Teacher).filter_by(teacher_id=id).first()
        if teacher:
            self.session.delete(teacher)
            self.session.commit()
            print(f"Teacher with ID={id} removed successfully.")
        else:
            print(f"Teacher with ID={id} not found.")

    def create(self, args):
        teacher = Teacher(teacher_name=args.name)
        self.session.add(teacher)
        self.session.commit()
        print(f"Teacher '{args.name}' created successfully.")

    def list(self):
        teachers = self.session.query(Teacher).all()
        print("Teachers:")
        for teacher in teachers:
            print(f"ID: {teacher.teacher_id}, Name: {teacher.teacher_name}")


class StudentsManager(ModelsManager):
    def update(self, args):
        student = self.session.query(Student).filter_by(student_id=args.id).first()
        if student:
            student.student_name = args.name
            student.group_id = args.group_id
            self.session.commit()
            print(f"Student with ID={args.id} updated successfully.")
        else:
            print(f"Student with ID={args.id} not found.")

    def remove(self, id):
        print(id)
        student = self.session.query(Student).filter_by(student_id=id).first()
        if student:
            self.session.delete(student)
            self.session.commit()
            print(f"Student with ID={id} removed successfully.")
        else:
            print(f"Student with ID={id} not found.")

    def create(self, args):
        student = Student(student_name=args.name, group_id=args.group_id)
        self.session.add(student)
        self.session.commit()
        print(f"Student '{args.name}' created successfully.")

    def list(self):
        students = self.session.query(Student).all()
        print("Students:")
        for student in students:
            print(f"ID: {student.student_id}, Name: {student.student_name}, Group id: {student.group_id}")


class GroupsManager(ModelsManager):
    def update(self, args):
        group = self.session.query(Group).filter_by(id=args.id).first()
        if group:
            group.group_name = args.name
            self.session.commit()
            print(f"Group with ID={args.id} updated successfully.")
        else:
            print(f"Group with ID={args.id} not found.")

    def remove(self, id):
        group = self.session.query(Group).filter_by(id=id).first()
        if group:
            self.session.delete(group)
            self.session.commit()
            print(f"Group with ID={id} removed successfully.")
        else:
            print(f"Group with ID={id} not found.")

    def create(self, args):
        group = Group(group_name=args.name)
        self.session.add(group)
        self.session.commit()
        print(f"Group '{args.name}' created successfully.")

    def list(self):
        groups = self.session.query(Group).all()
        print("Groups:")
        for group in groups:
            print(f"ID: {group.id}, Name: {group.group_name}")


class SubjectsManager(ModelsManager):
    def update(self, args):
        subject = self.session.query(Subject).filter_by(subject_id=args.id).first()
        if subject:
            subject.subject_name = args.name
            subject.teacher_id = args.teacher_id
            self.session.commit()
            print(f"Subject with ID={args.id} updated successfully.")
        else:
            print(f"Subject with ID={args.id} not found.")

    def remove(self, id):
        subject = self.session.query(Subject).filter_by(subject_id=id).first()
        if subject:
            self.session.delete(subject)
            self.session.commit()
            print(f"Subject with ID={id} removed successfully.")
        else:
            print(f"Subject with ID={id} not found.")

    def create(self, args):
        subject = Subject(subject_name=args.name, teacher_id=args.teacher_id)
        self.session.add(subject)
        self.session.commit()
        print(f"Subject '{args.name}' created successfully.")

    def list(self):
        subjects = self.session.query(Subject).all()
        print("Subjects:")
        for subject in subjects:
            print(f"ID: {subject.subject_id}, Name: {subject.subject_name}")


class GradesManager(ModelsManager):
    def update(self, args):
        grade = self.session.query(Grade).filter_by(grade_id=args.id).first()
        if grade:
            grade.subject_id = args.name
            grade.teacher_id = args.teacher_id
            grade.date = datetime.now()
            self.session.commit()
            print(f"Grade with ID={args.id} updated successfully.")
        else:
            print(f"Grade with ID={args.id} not found.")

    def remove(self, id):
        grade = self.session.query(Grade).filter_by(grade_id=id).first()
        if grade:
            self.session.delete(grade)
            self.session.commit()
            print(f"Grade with ID={id} removed successfully.")
        else:
            print(f"Grade with ID={id} not found.")

    def create(self, args):
        print(args)
        grade = Grade(grade=args.grade, subject_id=args.subject_id, student_id=args.student_id, date=datetime.now())
        self.session.add(grade)
        self.session.commit()
        print(f"Grade '{args.grade}' for student ID {args.student_id} created successfully.")

    def list(self):
        grades = self.session.query(Grade). \
            order_by(desc(Grade.date)). \
            all()
        print("Subjects:")
        for grade in grades:
            print(f"ID: {grade.grade_id}, Student ID: {grade.student_id}, Grade: {grade.grade}, "
                  f"Subject ID: {grade.subject_id}, Date: {grade.date}")
