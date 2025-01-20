


import sqlite3

conn = sqlite3.connect('students.sqlite')

with sqlite3.connect('students.sqlite') as conn:
    cursor = conn.cursor()
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


