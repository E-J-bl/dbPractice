import sqlite3

conn = sqlite3.connect('students.sqlite')
c = conn.cursor()

clear_student_table="""
delete from students"""

c.execute(clear_student_table)
conn.commit()