import sqlite3
conn = sqlite3.connect('students.sqlite')
cursor = conn.cursor()

select_students='''
SELECT id, first_name, last_name, gender 
FROM students
where age>=15'''
cursor.execute(select_students)
first_student = cursor.fetchone()
more_students=cursor.fetchmany(10)
other_students=cursor.fetchall()
conn.close()