import sqlite3
conn = sqlite3.connect('students.sqlite')
cursor = conn.cursor()

select_students='''
SELECT id, firstname, lastname, gender, age 
FROM students
where age>=15'''

cursor.execute(select_students)

first_student = cursor.fetchone()
more_students=cursor.fetchmany(5)
other_students=cursor.fetchall()
conn.close()

print(first_student,more_students,other_students,sep='\n')