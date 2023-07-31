"""Init

Revision ID: fd3d86b2cf58
Revises: 
Create Date: 2023-07-31 20:14:55.498571

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fd3d86b2cf58'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('groups',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('group_name', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('teachers',
    sa.Column('teacher_id', sa.Integer(), nullable=False),
    sa.Column('teacher_name', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('teacher_id')
    )
    op.create_table('students',
    sa.Column('student_id', sa.Integer(), nullable=False),
    sa.Column('student_name', sa.String(length=100), nullable=False),
    sa.Column('group_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['group_id'], ['groups.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('student_id')
    )
    op.create_table('subjects',
    sa.Column('subject_id', sa.Integer(), nullable=False),
    sa.Column('subject_name', sa.String(length=100), nullable=False),
    sa.Column('teacher_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['teacher_id'], ['teachers.teacher_id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('subject_id')
    )
    op.create_table('grades',
    sa.Column('grade_id', sa.Integer(), nullable=False),
    sa.Column('student_id', sa.Integer(), nullable=True),
    sa.Column('subject_id', sa.Integer(), nullable=True),
    sa.Column('grade', sa.Integer(), nullable=False),
    sa.Column('date', sa.Date(), nullable=False),
    sa.CheckConstraint('grade <= 100'),
    sa.CheckConstraint('grade >= 1'),
    sa.ForeignKeyConstraint(['student_id'], ['students.student_id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['subject_id'], ['subjects.subject_id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('grade_id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('grades')
    op.drop_table('subjects')
    op.drop_table('students')
    op.drop_table('teachers')
    op.drop_table('groups')
    # ### end Alembic commands ###
