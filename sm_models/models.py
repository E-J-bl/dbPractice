from typing import Optional
import sqlalchemy as sa
import sqlalchemy.orm as so
from sqlalchemy import ForeignKey


# Base is called an Abstract Base Class - our SQL Alchemy models will inherit from this class
class Base(so.DeclarativeBase):
    pass

likes = sa.Table('likes',
                           Base.metadata,
                           sa.Column('id', sa.Integer, primary_key=True),
                           sa.Column('user_id', sa.ForeignKey('users.id')),
                           sa.Column('posts_id', sa.ForeignKey('posts.id')),
                           sa.UniqueConstraint('user_id', 'posts_id'))



class User(Base):
    __tablename__ = "users"
    id: so.Mapped[int] = so.mapped_column(primary_key=True, autoincrement=True)
    name: so.Mapped[str]
    age: so.Mapped[int]
    gender: so.Mapped[str]
    nationality: so.Mapped[str]
    posts:so.Mapped[list["Post"]]=so.relationship('Post',
                                                  order_by="Post.id",
                                                  back_populates="user")
    liked_posts: so.Mapped[list["Post"]]=so.relationship('Post',secondary='likes',
                                                         order_by="Post.id",
                                                         back_populates="liked_posts")


class Post(Base):
    __tablename__ = "posts"
    id: so.Mapped[int] = so.mapped_column(primary_key=True, autoincrement=True)
    title: so.Mapped[str]
    description: so.Mapped[str]
    user: so.Mapped[list["User"]] = so.relationship('User',back_populates="posts")
    user_id: so.Mapped[int]= so.mapped_column(sa.ForeignKey('users.id'))
    liked_by: so.Mapped[int]= so.mapped_column(sa.ForeignKey('likes.user_id'))