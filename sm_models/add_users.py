from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from models import User, Post



people = [User(name="A",age=25,gender="Male",nationality="French"),
          User(name="B",age=35,gender="Female",nationality="French"),
          User(name="C",age=105,gender="NB",nationality="French"),]
posts = [Post(title="A", description="Hello world!",),]


people[0].posts.append(posts[0])

people[1].liked_posts.append(posts[0])