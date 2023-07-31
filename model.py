from sqlalchemy import Column, Integer, String, ForeignKey, Date, CheckConstraint
from sqlalchemy.orm import declarative_base, relationship
from connect_db import session

Base = declarative_base()


class Group(Base):
    __tablename__ = 'groups'
    id = Column(Integer, primary_key=True)
    group_name = Column(String(100), nullable=False)


class Student(Base):
    __tablename__ = 'students'
    student_id = Column(Integer, primary_key=True)
    student_name = Column(String(100), nullable=False)
    group_id = Column(Integer, ForeignKey('groups.id', ondelete="CASCADE"))
    group = relationship(Group)


class Teacher(Base):
    __tablename__ = 'teachers'
    teacher_id = Column(Integer, primary_key=True)
    teacher_name = Column(String(100), nullable=False)


class Subject(Base):
    __tablename__ = 'subjects'
    subject_id = Column(Integer, primary_key=True)
    subject_name = Column(String(100), nullable=False)
    teacher_id = Column(Integer, ForeignKey('teachers.teacher_id', ondelete="CASCADE"))
    teacher = relationship(Teacher)


class Grade(Base):
    __tablename__ = 'grades'
    __table_args__ = (
        CheckConstraint('grade >= 1'),
        CheckConstraint('grade <= 100'),
    )

    grade_id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey('students.student_id', ondelete="CASCADE"))
    subject_id = Column(Integer, ForeignKey('subjects.subject_id', ondelete="CASCADE"))
    grade = Column('grade', Integer, nullable=False)
    date = Column(Date, nullable=False)
    student = relationship(Student)
    subject = relationship(Subject)


session.close()
