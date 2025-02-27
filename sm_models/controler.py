import sqlalchemy as sa
import sqlalchemy.orm as so

from models import User,Post,Comment

class Controller:
    def __init__(self):
        self.current_user=None
        self.engine=sa.create_engine('sqlite:///social_media.db')

    def set_current_user(self,user):
        with so.Session(bind=self.engine) as session:
            self.current_user=session.scalar(sa.select(User).where(User.name==user).one_or_none())

    def get_user_names(self)-> list[str]:
        with so.Session(bind=self.engine) as session:
            user_names=session.scalar(sa.select(User.name).where(User.name!=None).order_by(User.name)).all()
        return list(user_names)

    def create_user(self,name,age,gender,nationality):
        with so.Session(bind=self.engine) as session:
            user=User(name,age,gender,nationality)
            session.add(user)
            session.commit()
            self.current_user=user
        return user

    def get_posts(self,user_name):
        with so.Session(bind=self.engine) as session:
            user=session.scalar(sa.select(User).where(User.name==user_name).one_or_none())
            post_info=[{
              'title':post.title,
                'description':post.description,
                'number_likes':len(post.liked_by_users),
            } for post in user.posts]
        return post_info


    def get_comments(self,post_id):
        with so.Session(bind=self.engine) as session:
            post=session.scalar(sa.select(Post).where(Post.id==post_id).one_or_none())
            comment_info=[{
              'user_name':comment.user.name,
                'comment':comment.comment,
            } for comment in post.comments]
        return comment_info


    def like_post(self,post_id):
        with so.Session(bind=self.engine) as session:
            likes=session.get(Post,post_id)
            likes=len(likes.liked_by_users)
        return likes