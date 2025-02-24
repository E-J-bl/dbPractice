from typing import Optional
import sqlalchemy as sa
import sqlalchemy.orm as so
from sqlalchemy import ForeignKey


# Base is called an Abstract Base Class - our SQL Alchemy models will inherit from this class
class Base(so.DeclarativeBase):
    pass


likes_table = sa.Table(
    'likes',
    Base.metadata,
    sa.Column('id', sa.Integer, primary_key=True),
    sa.Column('user_id', sa.Integer, sa.ForeignKey('users.id'), nullable=False),
    sa.Column('post_id', sa.Integer, sa.ForeignKey('posts.id'), nullable=False),
)



class User(Base):
    __tablename__ = "users"
    id: so.Mapped[int] = so.mapped_column(primary_key=True, autoincrement=True)
    name: so.Mapped[str]
    age: so.Mapped[int]
    gender: so.Mapped[str]
    nationality: so.Mapped[str]
    posts:so.Mapped[list["Post"]]=so.relationship(back_populates="user")
    liked_posts: so.Mapped[list['Post']] = so.relationship(secondary=likes_table, back_populates='liked_by_users')



class Post(Base):
    __tablename__ = "posts"
    id: so.Mapped[int] = so.mapped_column(primary_key=True, autoincrement=True)
    title: so.Mapped[str]
    description: so.Mapped[str]
    user: so.Mapped[list["User"]] = so.relationship('User',back_populates="posts")
    user_id: so.Mapped[int]= so.mapped_column(sa.ForeignKey('users.id'))
    liked_by_users: so.Mapped[list["User"]]= so.relationship(secondary=likes_table, back_populates='liked_posts')

class Comment(Base):
    __tablename__ = 'comments'
    id: so.Mapped[int] = so.mapped_column(primary_key=True, autoincrement=True)
    user_id: so.Mapped[int] = so.mapped_column(sa.ForeignKey('users.id'))
    post_id: so.Mapped[int] = so.mapped_column(sa.ForeignKey('posts.id'))
    comment: so.Mapped[str]
    post: so.Mapped['Post'] = so.relationship(back_populates='comments')
    user: so.Mapped['User'] = so.relationship(back_populates='comments_made')

    def __repr__(self):
        return f"Comment(user_id={self.user_id}, post_id={self.post_id}, comment='{self.comment}')"