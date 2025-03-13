import pytest
import sqlalchemy as sa
import sqlalchemy.orm as so
from sqlalchemy.exc import IntegrityError


from cli_and_database.models import (User,Comment,Post,Base)
from cli_and_database.write_to_db import write_initial_data
from cli_and_database.CLI import Controller



test_db_location="sqlite:///test_database.db"


def test_test():
    assert 3**2==9



class TestDatabase:
    @pytest.fixture(scope="class")
    def db_session(self):
        engine = sa.create_engine(test_db_location)
        Base.metadata.create_all(engine)
        session=so.Session(engine)
        yield session
        session.close()
        Base.metadata.drop_all(engine)

    def test_valid_user(self,db_session):
        user=User(name="Rayhan",age=20,gender="male")
        db_session.add(user)
        db_session.commit()
        qry=sa.select(User).where(User.name=="Rayhan")
        rayhan=db_session.scalar(qry)
        assert rayhan is not None
        assert rayhan.name == "Rayhan"
        assert rayhan.age == 20
        assert rayhan.gender == "male"
        assert rayhan.nationality is None
        db_session.rollback()

    def test_invalid_user(self,db_session):
        user=User(age=7,nationality='uk')
        db_session.add(user)
        with pytest.raises(IntegrityError):
            db_session.commit()

        db_session.rollback()


    def test_add_post(self,db_session):
        user = User(name="ray", age=20, gender="male")
        db_session.add(user)
        db_session.commit()
        post=Post(title="Test",description="test content",user=user)
        db_session.add(post)
        db_session.commit()
        qry=sa.select(Post).where(Post.title=="Test")
        po=db_session.scalar(qry)
        assert po is not None
        assert po.description=="test content"
        db_session.rollback()

    def test_comment(self,db_session):
        user = User(name="r", age=210, gender="f")
        db_session.add(user)
        db_session.commit()
        post = Post(title="Tes 3t", description="test content 3", user=user)
        db_session.add(post)
        db_session.commit()
        comment=Comment(user=user,post=post,comment='test response')
        db_session.add(comment)
        db_session.commit()

        db_session.rollback()
    def test_like_post(self,db_session):
        user = User(name="rale", age=130, gender="Other")
        db_session.add(user)
        db_session.commit()
        post = Post(title="test2", description="test content 2", user=user)
        db_session.add(post)
        db_session.commit()
        user.liked_posts.append(post)
        assert post in user.liked_posts
        with pytest.raises(IntegrityError):
            user.liked_posts.append(post)
            db_session.commit()

        db_session.rollback()


class TestController:
    @pytest.fixture(scope="class",autouse=True)
    def test_db(self):
        engine = sa.create_engine(test_db_location)
        Base.metadata.create_all(engine)
        write_initial_data(engine)
        yield
        #afthe the fixture is used drop the data from the database
        Base.metadata.drop_all(engine)

    @pytest.fixture(scope="class")
    def controller(self):
        control = Controller(db_location=test_db_location)
        return control

    def test_set_current_user_from_name(self,controller):
        controller.set_current_user_from_name(name="Alice")
        assert "Alice" == controller.current_user.name
        assert controller.current_user.id==1
        assert 30 == controller.current_user.age

    def test_get_user_names(self,controller):
        users=controller.get_user_names()
        assert len(users)==4
        assert users==['Alice','Bob','Charlie','Diana']

    def test_create_user(self,controller):
        us=controller.create_user('Ethil',74,'female','American')
        assert controller.current_user.name=='Ethil'
        assert controller.current_user.age==74
        assert controller.current_user.gender=="female"
        assert controller.current_user.nationality=='American'

    def test_get_posts(self):
        assert False

    def test_create_post(self):
        assert False

    def test_like_post(self):
        assert False

    def test_liked_by_user(self):
        assert False

    def test_make_comment(self):
        assert False

