import pytest
import sqlalchemy as sa
import sqlalchemy.orm as so
from sqlalchemy.exc import IntegrityError


from models import User,Comment,Post,Base


test_db_location="sqlite:///:memory:"


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


