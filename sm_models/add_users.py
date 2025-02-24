import sqlalchemy as sa
import sqlalchemy.orm as so
from models import User, Post, Base

# Create an engine
engine = sa.create_engine('sqlite:///social_media.db', echo=True)
session = so.Session(bind=engine)

# Create examples of Users
users = [User(name="Alice", age=30, gender="Female", nationality="Canadian"),
         User(name="Bob", age=25, gender="Male", nationality="American"),
         User(name="Charlie", age=28, gender="Male", nationality="British"),
         User(name="Diana", age=22, gender="Female", nationality="Australian"),
         ]

# Create examples of Posts
posts = [Post(title="Exploring the Rocky Mountains",
             description="Just returned from an amazing trip to the Rockies! "
                         "The views were breathtaking and the hikes were exhilarating.",
             ),
         Post(title="My Favorite Recipes",
             description="Sharing some of my favorite recipes, including a "
                         "delicious chocolate cake and a savory lasagna."
             ),
         Post(title="Tech Innovations in 2025",
             description="Discussing the latest tech innovations, "
                         "including advancements in AI, quantum computing, and renewable energy.",
             ),
         Post(title="Travel Tips for Australia",
             description="Planning a trip to Australia? Here are some tips to make your journey unforgettable, "
                         "from must-see destinations to local cuisine."),
         ]

for i in range(len(users)):
    users[i].posts.append(posts[i])

# Add likes
users[0].liked_posts.append(posts[1])
users[0].liked_posts.append(posts[2])
users[1].liked_posts.append(posts[0])
users[1].liked_posts.append(posts[3])
users[2].liked_posts.append(posts[0])
users[2].liked_posts.append(posts[3])
users[3].liked_posts.append(posts[1])
users[3].liked_posts.append(posts[2])

session.add_all(users)
session.commit()

