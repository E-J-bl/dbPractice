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


average_query="""
select avg(age)
from students
where gender=?
"""
average_age= cursor.execute(average_query,("F",)).fetchone()[0]

group_by_query="""
Select gender, avg(age)
from students
group by gender
"""

average_age_by_gender= cursor.execute(group_by_query).fetchall()



conn.close()

print(first_student,more_students,other_students,sep='\n', end="\n\n")

print(average_age)
print(average_age_by_gender)