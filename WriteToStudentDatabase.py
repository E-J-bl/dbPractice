
import random
from faker import Faker
import sqlite3

fake = Faker('en_GB')
conn = sqlite3.connect('students.sqlite')

parameterised_insert_query="""
INSERT INTO 
    students (firstname, lastname, age, gender)
values 
    (?, ?, ?, ?)
"""

cursor = conn.cursor()

fake.random.seed(42)
random.seed(42)

for _ in range(10):
    f_name = fake.first_name()
    l_name = fake.last_name()
    age=random.randint(10,20)
    gender=random.choice(['M','F','NB','O'])
    cursor.execute(parameterised_insert_query,(f_name,l_name,age,gender))




insert_query = """
INSERT INTO students (firstname,lastname ,age,gender)
 VALUES 
        ('Milan','Gal',69,'Eye of Rah'),
        ('Eleanore','Shiner',1000,'amogus'),
        ('Rayhan','Chowdhury','Eternal','Existence'),
        ('Denys','Zazuliak',0,'GOD'),
        ('Adam','Reeves',16,'Male'),
        ('Sami','Hafezgi',100,'Soliaire');
        
"""
cursor.execute(insert_query)


conn.commit()
conn.close()

