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
average_age= cursor.execute(average_query,("F",)).fetchall()[0][0]

group_by_query="""
Select gender, avg(age)
from students
group by gender
"""

average_age_by_gender= cursor.execute(group_by_query).fetchall()


j_start_query="""
select firstname
from students
where firstname like 'J%'
"""

j_start_response=cursor.execute(j_start_query).fetchall()[0:5]


number_per_gender_query="""
select gender,count(gender)
from students
group by gender"""

gender_count=cursor.execute(number_per_gender_query).fetchall()

number_firstname_count_query="""
select substring(firstname,1,1), sum(age)
from students
group by substring(firstname,1,1)
"""

age_sum_result=cursor.execute(number_firstname_count_query).fetchall()
conn.close()

print(first_student,more_students,other_students,sep='\n', end="\n\n")

print(average_age)
print(sorted(average_age_by_gender,key=lambda s:s[1]))

print(j_start_response)

print(sorted(gender_count,key=lambda s:s[1]))

print(sorted(age_sum_result,key=lambda s:s[1]))