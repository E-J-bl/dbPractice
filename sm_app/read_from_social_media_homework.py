import sqlite3


# Create a connection to the database
conn = sqlite3.connect("sm_app.sqlite")

# Create a cursor
cursor = conn.cursor()


ex1="""
SELECT text
FROM comments
WHERE text LIKE '%?'
"""

ex2="""
UPDATE users
SET name = 'Lizzy'
WHERE name = 'Elizabeth'
"""

ex3="""
SELECT users.name, count(posts.id)
FROM users inner join posts on users.id = posts.user_id
GROUP BY posts.id;
"""

cursor.execute(ex1)
questions=cursor.fetchall()
cursor.execute(ex2)

cursor.execute(ex3)
num_posts=cursor.fetchall()

conn.commit()
conn.close()
