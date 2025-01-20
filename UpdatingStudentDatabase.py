import sqlite3
from ast import increment_lineno

conn = sqlite3.connect('students.sqlite')
cursor = conn.cursor()

update_query="""
UPDATE students 
set lastname= ?
where id=4;"""


cursor.execute(update_query,("Smith"))
conn.commit()

increment_age_query='''
update students 
set age= age+1
'''
cursor.execute(increment_age_query)
conn.commit()
conn.close()

