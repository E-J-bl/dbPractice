import sqlite3

param_new_user='''
INSERT INTO 
    users (name,age,gender,nationality)
values 
    (?, ?, ?, ?)'''

param_new_post='''
INSERT INTO 
    posts (title,description,user_id)
values 
    (?, ?, ?)
'''

param_new_comments="""
INSERT INTO 
    comments (description,user_id,post_id)
values 
    (?, ?, ?)
"""


param_new_like="""
INSERT INTO 
    likes (user_id,post_id)
values 
    (?, ?)
"""

conn = sqlite3.connect('sm_app.sqlite')
c = conn.cursor()

c.executemany(param_new_user,[('James', 25, 'male', 'USA'),
                              ('Leila', 32, 'female', 'France'),
                              ('Brigitte', 35, 'female', 'England'),
                              ('Mike', 40, 'male', 'Denmark'),
                              ('Elizabeth', 21, 'female', 'Canada'),
                              ])

c.executemany(param_new_post,[('Happy', 'I am feeling very happy today', 1),
                              ('Hot Weather', 'The weather is very hot today', 2),
                              ('Help', 'I need some help with my work', 2),
                              ('Great News', 'I am getting married', 1),
                              ('Interesting Game', 'It was a fantastic game of tennis', 5),
                              ('Party', 'Anyone up for a late-night party today?', 3)
                              ])


c.executemany(param_new_comments,[('Count me in', 1, 6),
                                  ('What sort of help?', 5, 3),
                                  ('Congrats buddy', 2, 4),
                                  ('I was rooting for Nadal though', 4, 5),
                                  ('Help with your thesis?', 2, 3),
                                  ('Many congratulations', 5, 4)])

c.executemany(param_new_like,[(1, 6),
(2, 3),
(1, 5),
(5, 4),
(2, 4),
(4, 2),
(3, 6)
])
conn.commit()
conn.close()