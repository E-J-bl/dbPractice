import sqlalchemy as sa
import sqlalchemy.orm as so

from models import User, Post, Comment
import pyinputplus as pyip


class Controller:
    def __init__(self, db_location='sqlite:///social_media.db'):
        self.current_user = None
        self.engine = sa.create_engine(db_location)

    def set_current_user_from_name(self, name):
        with so.Session(bind=self.engine) as session:
            self.current_user = session.scalars(sa.select(User).where(User.name == name)).one_or_none()

    def get_user_names(self) -> list[str]:
        with so.Session(bind=self.engine) as session:
            user_names = session.scalars(sa.select(User.name).order_by(User.name)).all()
        return list(user_names)

    def create_user(self, name: str, age: int, gender: str, nationality: str) -> User:
        with so.Session(bind=self.engine) as session:
            user = User(name=name, age=age, gender=gender, nationality=nationality)
            session.add(user)
            session.commit()
            self.current_user = user
        return user

    def get_posts(self, user_name: str) -> list[dict]:
        with so.Session(bind=self.engine) as session:
            user_names=self.get_user_names()
            print(user_names,user_name)
            if user_name not in user_names:
                return [{"title":'Not a valid user',"description":"Please enter a valid user name","number_likes":0}]
            user = session.scalars(sa.select(User).where(User.name == user_name)).one_or_none()
            posts_info = [{'id': post.id,
                           'title': post.title,
                           'description': post.description,
                           'number_likes': len(post.liked_by_users),
                           }
                          for post in user.posts]
        return posts_info

    def get_all_posts(self) -> list[dict]:
        with so.Session(bind=self.engine) as session:
            allp = session.scalars(sa.select(User)).all()
            posts_info = [{'id': post.id,
                           'title': post.title,
                           'description': post.description,
                           'number_likes': len(post.liked_by_users),
                           }
                          for user in allp
                          for post in user.posts]
        return posts_info


class CLI:
    def __init__(self):
        self.controller = Controller()
        self.login()

    @staticmethod
    def show_title(title):
        print('\n' + title)
        print('-' * len(title) + '\n')

    def login(self):
        self.show_title('Login Screen')
        users = self.controller.get_user_names()
        menu_items = users + ['Create a new account',
                              'Exit',
                              ]
        menu_choice = pyip.inputMenu(menu_items,
                                     prompt='Select user or create a new account\n',
                                     numbered=True,
                                     )
        if menu_choice.lower() == 'create a new account':
            self.create_account()
        elif menu_choice.lower() == 'exit':
            print('Goodbye')
        else:
            user_name = menu_choice
            self.controller.set_current_user_from_name(user_name)
            self.user_home()

    def create_account(self, existing_users=None):
        self.show_title('Create Account Screen')
        print('Enter Account Details')
        user_name = pyip.inputStr('Username: ', blockRegexes=existing_users, strip=None)
        age = pyip.inputInt('Age: ', min=0, max=150, blank=True)
        gender = pyip.inputMenu(['male', 'female', 'other'], prompt='Gender: ', blank=True)
        nationality = pyip.inputStr('Nationality: ')
        self.controller.create_user(user_name, age, gender, nationality)
        self.login()

    def user_home(self):
        self.show_title(f'{self.controller.current_user.name} Home Screen')
        print(f'Name: {self.controller.current_user.name}')
        print(f'Age: {self.controller.current_user.age}')
        print(f'Nationality: {self.controller.current_user.nationality}')


        menu_items = {'Show posts from another user': [self.show_posts,[]],
                      'Look up user':[self.search_user,[]],
                      'Show your posts':[self.search_user,[self.controller.current_user.name]],
                      'Logout': [self.login,[]]}

        menu_choice = pyip.inputMenu(list(menu_items.keys()),
                                     prompt='Select an action\n',
                                     numbered=True,
                                     )
        menu_items[menu_choice][0](*menu_items[menu_choice][1])
        if menu_choice != 'Logout':
            self.user_home()

    def show_posts(self, user_name: str | None = None):
        if user_name is None:
            users = self.controller.get_user_names()
            menu_choice = pyip.inputMenu(users+["All"],
                                         prompt='Select a user\n',
                                         numbered=True,
                                         )
            user_name = menu_choice

        self.show_title(f"{user_name}'s Posts")
        if user_name != 'All':
            posts = self.controller.get_posts(user_name)
            for post in posts:
                print(f'Title: {post["title"]}')
                print(f'Content: {post["description"]}')
                print(f'Likes: {post["number_likes"]}')

            if not posts:
                print('No Posts')
        else:
            posts = self.controller.get_all_posts()
            for post in posts:
                print(f'Title: {post["title"]}')
                print(f'Content: {post["description"]}')
                print(f'Likes: {post["number_likes"]}')

            if not posts:
                print('No Posts')

    def search_user(self, user_name: str | None = None):
        user=user_name
        if user_name is None:
            user= input('Enter username: ')

        posts = self.controller.get_posts(user)
        print("PRINTING POSTS")
        for post in posts:
            print(f'Title: {post["title"]}')
            print(f'Content: {post["description"]}')
            print(f'Likes: {post["number_likes"]}')

        if not posts:
            print('No Posts')

        continues=input('Continue? (y/n) ')
        if continues.lower() == 'y':
            self.search_user()

cli = CLI()
controller = Controller()