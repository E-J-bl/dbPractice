import sqlite3
from tabulate import tabulate

def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
    except sqlite3.Error as e:
        print(f"The error '{e}' occurred")
    return result


select_users = "SELECT * from users"
with sqlite3.connect("sm_app.sqlite") as conn:
    users = execute_read_query(conn, select_users)
users.insert(0,     ('id','name','age','gender','nationality'))
print(tabulate(users[1:], headers=users[0], tablefmt="psql"))

select_user_activity = """
SELECT users.id,users.id,users.name,posts.description, comments.description 
from  posts 
join comments on  posts.user_id = comments.user_id
join users on  posts.user_id = users.id;"""


with sqlite3.connect("sm_app.sqlite") as conn:
    users_activity = execute_read_query(conn, select_user_activity)

for user in users_activity:
    print(user)


select_posts_comments_users="""
"""